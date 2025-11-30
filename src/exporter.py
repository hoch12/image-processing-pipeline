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

    def write(self, rows: Iterable[Dict[str, Any]], fieldnames=None) -> str:
        """
        Write rows to CSV. Determines fieldnames automatically if not provided.

        Each row should contain keys like:
            - 'source': original image path
            - 'processed_path': path to processed image
            - 'processed_width': width after resize
            - 'processed_height': height after resize
            - 'resize_percentage': percentage used for resizing (if applicable)

        Args:
            rows (Iterable[Dict[str, Any]]): Iterable of dictionaries representing rows.
            fieldnames (List[str], optional): Column names. If None, inferred from keys.

        Returns:
            str: Full path to the written CSV file. Returns path even if rows are empty.
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
