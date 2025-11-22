from pathlib import Path
from typing import Dict, Any
from PIL import Image, UnidentifiedImageError


class ImageValidator:
    def __init__(self, min_width: int = 2, min_height: int = 2):
        self.min_width = min_width
        self.min_height = min_height

    def validate(self, path: Path) -> Dict[str, Any]:

        result = {
            "path": str(path),
            "ok": False,
            "error": None,
            "width": None,
            "height": None,
            "format": None,
        }
        try:
            with Image.open(path) as img:
                img.verify()
            with Image.open(path) as img:
                width, height = img.size
                fmt = img.format
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
