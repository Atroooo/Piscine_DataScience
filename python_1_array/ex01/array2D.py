import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """_summary_

    Args:
        family (list): 2D array of family members
        start (int): start index
        end (int): end index

    Raises:
        AssertionError: Input must be a list and 2 integer.
        AssertionError: Input list with different sizes.

    Returns:
        list: sliced 2D array
    """
    try:
        if not isinstance(family, list) \
                or not isinstance(start, int) or not isinstance(end, int):
            raise AssertionError("Input must be a list and 2 integer.")
        if not all(len(item) == len(family[0]) for item in family):
            raise AssertionError("Input list with different sizes.")
        print("My shape is :", np.array(family).shape)
        print("My new shape is :", np.array(family[start:end]).shape)
        return family[start:end]
    except Exception as error:
        print("An error occurred:", error)
        return ""


def main():
    """Main function to test the functions.
    """
    family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))


if __name__ == "__main__":
    main()
