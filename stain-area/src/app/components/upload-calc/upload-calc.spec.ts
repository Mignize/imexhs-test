import { ComponentFixture, TestBed } from '@angular/core/testing';

import { UploadCalc } from './upload-calc';

describe('UploadCalc', () => {
  let component: UploadCalc;
  let fixture: ComponentFixture<UploadCalc>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [UploadCalc],
    }).compileComponents();

    fixture = TestBed.createComponent(UploadCalc);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should show error if no file selected', () => {
    const event = { target: { files: null } } as any;
    component.onFile(event);
    expect(component.errorMessage).toBe('No file selected');
  });

  it('should binarize image', () => {
    const data = new Uint8ClampedArray([10, 10, 10, 255, 250, 250, 250, 255]);
    const imageData = { data } as ImageData;
    component.binarizeImage(imageData);
    expect(data[0]).toBe(0);
    expect(data[4]).toBe(255);
  });

  it('should generate and update overlay points', () => {
    component.imageData = {
      width: 10,
      height: 10,
      data: new Uint8ClampedArray(400),
    } as ImageData;
    component.points = 5;
    component.calc();
    expect(component.pointsOverlay.length).toBe(5);
  });
});
