import { StainService } from './stain.service';

describe('StainService', () => {
  let service: StainService;

  beforeEach(() => {
    service = new StainService();
  });

  it('should calculate area correctly for all white', () => {
    const width = 10,
      height = 10,
      n = 100;
    const data = new Uint8ClampedArray(width * height * 4).fill(255);
    const imageData = { width, height, data } as ImageData;
    const result = service.calculateArea(imageData, n, 'img');
    expect(result.inside).toBe(n);
    expect(result.areaEstimate).toBe(width * height);
  });

  it('should delete a result', () => {
    const width = 2,
      height = 2,
      n = 4;
    const data = new Uint8ClampedArray(width * height * 4).fill(255);
    const imageData = { width, height, data } as ImageData;
    const result = service.calculateArea(imageData, n, 'img');
    service.deleteResult(result);
    service.results$.subscribe((results) => {
      expect(results.length).toBe(0);
    });
  });
});
