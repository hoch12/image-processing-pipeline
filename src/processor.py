class ImageProcessor:
    def __init__(self):
        self.steps = []

    def add_step(self, func):
        self.steps.append(func)

    def run(self, images):
        processed = []

        for img in images:
            current = img
            for step in self.steps:
                current = step(current)
            processed.append(current)

        return processed
