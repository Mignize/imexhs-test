This project implements a FileProcessor class with methods to handle file system operations, CSV data analysis, and DICOM medical imaging processing. It is designed to simplify common file tasks and includes robust error handling and logging.

### Features

1. List Folder Contents
   This method receives a folder name relative to the base_path, counts the number of elements inside, and prints them to the console. It displays the names and types (file or folder) of the items found. If details=True is passed, it also includes the file sizes in megabytes (MB) and their last modified timestamps.

2. Read CSV Files
   This functionality reads and analyzes CSV files located in the base directory. It prints the number of columns, their names, and the total number of rows. It also calculates and displays statistics such as the average and standard deviation for numeric columns. If summary=True is specified, it prints a summary of non-numeric columns, including unique values and their frequencies. Additionally, if a report_path is provided, the numeric analysis is saved as a .txt report. The method includes error handling for missing files, invalid formats, and incorrect data types.

3. Read DICOM Files
   This method reads and processes DICOM files. It extracts key metadata such as the patient's name, study date, and modality. Optionally, users can pass a list of DICOM tags to retrieve additional specific values. If extract_image=True is enabled and the file contains valid pixel data, the image is extracted and saved as a .png file in the base path. The method logs any issues such as missing files, invalid DICOM formats, or unsupported pixel data.

### Installation

Install the required dependencies using pip:

pip install pandas numpy pydicom matplotlib pillow

### Start

python index.py

### Test

The project includes a sample folder with test files to verify functionality. You can use these or replace them with your own files by modifying the base_path accordingly.
