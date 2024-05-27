from matplotlib import pyplot as plt
from numpy import array
import numpy as np
from load_image import ft_load


def ft_invert(array) -> array:
    """Inverse the colors of an image.

    Args:
        array (np.array): image as an array

    Returns:
        array: image with inverted colors
    """
    image = 255 - array
    ft_show(image)


def ft_red(array) -> array:
    """Convert the colors of an image to red.

    Args:
        array (np.array): image as an array

    Returns:
        array: image with red colors
    """
    red_channel = array[:, :, 0]
    image = np.zeros_like(array)
    image[:, :, 0] = red_channel
    ft_show(image)


def ft_green(array) -> array:
    """Convert the colors of an image to green.

    Args:
        array (np.array): image as an array

    Returns:
        array: image with green colors
    """
    green_channel = array[:, :, 1]
    image = array.copy()
    image[:, :, 0] = 0
    image[:, :, 1] = green_channel
    image[:, :, 2] = 0
    ft_show(image)


def ft_blue(array) -> array:
    """Convert the colors of an image to blue.

    Args:
        array (np.array): image as an array

    Returns:
        array: image with blue colors
    """
    blue_channel = array[:, :, 2]
    image = np.zeros_like(array)
    image[:, :, 2] = blue_channel
    ft_show(image)


def ft_grey(array) -> array:
    """Convert the colors of an image to grey.

    Args:
        array (np.array): image as an array

    Returns:
        array: image with grey colors
    """
    red_channel = array[:, :, 0] / 3
    green_channel = array[:, :, 1] / 3
    blue_channel = array[:, :, 2] / 3
    grey_channel = red_channel + green_channel + blue_channel
    grey_image = np.stack([grey_channel, grey_channel, grey_channel], axis=2)
    ft_show(grey_image)


def ft_show(array):
    """Show an image.

    Args:
        array (np.array): image as an array
    """
    plt.imshow(array)
    plt.show()


def main():
    """Main function to test the functions.
    """
    array = ft_load("landscape.jpg")
    print(array)
    ft_show(array)
    ft_invert(array)
    ft_red(array)
    ft_green(array)
    ft_blue(array)
    ft_grey(array)
    print(ft_invert.__doc__)


if __name__ == "__main__":
    main()
