from matplotlib import pyplot as plt
import numpy as np
from load_image import ft_load


def ft_zoom(array):
    """Zoom the image by 2.
    Args:
        array (array): image as an array
    Returns:
        array: zoomed image as an array
    """
    try:
        height, width = array.shape[:2]
        zoom_factor = 0.55
        new_height = int(height * zoom_factor)
        new_width = int(width * zoom_factor)

        center_x = int(width / 2 + 115)
        center_y = int(height / 2 - 115)

        start_x = int(max(0, center_x - new_width // 2))
        start_y = int(max(0, center_y - new_height // 2))
        end_x = min(width, start_x + new_width)
        end_y = min(height, start_y + new_height)

        return array[start_y:end_y, start_x:end_x]
    except Exception:
        print("Something went wrong.")


def transpose(array):
    """Transpose the image.
    Args:
        array (np.array): image as an array
    Returns:
        np.array: transposed image as an array
    """

    height, width = array.shape[:2]
    rez = []
    for w in range(width):
        row = []
        for h in range(height):
            element = array[h][w]
            row.append(element)
        rez.append(row)
    return np.array(rez)


def main():
    """Main function to test the functions.
    """
    array = ft_load("animal.jpeg")
    print(array)
    zoomed_array = ft_zoom(array)
    transposed_array = transpose(zoomed_array)
    print("New shape after Transpose:", transposed_array.shape)
    plt.imshow(transposed_array)
    plt.show()


if __name__ == "__main__":
    main()
