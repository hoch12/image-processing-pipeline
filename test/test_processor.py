import unittest
from pathlib import Path
from PIL import Image
from src.processor import ImageProcessor, make_resize_and_save_step

# --- Run with: 'python -m unittest test.test_processor' ---

class TestProcessor(unittest.TestCase):
    """
    Unit tests for ImageProcessor.

    This class tests that ImageProcessor correctly processes images
    both in serial and parallel execution modes, and that processed
    images are saved to the output folder.
    """

    def setUp(self):
        """
        Prepare a test image, output folder, and processor instance.
        """
        self.img_path = Path("input/Lion.jpg")  # Existing test image
        self.out_folder = Path("output")
        self.processor = ImageProcessor(output_folder=str(self.out_folder), max_size=500)
        self.processor.add_step(make_resize_and_save_step(output_folder=str(self.out_folder), max_size=500))

    def test_run_serial(self):
        """
        Test processing a single image in serial mode.
        Verifies that the output path exists and contains 'processed_path'.
        """
        results = self.processor.run_serial([self.img_path])
        self.assertTrue("processed_path" in results[0])
        processed_path = Path(results[0]["processed_path"])
        self.assertTrue(processed_path.exists())

    def test_run_parallel(self):
        """
        Test processing a single image in parallel mode.
        Verifies that the output path exists and contains 'processed_path'.
        """
        results = self.processor.run_parallel([self.img_path], max_workers=2)
        self.assertTrue("processed_path" in results[0])
        processed_path = Path(results[0]["processed_path"])
        self.assertTrue(processed_path.exists())

if __name__ == "__main__":
    unittest.main()

