This project implement a simple Angular application to compute the area of a stain in a binary image.

### Main Features

- Image upload: Supports drag & drop or click-to-select. Automatically converts images to binary if needed.
- Visual overlay: Displays random points over the image to illustrate the Monte Carlo method.
- Points adjustment: Slider to select the number of random points for estimation.
- Results: Table with calculation history, CSV export, individual and total deletion.
- Accessibility: Keyboard navigation, ARIA roles, tooltips, and contextual help.
- Methodology carousel: Tabs and carousel to explain the methodology and usage.
- Validation: Only allows binary images; auto-converts if necessary.
- Unit tests: Coverage for calculation logic, image loading/binarization, overlay, and results management.

### Start

1. Install dependencies:
   npm install

2. Run the app in development mode:
   npm start

3. Open http://localhost:4200 in your browser.

### Project Structure

- `src/app/components/upload-calc/`: Main component for upload, calculation, and visualization.
- `src/app/components/results-table/`: Results table and CSV export.
- `src/app/components/methodology-carousel/`: Methodology carousel.
- `src/app/services/stain.service.ts`: Calculation logic and utilities.

### Useful Scripts

- `npm start` — Start the app in development mode.
- `npm test` — Run unit tests.
