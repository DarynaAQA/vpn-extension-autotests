import os
from PIL import Image, ImageChops
from io import BytesIO


class ImageParser:

    def __init__(self):
        self.percent_threshold = 0.1

    def compare_elem_png(self, png_fresh: bytes, png_icon: bytes) -> bool:
        """
            Method to compare two images, with difference percentage threshold that could be changed
        """
        image_fresh = Image.open(BytesIO(png_fresh))
        image_icon = Image.open(BytesIO(png_icon))
        diff = ImageChops.difference(image_fresh, image_icon)
        if diff.getbbox() is None:
            return True
        diff_percent = (diff.getbbox()[2] * diff.getbbox()[3]) / (image_fresh.size[0] * image_fresh.size[1])
        if diff_percent <= self.percent_threshold:
            return True
        return False

    def set_percent_threshold(self, percent_threshold: float) -> None:
        """
            Set new percent threshold.
        """
        self.percent_threshold = percent_threshold

    @staticmethod
    def save_as_png(file_name: str, content: bytes) -> None:
        with open(file_name, 'wb') as f:
            f.write(content)

    @staticmethod
    def remove_by_path(file_path) -> None:
        try:
            os.remove(file_path)
        except OSError as e:
            print(f"Error deleting the file: {e}")

    @staticmethod
    def read_png_content(png_file_path) -> bytes:
        with open(png_file_path, 'rb') as f:
            png_content = f.read()
        return png_content
