from src.loader import ImageLoader

loader = ImageLoader("input")
paths = loader.get_image_paths()

print("Nalezené obrázky:")
for p in paths:
    print(" -", p)
