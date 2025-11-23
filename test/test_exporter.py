import unittest
from pathlib import Path
from src.exporter import CSVExporter

# --- Run with: 'python -m unittest test.test_exporter' ---

class TestExporter(unittest.TestCase):
    """
    Unit tests for CSVExporter.

    This class tests that CSVExporter correctly writes dictionaries to a CSV file
    and that the resulting file contains expected headers and content.
    """

    def setUp(self):
        """
        Set up the exporter instance and example data for testing.
        """
        self.output_folder = Path("output")
        self.exporter = CSVExporter(output_folder=str(self.output_folder), filename="test_report.csv")
        self.rows = [{"name": "Lion", "size": 1024}, {"name": "Tiger", "size": 2048}]

    def test_write(self):
        """
        Test that the write method creates a CSV file and includes expected content.

        Checks:
        - The CSV file exists after writing.
        - The header "name" is present in the file.
        - The value "Lion" from the test data is present in the file.
        """
        csv_path = self.exporter.write(self.rows)
        self.assertTrue(Path(csv_path).exists())
        content = Path(csv_path).read_text()
        self.assertIn("name", content)
        self.assertIn("Lion", content)

if __name__ == "__main__":
    unittest.main()

