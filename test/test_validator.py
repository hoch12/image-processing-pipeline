import unittest
from src.validator import ImageValidator
from pathlib import Path

class TestValidator(unittest.TestCase):
    def setUp(self):
        self.valid_image = Path("input/Lion.jpg")      # dej tam existující obrázek
        self.invalid_image = Path("input/bad_photo.jpg")  # dej tam soubor, který není obrázek nebo je poškozený
        self.validator = ImageValidator()

    def test_valid_image(self):
        result = self.validator.validate(self.valid_image)
        self.assertTrue(result['ok'])  # kontrola, že obrázek je validní

    def test_invalid_image(self):
        result = self.validator.validate(self.invalid_image)
        self.assertFalse(result['ok'])  # kontrola, že obrázek je nevalidní

if __name__ == "__main__":
    unittest.main()
