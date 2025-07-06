import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ResultsTable } from './results-table';

describe('ResultsTable', () => {
  let component: ResultsTable;
  let fixture: ComponentFixture<ResultsTable>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ResultsTable],
    }).compileComponents();

    fixture = TestBed.createComponent(ResultsTable);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should call deleteResult on service', () => {
    const mock = {
      timestamp: new Date(),
      points: 1,
      inside: 1,
      areaEstimate: 1,
      imageUrl: '',
    };
    const spy = spyOn(component['stainService'], 'deleteResult');
    component.deleteResult(mock);
    expect(spy).toHaveBeenCalledWith(mock);
  });

  it('should call clearResults on service', () => {
    const spy = spyOn(component['stainService'], 'clearResults');
    component.clearResults();
    expect(spy).toHaveBeenCalled();
  });
});
