from pathlib import Path
from typing import Callable, List, Any
from PIL import Image

class ImageProcessor:
    """
    Processes images through a configurable pipeline of steps.

    Attributes:
        steps (List[Callable[[Path], Any]]): Functions defining processing steps.
        output_folder (Path): Folder to save processed images.
    """

    def __init__(self, output_folder: str = "output"):
        """
        Initialize the processor.

        Args:
            output_folder (str): Folder where processed images will be stored.
        """
        self.steps: List[Callable[[Path], Any]] = []
        self.output_folder = Path(output_folder)
        self.output_folder.mkdir(parents=True, exist_ok=True)

    def add_step(self, func: Callable[[Path], Any]):
        """
        Add a processing step to the pipeline.

        Args:
            func (Callable[[Path], Any]): Function taking a Path and returning dict info.
        """
        self.steps.append(func)

    def _run_steps(self, path: Path):
        """
        Run all steps on a single image.

        Args:
            path (Path): Path to the image.

        Returns:
            dict: Aggregated results including source path and processing info.
        """
        results = {"source": str(path)}
        for step in self.steps:
            r = step(path)
            if isinstance(r, dict):
                results.update(r)
        return results

    def run_serial(self, image_paths: List[Path]):
        """
        Process images one by one.

        Args:
            image_paths (List[Path]): List of image paths.

        Returns:
            List[dict]: Results for each image.
        """
        return [self._run_steps(p) for p in image_paths]

    def run_parallel(self, image_paths: List[Path], max_workers: int = 4):
        """
        Process images concurrently using threads.

        Args:
            image_paths (List[Path]): List of image paths.
            max_workers (int): Number of threads.

        Returns:
            List[dict]: Results for each image.
        """
        from concurrent.futures import ThreadPoolExecutor, as_completed

        out = []
        with ThreadPoolExecutor(max_workers=max_workers) as ex:
            futures = {}
            for p in image_paths:
                fut = ex.submit(self._run_steps, p)
                futures[fut] = p  # store the original image path 'p' associated with its running Future 'fut'

            for fut in as_completed(futures):
                result = fut.result()
                out.append(result)

        return out


def make_resize_and_save_step(output_folder: str = "output", scale: float = 1.0):
    """
    Create a processing step that resizes images by a given percentage and saves them.

    Args:
        output_folder (str): Folder to save processed images.
        scale (float): Resize factor (0.5 = 50%).

    Returns:
        Callable[[Path], dict]: Function that resizes and saves an image.
    """
    out_folder = Path(output_folder)
    out_folder.mkdir(parents=True, exist_ok=True)

    def step(path: Path):
        """
        Resize the image by scale and save as JPEG.

        Args:
            path (Path): Input image path.

        Returns:
            dict: Info about the processed image or error message.
        """
        try:
            with Image.open(path) as img:
                img = img.convert("RGB")
                w, h = img.size
                new_w = max(1, int(w * scale))
                new_h = max(1, int(h * scale))
                img = img.resize((new_w, new_h), Image.LANCZOS) # using LANCZOS for high-quality image resampling
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
