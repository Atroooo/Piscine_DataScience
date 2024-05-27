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
        print(AssertionError.__name__ + ":", error)
        return ""


def main():
    """Main function to test the functions.
    """
    print(ft_load("landscape.jpg"))


if __name__ == "__main__":
    main()
