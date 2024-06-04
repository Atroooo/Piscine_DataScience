from matplotlib import pyplot as plt


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

        image_zoomed = array[start_y:end_y, start_x:end_x]
        print("New shape after slicing:", image_zoomed.shape)
        print(image_zoomed)
        plt.imshow(image_zoomed)
        plt.show()
    except Exception:
        print("Something went wrong.")
