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
        local_dir = os.path.dirname(__file__)
        file_path = os.path.join(local_dir, path)
        if not os.path.exists(file_path):
            raise AssertionError("File not found:", file_path)
        image_opened = image.imread(file_path)
        image_as_array = array(image_opened)
        print("Image shape:", image_as_array.shape)
        return image_as_array
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
