from matplotlib import pyplot as plt
from load_image import ft_load
from rotate import ft_zoom, transpose


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
