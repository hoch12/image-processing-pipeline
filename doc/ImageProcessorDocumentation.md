# Parallel Image Processing Pipeline – Full Project Documentation   

**Author:** Dominik Hoch    
**Mail:** [domik.hoch@gmail.com](mailto:domik.hoch@gmail.com)   
**LinkedIn:** www.linkedin.com/in/dominik-hoch-144143343    
**School:** SPŠE Ječná  
**Date:** 2025  
**Project Type:** School Project    

---

## 1. Project Overview  

The **Parallel Image Processing Pipeline** is a school project designed to process images efficiently in parallel. The program loads images from an input folder, validates them, processes them (e.g., resizing), and exports results to an output folder including a CSV report.  

The primary goal of this project is to demonstrate: 

* Parallel and concurrent processing of images  
* Image validation and manipulation
* Automated reporting of processing results

---

## 2. Functional Requirements

**User can:**

* Provide an input folder containing images (`input/`)
* Configure output folder for processed images and CSV report (`output/`)
* Specify maximum number of concurrent threads
* Resize images to a maximum width/height in pixels

**Application will:**

* Validate all input images (check if proper image and minimum size)
* Process images in parallel (resize and save)
* Generate a CSV report summarizing processing results

---

## 3. Non-Functional Requirements

* Platform independent (tested on macOS, Python 3.11)
* Uses Python standard libraries and `Pillow` for image processing
* Thread-based parallelism using `concurrent.futures.ThreadPoolExecutor`
* Output is deterministic (CSV and image files are consistently named)

---

## 4. Project Structure

```
image-processing-pipeline/
│
├── docs/                ← Project documentation
├── src/                 ← Source code modules
│   ├── loader.py        ← ImageLoader class
│   ├── validator.py     ← ImageValidator class
│   ├── processor.py     ← ImageProcessor class and processing steps
│   ├── exporter.py      ← CSVExporter class
│   └── pipeline.py      ← ImagePipeline orchestration
│   └── main.py          
├── tests/               ← Unit tests for all modules
│   ├── test_loader.py
│   ├── test_validator.py
│   ├── test_processor.py
│   └── test_exporter.py
├── input/               ← Input images folder
├── output/              ← Output images and CSV reports
├── .venv/               ← Python virtual environment
├── requirements.txt     ← Python dependencies
└── README.md            ← Usage instructions
```

---

## 5. Architecture Overview

### 5.1 Big Picture

* **Loader:** Reads all image file paths from the input folder.
* **Validator:** Checks each image for validity and minimum size.
* **Processor:** Applies image processing steps (resize, save). Supports serial or parallel execution.
* **Exporter:** Writes processing results into a CSV file.
* **Pipeline:** Coordinates loader, validator, processor, and exporter.

### 5.2 Component Interactions

```
[User Input Folder] --> ImageLoader --> ImageValidator --> ImageProcessor --> CSVExporter --> [Output Folder + CSV]
```

* Each component communicates via Python objects (`Path` and `dict`).
* `ImageProcessor` supports **parallel processing** via threads.

---

## 6. Installation and Setup

1. Clone the project:

```bash
git clone https://github.com/hoch12/image-processing-pipeline.git
cd image-processing-pipeline
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # macOS / Linux
.venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 7. Running the Application

```bash
python -m src.main --input input --output output --workers 4 --resize 1024
```

**Arguments:**

* `--input`: Input folder with images
* `--output`: Output folder for processed images and CSV report
* `--workers`: Number of concurrent threads
* `--resize`: Maximum width/height in pixels

**Output:**

* Processed images in `output/`
* CSV report (`report.csv`) summarizing each image (path, size, processing info)

---

## 8. Error Handling

* Invalid images (corrupt or non-image) are marked in CSV with `ok: False` and error message.
* File system errors (cannot save) are captured and included in CSV `error` field.
* Exceptions in parallel processing do not crash the program; they are logged per image.

---

## 9. Testing and Validation

Unit tests exist for all major modules:

| Module       | Test Class      | Checks                                                   |
| ------------ | --------------- | -------------------------------------------------------- |
| `loader.py`    | `test_loader.py`    | Ensures only image files are loaded                      |
| `validator.py` | `test_validator.py` | Checks valid and invalid images                          |
| `processor.py` | `test_processor.py` | Ensures images are resized and saved (serial & parallel) |
| `exporter.py`  | `test_exporter.py`  | Ensures CSV is written with correct content              |

**Run all tests:**

```bash
python -m unittest discover -s test
```

---

## 10. Configuration

* All configurable options (input/output folders, threads, resize size) are **command-line arguments**.
* Defaults: `input/`, `output/`, 4 threads, resize max 1024 px.

---

## 11. Third-Party Libraries

* `Pillow` – image reading and manipulation
* `pytest` – optional, for additional testing
* Standard libraries: `pathlib`, `csv`, `typing`, `concurrent.futures`

No database or network services are required.

---

## 12. License

This project is licensed under the **MIT License**. You can freely use, modify, and distribute it with attribution.

---

## 13. Import/Export

* **Input:** Images in standard formats (`.png`, `.jpg`, `.jpeg`, `.bmp`, `.gif`, `.tiff`)
* **Output:**

  * Processed images (resized) as JPEGs
  * CSV report containing image metadata and processing status

**CSV Columns:** Determined dynamically from processed image data. Missing keys are filled with empty strings.

---

## 14. Known Limitations

* No support for non-image files (they are skipped and logged).
* Performance depends on CPU cores; thread-based parallelism may be limited by GIL in Python.
* CSV uses UTF-8; extremely large datasets may require streaming modifications.

---

## 15. Future Enhancements

* Add database support for storing processing results.
* Support image filters or transformations beyond resizing.
* Add GUI for easier usage.

---

## 16. References

* Python 3.11 Documentation
* Pillow Documentation: [https://pillow.readthedocs.io/](https://pillow.readthedocs.io/)
* Python `csv` module: [https://docs.python.org/3/library/csv.html](https://docs.python.org/3/library/csv.html)
* Concurrent Futures: [https://docs.python.org/3/library/concurrent.futures.html](https://docs.python.org/3/library/concurrent.futures.html)
