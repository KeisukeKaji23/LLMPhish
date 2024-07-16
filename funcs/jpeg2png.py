import os
from PIL import Image


def convert_jpeg_to_png(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".jpeg") or filename.endswith(".jpg"):
            img = Image.open(os.path.join(directory, filename))
            png_filename = os.path.splitext(filename)[0] + ".png"
            img.save(os.path.join(directory, png_filename), "PNG")
            os.remove(os.path.join(directory, filename))
            print(f"Converted {filename} to {png_filename}")


convert_jpeg_to_png("/home/keisukekaji/my-study/dataset/spam-phishing/screenshots")
