import { Routes } from '@angular/router';
import { UploadCalc } from './components/upload-calc/upload-calc';
import { ResultsTable } from './components/results-table/results-table';

export const routes: Routes = [
  { path: 'calculate', component: UploadCalc },
  { path: 'results', component: ResultsTable },
  { path: '', redirectTo: 'calculate', pathMatch: 'full' },
];
