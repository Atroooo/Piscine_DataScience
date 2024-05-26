import sys


def convert_to_morse(str):
    """
    This function converts a string to morse code.

    Args:
        str (string): the string to convert

    Returns:
        string
    """

    morse = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '0': '-----', ' ': '/'
    }
    return ' '.join([morse.get(c, c) for c in str.upper()])


def main():
    """
    To run the program you need to input a string as an argument.

    It returns the string converted to morse code.
    """
    try:
        if len(sys.argv) != 2:
            raise AssertionError("AssertionError: the arguments are bad")
        text = sys.argv[1]
        if not isinstance(text, str):
            raise AssertionError("Invalid argument types.")
        for char in text:
            if char.isalnum() is False and char != ' ':
                raise AssertionError("Invalid argument types.")
        morse_code = convert_to_morse(text)
        print(morse_code)
    except ValueError:
        print("AssertionError: the arguments are bad")
    except AssertionError:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
