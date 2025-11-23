import unittest
from src.validator import ImageValidator
from pathlib import Path

# --- Run with: 'python -m unittest test.test_validator' ---

class TestValidator(unittest.TestCase):
    """
    Unit test suite for the ImageValidator class.

    This test class verifies two core behaviors:
    1) A valid, readable image file is correctly recognized as valid.
    2) A corrupted or non-image file is correctly recognized as invalid.
    """

    def setUp(self):
        """
        Prepare the test environment before each test.

        Attributes:
            valid_image (Path): Path to an existing valid image file.
            invalid_image (Path): Path to a corrupted or non-image file.
            validator (ImageValidator): Instance of validator used in tests.
        """
        self.valid_image = Path("input/Lion.jpg")
        self.invalid_image = Path("input/bad_photo.jpg")
        self.validator = ImageValidator()

    def test_valid_image(self):
        """
        Ensure that a correct image file is validated as OK.

        Expected:
            - validate() returns a result dictionary
            - result['ok'] is True for a valid image
        """
        result = self.validator.validate(self.valid_image)
        self.assertTrue(result['ok'])

    def test_invalid_image(self):
        """
        Ensure that an invalid or corrupted file is marked as not valid.

        Expected:
            - validate() returns a result dictionary
            - result['ok'] is False for an invalid/corrupted image
        """
        result = self.validator.validate(self.invalid_image)
        self.assertFalse(result['ok'])

if __name__ == "__main__":
    unittest.main()
