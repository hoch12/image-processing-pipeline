from src.pipeline import ImagePipeline
import argparse

def main():
    """
    Entry point for running the Parallel Image Processing Pipeline from the command line.

    Functionality:
        - Parses command-line arguments for input/output folders, number of workers, and resize scale.
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

    # Initialize the image processing pipeline with provided arguments
    pipeline = ImagePipeline(
        input_folder=args.input,
        output_folder=args.output,
        max_workers=args.workers,
        scale=args.scale
    )

    # Run the pipeline (load, validate, process, export)
    results = pipeline.run()

    # Print results summary
    print("Done.")
    print(f"CSV report: {results['csv']}")
    print(f"Validated: {results['count_validated']}, Processed: {results['count_processed']}")

# Only run main if this script is executed directly
if __name__ == "__main__":
    main()
