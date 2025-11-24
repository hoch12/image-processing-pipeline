from pathlib import Path
from typing import List

class ImageLoader:
    """
    ImageLoader is responsible for scanning a folder and collecting paths of all supported image files.

    ```
    Attributes:
        folder_path (Path): Path object pointing to the folder containing images.
    """

    def __init__(self, folder_path: str = "input"):
        """
        Initialize the ImageLoader with the folder to scan.

        Args:
            folder_path (str): Path to the folder containing images. Defaults to "input".
        """
        self.folder_path = Path(folder_path)


    def get_image_paths(self) -> List[Path]:
        """
        Retrieve a sorted list of paths to all image files in the folder matching supported extensions.

        Supported extensions include: .png, .jpg, .jpeg, .bmp, .gif, .tiff.

        Returns:
            List[Path]: A sorted list of Path objects pointing to image files.
        """
        exts = ("*.png", "*.jpg", "*.jpeg", "*.bmp", "*.gif", "*.tiff")
        paths = []
        for ext in exts:
            # Use glob to find all files matching the extension pattern in folder_path
            paths.extend(self.folder_path.glob(ext))
        # Remove duplicates and sort the list
        paths = sorted(set(paths))
        return paths
