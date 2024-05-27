import sys
from ft_filter import ft_filter


def main():
    """
    To run the program you need to input a string and an integer as arguments.

    It returns a list of words from the string that have a length greater
        than the integer.
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError("AssertionError: the arguments are bad")
        text = sys.argv[1]
        number = int(sys.argv[2])

        if not isinstance(text, str) or not isinstance(number, int):
            raise AssertionError("Invalid argument types.")

        filtered_words = \
            list(ft_filter(lambda word: len(word) > number, text.split()))

        print(filtered_words)
    except ValueError:
        print("AssertionError: the arguments are bad")
    except AssertionError:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
