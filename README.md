# Parallel Image Processing Pipeline    
**Author:** Dominik Hoch        
**School:** SPŠE Ječná      
**Mail:** [domik.hoch@gmail.com](mailto:domik.hoch@gmail.com)    
**LinkedIn:** www.linkedin.com/in/dominik-hoch-144143343    
**Year:** 2025  
This project is a school application demonstrating a fully implemented parallel image-processing pipeline.  
It loads images from the `input/` folder, validates them, processes them using a configurable pipeline with     
optional resizing, and exports the final results into a CSV report. 

The main goal of the project is to demonstrate understanding of:    

- Working with files and large data batches   
- Parallel and concurrent processing using worker threads 
- Modular OOP architecture    
- Unit testing and code documentation 
- Real-world image processing with the Pillow (PIL) library   

## Project Features    
✔ Loads and scans images from an input directory    
✔ Validates file format, size, and integrity    
✔ Processes images using custom processing steps    
✔ Supports resizing and saving processed images 
✔ Parallel execution using worker threads   
✔ CSV export with full metadata 
✔ Structured OOP architecture (`loader`, `validator`, `processor`, `pipeline`)  
✔ Full set of unit tests    

## Project Structure  

```
image-processing-pipeline/  
│   
├── docs/                    <- Documentation    
├── src/                     <- Source code (modules & pipeline)     
│   ├── loader.py   
│   ├── validator.py    
│   ├── processor.py    
│   ├── exporter.py     
│   ├── pipeline.py     
│   └── main.py     
│   
├── tests/                   <- Unit tests  
│   ├── test_loader.py   
│   ├── test_validator.py    
│   ├── test_processor.py    
│   ├── test_exporter.py     
│   
├── input/                   <- Input images     
├── output/                  <- Processed images + CSV reports   
│   
└── README.md   
```

## How the Pipeline Works  
1. ImageLoader     
- Scans the input folder  
- Returns a list of valid file paths with supported extensions    
2. ImageValidator  
- Checks resolution   
- Checks whether the file is a valid image    
- Extracts metadata (width, height, format)   
3. ImageProcessor  
- Executes processing tasks (resizing, saving, custom steps)      
- Supports serial and parallel mode   
4. CSVExporter     
- Writes validation + processing results into a CSV file  
5. ImagePipeline
- Coordinates all components  
- Runs the pipeline end to end    
- Returns summary statistics  

## Installation    
1. Clone/download the project from GitHub  
2. Install required packages:  
`pip install -r requirements.txt`     
   - The main dependencies are:  
     - `Pillow`  
     - standard libraries (`pathlib`, `concurrent.futures`, `csv`, etc.)     


## Running the Pipeline    
Run the program manually:   
    `python -m src.main --input input --output output --workers 4 --resize 800`   
### Argument Description    
| Argument    | Meaning                                                |
| ----------- | ------------------------------------------------------ |
| `--input`   | Folder containing input images                         |
| `--output`  | Folder where processed images and CSV report are saved |
| `--workers` | Number of worker threads used for parallel processing  |
| `--resize`  | Maximum output size in pixels                          |
  
### Example:    
`python -m src.main --input input_pics --output output_pics --workers 6 --resize 1024` 

## Running Unit Tests  
The tests verify:   
Loader → loads only image files     
- Validator → identifies valid & invalid images   
- Processor → creates processed output files  
- Exporter → generates a CSV with correct content     
### Run all tests at once:  
`python -m unittest discover test`    
### Run a single test:  
`python -m unittest test.test_loader`     
`python -m unittest test.test_validator`  
`python -m unittest test.test_processor`  
`python -m unittest test.test_exporter`   
## Output  
After running the program, the `output/` folder contains:     
- Processed and resized images    
- report.csv containing:  
  - validation result   
  - size, format    
  - processed file path    

## Notes   
- The code follows proper OOP architecture    
- Every module is documented with programmer documentation (docstrings)   
- Unit tests provide coverage for key functions   
- Parallel processing is implemented using ThreadPoolExecutor 