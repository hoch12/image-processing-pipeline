import unittest
from src.loader import ImageLoader

# --- Run with: 'python -m unittest test.test_loader' ---

class TestLoader(unittest.TestCase):
    """
    Unit tests for ImageLoader.

    This class tests that ImageLoader correctly loads only files with
    supported image extensions from a given folder.
    """

    def test_loader_loads_only_images(self):
        """
        Test that get_image_paths returns only files with valid image extensions.

        Supported extensions: .png, .jpg, .jpeg, .bmp, .gif, .tiff
        """
        loader = ImageLoader("input")
        images = loader.get_image_paths()
        for img in images:
            self.assertTrue(img.suffix.lower() in (".png", ".jpg", ".jpeg", ".bmp", ".gif", ".tiff"))

if __name__ == "__main__":
    unittest.main()

