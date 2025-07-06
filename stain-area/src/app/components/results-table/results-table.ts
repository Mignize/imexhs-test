import { Component } from '@angular/core';
import { DatePipe, DecimalPipe, AsyncPipe } from '@angular/common';
import { StainService, Calculation } from '../../services/stain.service';

@Component({
  selector: 'app-results-table',
  standalone: true,
  imports: [DatePipe, DecimalPipe, AsyncPipe],
  templateUrl: './results-table.html',
  styleUrls: ['./results-table.css'],
})
export class ResultsTable {
  results$;
  constructor(private stainService: StainService) {
    this.results$ = this.stainService.results$;
  }

  downloadCSV() {
    this.results$
      .subscribe((results) => {
        if (!results.length) return;
        const header = 'Date;Points;Inside;Estimated Area\n';
        const rows = results
          .map(
            (r) =>
              `${this.formatDate(r.timestamp)};${r.points};${
                r.inside
              };${r.areaEstimate.toFixed(2)}`
          )
          .join('\n');
        const csv = header + rows;
        const blob = new Blob([csv], { type: 'text/csv' });
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'stain_results.csv';
        a.click();
        window.URL.revokeObjectURL(url);
      })
      .unsubscribe();
  }

  formatDate(date: Date | string): string {
    const d = new Date(date);

    return (
      d.getFullYear() +
      '-' +
      String(d.getMonth() + 1).padStart(2, '0') +
      '-' +
      String(d.getDate()).padStart(2, '0') +
      ' ' +
      d.toLocaleTimeString()
    );
  }

  deleteResult(result: Calculation) {
    this.stainService.deleteResult(result);
  }

  clearResults() {
    this.stainService.clearResults();
  }
}
