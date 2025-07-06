import { Component } from '@angular/core';
import { NgClass } from '@angular/common';
import { MethodologyCarousel } from './components/methodology-carousel/methodology-carousel';
import { UploadCalc } from './components/upload-calc/upload-calc';
import { ResultsTable } from './components/results-table/results-table';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [NgClass, MethodologyCarousel, UploadCalc, ResultsTable],
  template: `
    <div class="w-full max-w-3xl mx-auto mt-8">
      <div class="flex border-b mb-6">
        <button
          (click)="tab = 0"
          [class.font-bold]="tab === 0"
          class="px-4 py-2 focus:outline-none"
          [ngClass]="
            tab === 0
              ? 'border-b-2 border-blue-600 text-blue-600'
              : 'text-gray-600'
          "
        >
          Calculate area
        </button>
        <button
          (click)="tab = 1"
          [class.font-bold]="tab === 1"
          class="px-4 py-2 focus:outline-none"
          [ngClass]="
            tab === 1
              ? 'border-b-2 border-blue-600 text-blue-600'
              : 'text-gray-600'
          "
        >
          Previous results
        </button>
      </div>
      @if (tab === 0) {
      <div class="flex flex-col gap-6">
        <app-methodology-carousel></app-methodology-carousel>
        <app-upload-calc></app-upload-calc>
      </div>
      } @if (tab === 1) {
      <app-results-table></app-results-table>
      }
    </div>
  `,
})
export class AppComponent {
  tab = 0;
}
