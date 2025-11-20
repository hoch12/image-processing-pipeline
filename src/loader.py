from pathlib import Path
from typing import List


class ImageLoader:
    def __init__(self, folder_path: str = "input"):
        self.folder_path = Path(folder_path)
        if not self.folder_path.exists():
            raise FileNotFoundError(f"Složka {folder_path} neexistuje.")

    def get_image_paths(self) -> List[Path]:
        image_files = list(self.folder_path.glob("*.png")) + \
                      list(self.folder_path.glob("*.jpg"))
        return image_files
