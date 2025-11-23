from src.pipeline import ImagePipeline
import argparse

def main():
    """
    Entry point for running the Parallel Image Processing Pipeline from the command line.

    Functionality:
        - Parses command-line arguments for input/output folders, number of workers, and resize limit.
        - Instantiates the ImagePipeline with the provided parameters.
        - Executes the pipeline: loading, validating, processing images, and exporting results.
        - Prints a summary including CSV report path, number of validated images, and number processed.

    Command-line arguments:
        --input (str): Input folder containing images. Defaults to "input".
        --output (str): Output folder to save processed images and CSV. Defaults to "output".
        --workers (int): Maximum number of parallel threads for processing. Defaults to 4.
        --resize (int): Maximum size for resizing images (pixels, longest edge). Defaults to 1024.
    """
    parser = argparse.ArgumentParser(description="Parallel Image Processing Pipeline")
    parser.add_argument("--input", default="input", help="input folder")
    parser.add_argument("--output", default="output", help="output folder")
    parser.add_argument("--workers", type=int, default=4, help="max worker threads")
    parser.add_argument("--resize", type=int, default=1024, help="max size (px)")
    args = parser.parse_args()

    # Initialize the image processing pipeline with provided arguments
    p = ImagePipeline(
        input_folder=args.input,
        output_folder=args.output,
        max_workers=args.workers,
        resize_max=args.resize
    )

    # Run the pipeline
    res = p.run()

    # Print results summary
    print("Done.")
    print(f"CSV report: {res['csv']}")
    print(f"Validated: {res['count_validated']}, Processed: {res['count_processed']}")

if __name__ == "__main__":
    main()
