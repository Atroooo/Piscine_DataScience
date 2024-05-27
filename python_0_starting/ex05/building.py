import sys


def count_char(str):
    """
    text (input string): The text to analyze

    Prints the following information:
    1. The number of characters in the text
    2. The number of upper case letters
    3. The number of lower case letters
    4. The number of punctuation marks
    5. The number of spaces
    6. The number of digits
    """
    upper = lower = punct = spaces = digits = 0
    for char in str:
        if (char.isupper()):
            upper += 1
        elif (char.islower()):
            lower += 1
        elif (char.isdigit()):
            digits += 1
        elif (char.isspace()):
            spaces += 1
        elif (char in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"):
            punct += 1

    print("The text contains", len(str), "characters:")
    print(upper, "upper letters")
    print(lower, "lower letters")
    print(punct, "punctuation marks")
    print(spaces, "spaces")
    print(digits, "digits")


def main():
    """
    Analyzes the given text and prints information about its char composition.

    Asks for input if no argument is given:

    raises AssertionError: Too many arguments provided
    """
    try:
        if len(sys.argv) < 2:
            try:
                s = input("What is the text to count?\n")
                s += "\n"
            except EOFError:
                pass
        elif len(sys.argv) == 2:
            s = sys.argv[1]
        elif len(sys.argv) > 2:
            raise AssertionError("Too many arguments provided")
        count_char(s)
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


if __name__ == "__main__":
    main()
