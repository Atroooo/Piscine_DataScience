import sys


if len(sys.argv) > 2:
    print("AssertionError: more than one argument is provided")
elif len(sys.argv) == 0:
    exit(0)
else:
    number = 0
    try:
        number = int(sys.argv[1])
    except ValueError:
        print("AssertionError: argument is not an integer")
        exit(0)

    if (number % 2 == 0):
        print("I'm Even.")
    else:
        print("I'm Odd.")
