import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MethodologyCarousel } from './methodology-carousel';

describe('MethodologyCarousel', () => {
  let component: MethodologyCarousel;
  let fixture: ComponentFixture<MethodologyCarousel>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [MethodologyCarousel]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MethodologyCarousel);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
