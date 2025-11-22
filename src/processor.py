from pathlib import Path
from typing import Callable, List, Any
from PIL import Image


class ImageProcessor:
    def __init__(self, output_folder: str = "output", max_size: int = 1024):
        self.steps: List[Callable[[Path], Any]] = []
        self.output_folder = Path(output_folder)
        self.output_folder.mkdir(parents=True, exist_ok=True)
        self.max_size = max_size

    def add_step(self, func: Callable[[Path], Any]) -> None:
        self.steps.append(func)

    def _run_steps(self, path: Path):
        current = path
        results = {"source": str(path)}
        for step in self.steps:
            r = step(current)
            if isinstance(r, dict):
                results.update(r)
        return results

    def run_serial(self, image_paths: List[Path]):
        out = []
        for p in image_paths:
            out.append(self._run_steps(p))
        return out

    def run_parallel(self, image_paths: List[Path], max_workers: int = 4):
        from concurrent.futures import ThreadPoolExecutor, as_completed
        out = []
        with ThreadPoolExecutor(max_workers=max_workers) as ex:
            futures = {ex.submit(self._run_steps, p): p for p in image_paths}
            for fut in as_completed(futures):
                out.append(fut.result())
        return out


def make_resize_and_save_step(output_folder: str = "output", max_size: int = 1024):
    out_folder = Path(output_folder)
    out_folder.mkdir(parents=True, exist_ok=True)

    def step(path: Path):
        try:
            with Image.open(path) as img:
                img = img.convert("RGB")
                w, h = img.size
                if max(w, h) > max_size:
                    if w >= h:
                        new_w = max_size
                        new_h = int(h * (max_size / w))
                    else:
                        new_h = max_size
                        new_w = int(w * (max_size / h))
                    img = img.resize((new_w, new_h), Image.LANCZOS)
                # save to output folder with same stem + _processed.jpg
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
