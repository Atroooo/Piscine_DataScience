from matplotlib import pyplot as plt
from numpy import array
import numpy as np


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
    image = np.zeros_like(array)
    image[:, :, 1] = green_channel
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
    div = 255 * 3
    red_channel = array[:, :, 0] / div
    green_channel = array[:, :, 1] / div
    blue_channel = array[:, :, 2] / div
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
