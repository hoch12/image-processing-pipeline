from pathlib import Path
import csv
from typing import Iterable, Dict, Any

class CSVExporter:
    """
    CSVExporter is responsible for writing data to a CSV file in a specified output folder.

    Attributes:
        output_folder (Path): Path object pointing to the folder where the CSV will be saved.
        path (Path): Full path to the CSV file including filename.
    """

    def __init__(self, output_folder: str = "output", filename: str = "report.csv"):
        """
        Initialize the CSVExporter with the output folder and filename.

        Args:
            output_folder (str): Folder where CSV file will be saved. Defaults to "output".
            filename (str): Name of the CSV file. Defaults to "report.csv".
        """
        self.output_folder = Path(output_folder).resolve()
        self.output_folder.mkdir(parents=True, exist_ok=True)
        self.path = self.output_folder / filename

    def write(self, rows: Iterable[Dict[str, Any]], fieldnames=None):
        """
        Write a list of dictionaries to a CSV file. Automatically determines fieldnames
        if not provided, preserving the order of first appearance.

        Args:
            rows (Iterable[Dict[str, Any]]): Iterable of dictionaries representing CSV rows.
            fieldnames (List[str], optional): List of column names for the CSV. If None,
                                              the keys from the rows are used in order.

        Returns:
            str: The full path to the written CSV file as a string.
        """
        rows = list(rows)
        if not rows:
            return str(self.path)

        # Determine fieldnames from first occurrence of keys in rows if not provided
        if fieldnames is None:
            seen = []
            for r in rows:
                for k in r.keys():
                    if k not in seen:
                        seen.append(k)
            fieldnames = seen

        # Open CSV file and write rows
        with open(self.path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for r in rows:
                # Ensure all fieldnames are present in each row
                writer.writerow({k: r.get(k, "") for k in fieldnames})

        return str(self.path)
