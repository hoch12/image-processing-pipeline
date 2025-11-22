from pathlib import Path
import csv
from typing import Iterable, Dict, Any


class CSVExporter:
    def __init__(self, output_folder: str = "output", filename: str = "report.csv"):
        self.output_folder = Path(output_folder).resolve()
        self.output_folder.mkdir(parents=True, exist_ok=True)
        self.path = self.output_folder / filename

    def write(self, rows: Iterable[Dict[str, Any]], fieldnames=None):
        rows = list(rows)
        if not rows:
            return str(self.path)

        if fieldnames is None:
            seen = []
            for r in rows:
                for k in r.keys():
                    if k not in seen:
                        seen.append(k)
            fieldnames = seen

        with open(self.path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for r in rows:
                writer.writerow({k: r.get(k, "") for k in fieldnames})

        return str(self.path)
