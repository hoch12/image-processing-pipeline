from pathlib import Path
from typing import List


class ImageLoader:
    def __init__(self, folder_path: str = "input"):
        self.folder_path = Path(folder_path)

    def get_image_paths(self) -> List[Path]:
        exts = ("*.png", "*.jpg", "*.jpeg", "*.bmp", "*.gif", "*.tiff")
        paths = []
        for ext in exts:
            paths.extend(self.folder_path.glob(ext))
        paths = sorted(set(paths))
        return paths
