import os
import logging
from typing import Optional, List, Tuple
from datetime import datetime

import pandas as pd
import pydicom
from pydicom.errors import InvalidDicomError
from PIL import Image
import numpy as np


import os
import logging
from typing import Optional, List, Tuple
from datetime import datetime

import pandas as pd
import pydicom
from pydicom.errors import InvalidDicomError
from PIL import Image
import numpy as np

class FileProcessor:
    def __init__(self, base_path: str, log_file: str = "file_processor.log"):
        self.base_path = base_path
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        handler = logging.FileHandler(log_file)
        handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(handler)

    def list_folder_contents(self, folder_name: str, details: bool = False) -> None:
        full_path = os.path.join(self.base_path, folder_name)
        if not os.path.exists(full_path):
            self.logger.error(f"Folder does not exist: {full_path}")
            print(f"Error: Folder '{folder_name}' not found.")
            return

        entries = os.listdir(full_path)
        print(f"Folder: {full_path}")
        print(f"Number of elements: {len(entries)}")

        for entry in entries:
            entry_path = os.path.join(full_path, entry)
            if os.path.isdir(entry_path):
                mod_time = datetime.fromtimestamp(os.path.getmtime(entry_path))
                print(f"Folder: - {entry} (Last Modified: {mod_time})")
            elif os.path.isfile(entry_path):
                size_mb = os.path.getsize(entry_path) / (1024 * 1024)
                mod_time = datetime.fromtimestamp(os.path.getmtime(entry_path))
                if details:
                    print(f"File: - {entry} ({size_mb:.1f} MB, Last Modified: {mod_time})")
                else:
                    print(f"File: - {entry}")

    def read_csv(self, filename: str, report_path: Optional[str] = None, summary: bool = False) -> None:
        filepath = os.path.join(self.base_path, filename)
        if not os.path.exists(filepath):
            self.logger.error(f"CSV file not found: {filepath}")
            print(f"Error: CSV file '{filename}' not found.")
            return

        try:
            df = pd.read_csv(filepath)
        except Exception as e:
            self.logger.error(f"Failed to read CSV: {e}")
            print("Error: Failed to read CSV file.")
            return

        print(f"CSV Analysis:")
        print(f"Columns: {list(df.columns)}")
        print(f"Rows: {len(df)}")

        report_lines = []

        for col in df.select_dtypes(include='number'):
            try:
                avg = df[col].mean()
                std = df[col].std()
                print(f"- {col}: Average = {avg:.2f}, Std Dev = {std:.2f}")
                report_lines.append(f"{col}: Average = {avg:.2f}, Std Dev = {std:.2f}")
            except Exception as e:
                self.logger.error(f"Error analyzing numeric column '{col}': {e}")

        if summary:
            for col in df.select_dtypes(exclude='number'):
                try:
                    unique_counts = df[col].value_counts()
                    print(f"- {col}: Unique Values = {unique_counts.shape[0]}")
                    for val, count in unique_counts.items():
                        print(f"    {val}: {count}")
                except Exception as e:
                    self.logger.error(f"Error summarizing column '{col}': {e}")

        if report_path:
            os.makedirs(report_path, exist_ok=True)
            report_file = os.path.join(report_path, f"{os.path.splitext(filename)[0]}_report.txt")
            try:
                with open(report_file, 'w') as f:
                    f.write("\n".join(report_lines))
                print(f"Saved summary report to {report_file}")
            except Exception as e:
                self.logger.error(f"Failed to save report: {e}")

    def read_dicom(self, filename: str, tags: Optional[List[Tuple[int, int]]] = None, extract_image: bool = False) -> None:
        filepath = os.path.join(self.base_path, filename)
        if not os.path.exists(filepath):
            self.logger.error(f"DICOM file not found: {filepath}")
            print(f"Error: DICOM file '{filename}' not found.")
            return

        try:
            dicom = pydicom.dcmread(filepath)
        except InvalidDicomError as e:
            self.logger.error(f"Invalid DICOM format: {e}")
            print("Error: Invalid DICOM file.")
            return

        try:
            print("DICOM Analysis:")
            print(f"Patient Name: {dicom.get('PatientName', 'N/A')}")
            print(f"Study Date: {dicom.get('StudyDate', 'N/A')}")
            print(f"Modality: {dicom.get('Modality', 'N/A')}")

            if tags:
                for group, element in tags:
                    tag_value = dicom.get((group, element), "Not Found")
                    print(f"Tag ({hex(group)}, {hex(element)}): {tag_value}")

            if extract_image:
                if hasattr(dicom, "pixel_array"):
                    image = self._process_dicom_image(dicom)
                    image_path = os.path.join(self.base_path, f"{os.path.splitext(filename)[0]}.png")
                    Image.fromarray(image).save(image_path)
                    print(f"Extracted image saved to {image_path}")
                else:
                    self.logger.error("DICOM does not contain pixel data.")
                    print("Error: DICOM does not contain image data.")
        except Exception as e:
            self.logger.error(f"Error processing DICOM file: {e}")
            print("Error: DICOM contains unsupported or corrupted image data.")

    def _process_dicom_image(self, dicom) -> np.ndarray:
        try:
            img = dicom.pixel_array.astype(np.float32)


            center = dicom.get('WindowCenter', None)
            width = dicom.get('WindowWidth', None)
            if isinstance(center, pydicom.multival.MultiValue): center = center[0]
            if isinstance(width, pydicom.multival.MultiValue): width = width[0]

            if center and width:
                img = np.clip(img, center - width / 2, center + width / 2)

            img -= img.min()
            img /= img.max()
            img *= 255
            img = img.astype(np.uint8)

            mask_rows = np.any(img > 10, axis=1)
            mask_cols = np.any(img > 10, axis=0)
            img = img[mask_rows][:, mask_cols]


            return img
        except Exception as e:
            self.logger.error(f"Error in DICOM image processing: {e}")
            raise



processor = FileProcessor(base_path="./files-for-test", log_file="processor.log")

processor.list_folder_contents(folder_name=".", details=True)

processor.read_csv(
    filename="sample-02-csv.csv",
    report_path="./reports",
    summary=True
)

processor.read_dicom(
    filename="sample-02-dicom-2.dcm",
    tags=[(0x0010, 0x0010), (0x0008, 0x0060)],
    extract_image=True
)