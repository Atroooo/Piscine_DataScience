from load_image import ft_load
from zoom import ft_zoom


def main():
    """Main function to test the functions.
    """
    array = ft_load("animal.jpeg")
    print(array)
    ft_zoom(array)


if __name__ == "__main__":
    main()
