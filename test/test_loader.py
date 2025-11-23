import unittest
from src.loader import ImageLoader

class TestLoader(unittest.TestCase):
    def test_loader_loads_only_images(self):
        loader = ImageLoader("input")
        images = loader.get_image_paths()
        # všechny soubory mají správnou příponu
        for img in images:
            self.assertTrue(img.suffix.lower() in (".png", ".jpg", ".jpeg", ".bmp", ".gif", ".tiff"))

if __name__ == "__main__":
    unittest.main()
