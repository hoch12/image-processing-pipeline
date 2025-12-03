"""
Main entry point for the Parallel Image Processing Pipeline.

This script parses command-line arguments, validates input parameters,
and initiates the processing pipeline. It handles high-level error reporting
and prints the execution summary to the console.

Author: Dominik Hoch
Date: 2025
"""

from src.pipeline import ImagePipeline
import argparse
import sys
from pathlib import Path


def validate_args(args):
    """
    Validates command line arguments to prevent runtime errors and ensure
    data integrity before processing starts.

    Checks:
    1. If the input directory exists and is a directory.
    2. If the number of workers is a positive integer.
    3. If the scale factor is a positive float.

    Args:
        args (Namespace): Parsed command-line arguments.

    Raises:
        SystemExit: If any validation check fails, the program exits with status code 1.
    """
    # 1. Validate Input Directory
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"[ERROR] Input directory '{args.input}' does not exist.")
        sys.exit(1)
    if not input_path.is_dir():
        print(f"[ERROR] The path '{args.input}' is not a directory.")
        sys.exit(1)

    # 2. Validate Worker Count
    if args.workers < 1:
        print(f"[ERROR] Number of workers must be at least 1. Received: {args.workers}")
        sys.exit(1)

    # 3. Validate Scale Factor
    if args.scale <= 0:
        print(f"[ERROR] Scale factor must be greater than 0. Received: {args.scale}")
        sys.exit(1)


def main():
    """
    Entry point for running the Parallel Image Processing Pipeline from the command line.

    Functionality:
        - Parses command-line arguments for input/output folders, number of workers, and resize scale.
        - Validates the provided arguments to prevent invalid execution states.
        - Instantiates the ImagePipeline with the provided parameters.
        - Executes the pipeline: loading, validating, processing images, and exporting results.
        - Prints a summary including CSV report path, number of validated images, and number processed.

    Command-line arguments:
        --input (str): Input folder containing images. Defaults to "input".
        --output (str): Output folder to save processed images and CSV. Defaults to "output".
        --workers (int): Maximum number of parallel threads for processing. Defaults to 4.
        --scale (float): Resize scale (0.5 = 50%). Defaults to 1.0 (no resize).
    """
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Parallel Image Processing Pipeline")
    parser.add_argument("--input", default="input", help="Input folder containing images")
    parser.add_argument("--output", default="output", help="Output folder to save processed images and CSV")
    parser.add_argument("--workers", type=int, default=4, help="Maximum number of parallel threads for processing")
    parser.add_argument("--scale", type=float, default=1.0, help="Resize scale factor (0.5 = 50%)")
    args = parser.parse_args()

    # --- VALIDATION STEP ---
    validate_args(args)
    # -----------------------

    print("[INFO] Starting image processing pipeline...")
    print(f"[INFO] Input Directory: {args.input}")
    print(f"[INFO] Threads: {args.workers} | Scale: {args.scale}")

    # Initialize the image processing pipeline with provided arguments
    pipeline = ImagePipeline(
        input_folder=args.input,
        output_folder=args.output,
        max_workers=args.workers,
        scale=args.scale
    )

    # Run the pipeline (load, validate, process, export)
    try:
        results = pipeline.run()

        # Print results summary
        print("\n[SUCCESS] Processing complete.")
        print(f"Report location:  {results['csv']}")
        print(f"Images validated: {results['count_validated']}")
        print(f"Images processed: {results['count_processed']}")

    except Exception as e:
        print(f"\n[CRITICAL ERROR] An unexpected error occurred: {e}")
        sys.exit(1)


# Only run main if this script is executed directly
if __name__ == "__main__":
    main()