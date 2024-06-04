from load_image import ft_load
from pimp_image import ft_show, ft_invert, ft_red, ft_green, ft_blue, ft_grey


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
