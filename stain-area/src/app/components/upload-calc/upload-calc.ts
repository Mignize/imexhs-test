import { Component, ViewChild, ElementRef } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { StainService, Calculation } from '../../services/stain.service';

@Component({
  selector: 'app-upload-calc',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './upload-calc.html',
  styleUrls: ['./upload-calc.css'],
})
export class UploadCalc {
  points = 100;
  imageData?: ImageData;
  imageUrl?: string;
  isBinary: boolean = true;
  resultMessage: string = '';
  errorMessage: string = '';
  showResult: boolean = false;
  dragActive: boolean = false;
  pointsOverlay: { x: number; y: number }[] = [];
  @ViewChild('overlayCanvas') overlayCanvas?: ElementRef<HTMLCanvasElement>;
  @ViewChild('fileUploadInput') fileUploadInput?: ElementRef<HTMLInputElement>;

  constructor(private stainService: StainService) {}

  onFile(event: Event) {
    this.errorMessage = '';
    let file: File | null = null;
    if (event instanceof DragEvent && event.dataTransfer) {
      file = event.dataTransfer.files[0];
    } else {
      const input = event.target as HTMLInputElement;
      if (!input.files || !input.files[0]) {
        this.errorMessage = 'No file selected';
        return;
      }
      file = input.files[0];
    }
    if (file) {
      const reader = new FileReader();
      reader.onload = (e: any) => {
        const img = new Image();
        img.onload = () => {
          const canvas = document.createElement('canvas');
          canvas.width = img.width;
          canvas.height = img.height;
          const ctx = canvas.getContext('2d');
          if (ctx) {
            ctx.drawImage(img, 0, 0);
            let imageData = ctx.getImageData(0, 0, img.width, img.height);
            this.binarizeImage(imageData);
            ctx.putImageData(imageData, 0, 0);
            this.imageData = imageData;
            this.imageUrl = canvas.toDataURL();
            this.pointsOverlay = [];
            this.updateOverlay();
          }
        };
        img.src = e.target.result;
      };
      reader.readAsDataURL(file);
    }
  }

  onDrop(event: DragEvent) {
    event.preventDefault();
    this.dragActive = false;
    this.onFile(event);
  }

  onAreaClick(event: Event) {
    if (this.fileUploadInput) {
      this.fileUploadInput.nativeElement.click();
    }
  }

  binarizeImage(imageData: ImageData) {
    const data = imageData.data;
    for (let i = 0; i < data.length; i += 4) {
      const lum = 0.299 * data[i] + 0.587 * data[i + 1] + 0.114 * data[i + 2];
      const v = lum > 127 ? 255 : 0;
      data[i] = data[i + 1] = data[i + 2] = v;
      data[i + 3] = 255;
    }
  }

  calc() {
    this.showResult = false;
    this.pointsOverlay = [];
    if (this.imageData && this.isBinary) {
      const width = this.imageData.width;
      const height = this.imageData.height;
      for (let i = 0; i < this.points; i++) {
        this.pointsOverlay.push({
          x: Math.random() * width,
          y: Math.random() * height,
        });
      }
      setTimeout(() => this.updateOverlay(), 50);
      const result: Calculation = this.stainService.calculateArea(
        this.imageData,
        this.points,
        this.imageUrl || ''
      );
      this.resultMessage = `Estimated area: ${result.areaEstimate.toFixed(
        2
      )} px²`;
      this.showResult = true;
    } else if (!this.isBinary) {
      this.errorMessage = 'Cannot calculate: the image is not binary.';
    }
  }

  updateOverlay() {
    setTimeout(() => {
      if (this.overlayCanvas && this.imageData && this.pointsOverlay.length) {
        const canvas = this.overlayCanvas.nativeElement;
        const ctx = canvas.getContext('2d');
        if (ctx) {
          ctx.clearRect(0, 0, canvas.width, canvas.height);
          ctx.save();
          ctx.globalCompositeOperation = 'source-over';
          ctx.fillStyle = '#ff0000';
          ctx.strokeStyle = '#fff';
          ctx.lineWidth = 1.5;
          for (const p of this.pointsOverlay) {
            ctx.beginPath();
            ctx.arc(p.x, p.y, 5, 0, 2 * Math.PI);
            ctx.fill();
            ctx.stroke();
          }
          ctx.restore();
        }
      }
    }, 0);
  }
}
