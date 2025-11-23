# Parallel Image Processing Pipeline    

**Author:** Dominik Hoch    
**School:** SPŠE Ječná  
**Mail:** [domik.hoch@gmail.com](mailto:domik.hoch@gmail.com)   
**LinkedIn:** [www.linkedin.com/in/dominik-hoch-144143343](http://www.linkedin.com/in/dominik-hoch-144143343)   
**Year:** 2025  

This project is a school application demonstrating a parallel image-processing pipeline.
It loads images from the `input/` folder, validates them, processes them (e.g., resizing), and exports results into a CSV report.

---

## Project Features

* Load and scan images from an input directory
* Validate file format, size, and integrity
* Process images using custom processing steps
* Resize and save processed images
* Parallel execution using worker threads
* Export results to CSV with full metadata
* Structured OOP architecture (`loader`, `validator`, `processor`, `pipeline`)
* Full unit test coverage

---

## Project Structure

```
image-processing-pipeline/
│
├── docs/                <- Documentation
├── src/                 <- Source code modules
│   ├── loader.py
│   ├── validator.py
│   ├── processor.py
│   ├── exporter.py
│   ├── pipeline.py
│   └── main.py
├── tests/               <- Unit tests
│   ├── test_loader.py
│   ├── test_validator.py
│   ├── test_processor.py
│   ├── test_exporter.py
├── input/               <- Input images
├── output/              <- Processed images + CSV reports
└── README.md
```

---

## How the Pipeline Works

1. **ImageLoader** – scans the input folder and returns valid image file paths
2. **ImageValidator** – checks resolution, validity, and extracts metadata
3. **ImageProcessor** – applies processing tasks (resize, save, custom steps), supports serial and parallel execution
4. **CSVExporter** – writes validation and processing results into a CSV
5. **ImagePipeline** – coordinates all components and returns summary statistics

---

## Installation

1. Clone the project:

```bash
git clone https://github.com/hoch12/image-processing-pipeline.git
cd image-processing-pipeline
```

2. Create a virtual environment and activate it:

```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows
```

3. Install required packages:

```bash
pip install -r requirements.txt
```

Main dependencies: `Pillow` and standard Python libraries.

---

## Running the Pipeline

```bash
python -m src.main --input input --output output --workers 4 --resize 800
```

**Arguments:**

| Argument    | Description                                |
| ----------- | ------------------------------------------ |
| `--input`   | Folder containing input images             |
| `--output`  | Folder for processed images and CSV report |
| `--workers` | Number of threads for parallel processing  |
| `--resize`  | Maximum output size in pixels              |

**Example:**

```bash
python -m src.main --input input_pics --output output_pics --workers 6 --resize 1024
```

---

## Running Unit Tests

* Verify functionality of loader, validator, processor, and exporter

**Run all tests:**

```bash
python -m unittest discover -s tests
```

**Run a single test:**

```bash
python -m unittest test.test_loader
python -m unittest test.test_validator
python -m unittest test.test_processor
python -m unittest test.test_exporter
```

---

## Output

After running the pipeline, the `output/` folder contains:

* Processed/resized images
* `report.csv` containing: validation results, size, format, processed file paths

---

## Notes

* Proper OOP structure is maintained
* Modules include programmer documentation (docstrings)
* Parallel processing uses `ThreadPoolExecutor` for efficiency
* Unit tests cover key functionalities
