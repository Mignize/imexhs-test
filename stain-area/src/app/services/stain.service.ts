import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

export interface Calculation {
  timestamp: Date;
  points: number;
  inside: number;
  areaEstimate: number;
  imageUrl: string;
}

@Injectable({ providedIn: 'root' })
export class StainService {
  private resultsSubject = new BehaviorSubject<Calculation[]>([]);
  results$ = this.resultsSubject.asObservable();

  constructor() {}

  calculateArea(
    imageData: ImageData,
    n: number,
    imageUrl: string
  ): Calculation {
    const totalArea = imageData.width * imageData.height;
    let inside = 0;
    for (let i = 0; i < n; i++) {
      const x = Math.floor(Math.random() * imageData.width);
      const y = Math.floor(Math.random() * imageData.height);
      const idx = (y * imageData.width + x) * 4;
      if (imageData.data[idx] === 255) inside++;
    }
    const estimate = (totalArea * inside) / n;
    const calc: Calculation = {
      timestamp: new Date(),
      points: n,
      inside,
      areaEstimate: estimate,
      imageUrl,
    };
    this.pushResult(calc);
    return calc;
  }

  private pushResult(calc: Calculation) {
    const updated = [calc, ...this.resultsSubject.value];
    this.resultsSubject.next(updated);
  }

  deleteResult(result: Calculation) {
    const updated = this.resultsSubject.value.filter((r) => r !== result);
    this.resultsSubject.next(updated);
  }

  clearResults() {
    this.resultsSubject.next([]);
  }
}
