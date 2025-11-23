from pathlib import Path
from typing import Dict, Any
from PIL import Image, UnidentifiedImageError

class ImageValidator:
    """
    ImageValidator is responsible for checking if an image meets the minimum size requirements 
    and whether it is a valid image file.

    Attributes:
        min_width (int): Minimum allowed width of an image.
        min_height (int): Minimum allowed height of an image.
    """

    def __init__(self, min_width: int = 2, min_height: int = 2):
        """
        Initialize the ImageValidator with minimum width and height.

        Args:
            min_width (int): Minimum width of the image. Defaults to 2.
            min_height (int): Minimum height of the image. Defaults to 2.
        """
        self.min_width = min_width
        self.min_height = min_height

    def validate(self, path: Path) -> Dict[str, Any]:
        """
        Validate an image file at the given path.

        Checks if the file is a valid image, verifies its size, and returns relevant information.

        Args:
            path (Path): Path to the image file to validate.

        Returns:
            Dict[str, Any]: Dictionary containing:
                - "path": The string path of the image.
                - "ok": True if valid and meets size requirements, False otherwise.
                - "error": Error message if invalid or too small, None otherwise.
                - "width": Width of the image if valid.
                - "height": Height of the image if valid.
                - "format": Image format if valid.
        """
        result = {
            "path": str(path),
            "ok": False,
            "error": None,
            "width": None,
            "height": None,
            "format": None,
        }
        try:
            # Open image to verify it is not corrupted
            with Image.open(path) as img:
                img.verify()
            # Open again to get size and format
            with Image.open(path) as img:
                width, height = img.size
                fmt = img.format
            # Check if image meets minimum size
            if width < self.min_width or height < self.min_height:
                result["error"] = f"Too small ({width}x{height})"
            else:
                result["ok"] = True
                result["width"] = width
                result["height"] = height
                result["format"] = fmt
        except UnidentifiedImageError:
            result["error"] = "Unidentified image / not an image"
        except Exception as e:
            result["error"] = f"Exception: {e}"
        return result
