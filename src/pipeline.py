from pathlib import Path
from typing import List
from .loader import ImageLoader
from .validator import ImageValidator
from .processor import ImageProcessor, make_resize_and_save_step
from .exporter import CSVExporter

class ImagePipeline:
    """
    ImagePipeline orchestrates a full image processing workflow: loading images from a folder,
    validating their dimensions, processing (e.g., resizing) them, and exporting results to CSV.

    Attributes:
        loader (ImageLoader): Loads images from the input folder.
        validator (ImageValidator): Validates image dimensions.
        processor (ImageProcessor): Processes images with defined steps.
        exporter (CSVExporter): Exports results to a CSV file.
        max_workers (int): Maximum number of threads for parallel processing.
    """

    def __init__(self,
                 input_folder: str = "input",
                 output_folder: str = "output",
                 max_workers: int = 4,
                 resize_max: int = 1024):
        """
        Initialize the pipeline with input/output paths, processing parameters, and worker settings.

        Args:
            input_folder (str): Folder to load images from. Defaults to "input".
            output_folder (str): Folder to save processed images and CSV. Defaults to "output".
            max_workers (int): Number of parallel threads for image processing. Defaults to 4.
            resize_max (int): Maximum size for resizing images (longest edge). Defaults to 1024.
        """
        self.loader = ImageLoader(input_folder)
        self.validator = ImageValidator(min_width=2, min_height=2)
        self.processor = ImageProcessor(output_folder=output_folder, max_size=resize_max)
        self.processor.add_step(make_resize_and_save_step(output_folder=output_folder, max_size=resize_max))
        self.exporter = CSVExporter(output_folder=output_folder)
        self.max_workers = max_workers

    def run(self):
        """
        Execute the image processing pipeline:
        1. Load images from the input folder.
        2. Validate each image's dimensions.
        3. Process valid images (resizing, saving).
        4. Merge validation and processing results.
        5. Export all results to a CSV file.

        Returns:
            dict: A summary containing:
                "csv" (str): Path to the generated CSV file.
                "count_validated" (int): Total number of images validated.
                "count_processed" (int): Number of images successfully processed.
        """
        # Load all image paths
        paths = self.loader.get_image_paths()

        # Validate images and separate valid/invalid
        validated = [self.validator.validate(Path(p)) for p in paths]
        to_process = []
        results = []
        for v in validated:
            if v.get("ok"):
                to_process.append(Path(v["path"]))
            else:
                results.append(v)

        # Process valid images in parallel
        if to_process:
            processed = self.processor.run_parallel(to_process, max_workers=self.max_workers)
            for p in processed:
                src = p.get("source")
                vd = next((x for x in validated if str(x["path"]) == str(src)), {})
                merged = {}
                merged.update(vd)
                merged.update(p)
                results.append(merged)

        # Export all results to CSV
        csv_path = self.exporter.write(results)
        return {"csv": csv_path, "count_validated": len(validated), "count_processed": len(to_process)}
