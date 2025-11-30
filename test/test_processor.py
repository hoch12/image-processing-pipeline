import unittest
from pathlib import Path
from PIL import Image
from src.processor import ImageProcessor, make_resize_and_save_step

class TestProcessor(unittest.TestCase):
    """
    Unit tests for ImageProcessor with percentage-based resizing using 'scale'.
    """

    def setUp(self):
        """
        Prepare a test image, output folder, and processor instance.
        """
        self.img_path = Path("input/Lion.jpg")  # Make sure this test image exists
        self.out_folder = Path("output")

        # Initialize ImageProcessor (no max_size, scale-based resizing)
        self.processor = ImageProcessor(output_folder=str(self.out_folder))
        # Add resize step with 50% scale
        self.processor.add_step(make_resize_and_save_step(output_folder=str(self.out_folder), scale=0.5))

    def test_run_serial(self):
        """
        Test processing a single image in serial mode.
        """
        results = self.processor.run_serial([self.img_path])
        self.assertIn("processed_path", results[0])
        processed_path = Path(results[0]["processed_path"])
        self.assertTrue(processed_path.exists())

    def test_run_parallel(self):
        """
        Test processing a single image in parallel mode.
        """
        results = self.processor.run_parallel([self.img_path], max_workers=2)
        self.assertIn("processed_path", results[0])
        processed_path = Path(results[0]["processed_path"])
        self.assertTrue(processed_path.exists())

if __name__ == "__main__":
    unittest.main()
