from pathlib import Path
from typing import Callable, List, Any
from PIL import Image


class ImageProcessor:
    """
    A class to process images through a configurable pipeline of processing steps.

    Attributes:
        steps (List[Callable[[Path], Any]]): A list of functions that define processing steps.
        output_folder (Path): The folder where processed images will be saved.
        max_size (int): Maximum width or height for processed images.
    """

    def __init__(self, output_folder: str = "output", max_size: int = 1024):
        """
        Initializes the ImageProcessor.

        Args:
            output_folder (str): Folder where processed images will be stored. Default is "output".
            max_size (int): Maximum width or height for processed images. Default is 1024.
        """
        self.steps: List[Callable[[Path], Any]] = []  # store processing steps
        self.output_folder = Path(output_folder)
        self.output_folder.mkdir(parents=True, exist_ok=True)  # ensure folder exists
        self.max_size = max_size

    def add_step(self, func: Callable[[Path], Any]) -> None:
        """
        Adds a processing step to the pipeline.

        Args:
            func (Callable[[Path], Any]): A function that takes a Path to an image and returns a dictionary with processing info.
        """
        self.steps.append(func)

    def _run_steps(self, path: Path):
        """
        Executes all processing steps on a single image.

        Args:
            path (Path): Path to the image to be processed.

        Returns:
            dict: Aggregated results from all steps, including source path and any processing info.
        """
        current = path
        results = {"source": str(path)}
        for step in self.steps:
            r = step(current)
            if isinstance(r, dict):  # merge returned dict from step
                results.update(r)
        return results

    def run_serial(self, image_paths: List[Path]):
        """
        Processes images sequentially (one after another).

        Args:
            image_paths (List[Path]): List of image file paths to process.

        Returns:
            List[dict]: List of results for each processed image.
        """
        out = []
        for p in image_paths:
            out.append(self._run_steps(p))
        return out

    def run_parallel(self, image_paths: List[Path], max_workers: int = 4):
        """
        Processes images in parallel using threads.

        Args:
            image_paths (List[Path]): List of image file paths to process.
            max_workers (int): Number of worker threads to use for parallel processing. Default is 4.

        Returns:
            List[dict]: List of results for each processed image.
        """
        from concurrent.futures import ThreadPoolExecutor, as_completed

        out = []
        # Create a thread pool to process images concurrently
        with ThreadPoolExecutor(max_workers=max_workers) as ex:
            # Submit each image path to the thread pool; returns a Future object
            futures = {ex.submit(self._run_steps, p): p for p in image_paths}
            # As each future completes, append the result to output list
            for fut in as_completed(futures):
                out.append(fut.result())
        return out


def make_resize_and_save_step(output_folder: str = "output", max_size: int = 1024):
    """
    Factory function to create a resize-and-save processing step.

    Args:
        output_folder (str): Folder where processed images will be saved.
        max_size (int): Maximum width or height for the resized images.

    Returns:
        Callable[[Path], dict]: A function that resizes an image and saves it to the output folder.
    """
    out_folder = Path(output_folder)
    out_folder.mkdir(parents=True, exist_ok=True)  # ensure output folder exists

    def step(path: Path):
        """
        Resize the image if larger than max_size and save it as JPEG.

        Args:
            path (Path): Path to the input image.

        Returns:
            dict: Information about the processed image, or an error message.
        """
        try:
            with Image.open(path) as img:
                img = img.convert("RGB")  # ensure image is RGB
                w, h = img.size
                if max(w, h) > max_size:
                    # Compute new size preserving aspect ratio
                    if w >= h:
                        new_w = max_size
                        new_h = int(h * (max_size / w))
                    else:
                        new_h = max_size
                        new_w = int(w * (max_size / h))
                    img = img.resize((new_w, new_h), Image.LANCZOS)
                # Save resized image to output folder
                out_path = out_folder / f"{path.stem}_processed.jpg"
                img.save(out_path, format="JPEG", quality=85)
                return {
                    "processed_path": str(out_path),
                    "processed_width": img.size[0],
                    "processed_height": img.size[1],
                }
        except Exception as e:
            return {"error": str(e)}

    return step
