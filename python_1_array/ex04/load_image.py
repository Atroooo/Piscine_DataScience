from numpy import array
from matplotlib import image
import os


def ft_load(path: str) -> array:
    """Load an image from a file as an array.

    Args:
        path (str): path to the image

    Returns:
        array: image as an array
    """
    try:
        if not path.lower().endswith(("jpg", "jpeg")):
            raise AssertionError("Only JPG and JPEG formats are supported.")
        if not os.path.exists(path):
            raise AssertionError("File not found:", path)
        image_opened = image.imread(path)
        image_as_array = array(image_opened)
        print("Image shape:", image_as_array.shape)
        return image_as_array
    except AssertionError as error:
        print("\033[31m", AssertionError.__name__ + ":", error, "\033[0m")
        return ""
