from src.pipeline import ImagePipeline
import argparse

def main():
    parser = argparse.ArgumentParser(description="Parallel Image Processing Pipeline")
    parser.add_argument("--input", default="input", help="input folder")
    parser.add_argument("--output", default="output", help="output folder")
    parser.add_argument("--workers", type=int, default=4, help="max worker threads")
    parser.add_argument("--resize", type=int, default=1024, help="max size (px)")
    args = parser.parse_args()

    p = ImagePipeline(input_folder=args.input, output_folder=args.output,
                      max_workers=args.workers, resize_max=args.resize)
    res = p.run()
    print("Done.")
    print(f"CSV report: {res['csv']}")
    print(f"Validated: {res['count_validated']}, Processed: {res['count_processed']}")

if __name__ == "__main__":
    main()
