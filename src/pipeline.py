from pathlib import Path
from typing import List
from .loader import ImageLoader
from .validator import ImageValidator
from .processor import ImageProcessor, make_resize_and_save_step
from .exporter import CSVExporter


class ImagePipeline:
    def __init__(self,
                 input_folder: str = "input",
                 output_folder: str = "output",
                 max_workers: int = 4,
                 resize_max: int = 1024):
        self.loader = ImageLoader(input_folder)
        self.validator = ImageValidator(min_width=2, min_height=2)
        self.processor = ImageProcessor(output_folder=output_folder, max_size=resize_max)
        self.processor.add_step(make_resize_and_save_step(output_folder=output_folder, max_size=resize_max))
        self.exporter = CSVExporter(output_folder=output_folder)
        self.max_workers = max_workers

    def run(self):
        paths = self.loader.get_image_paths()
        validated = [self.validator.validate(Path(p)) for p in paths]
        to_process = []
        results = []
        for v in validated:
            if v.get("ok"):
                to_process.append(Path(v["path"]))
            else:
                results.append(v)
        if to_process:
            processed = self.processor.run_parallel(to_process, max_workers=self.max_workers)
            for p in processed:
                src = p.get("source")
                vd = next((x for x in validated if str(x["path"]) == str(src)), {})
                merged = {}
                merged.update(vd)
                merged.update(p)
                results.append(merged)
        csv_path = self.exporter.write(results)
        return {"csv": csv_path, "count_validated": len(validated), "count_processed": len(to_process)}
