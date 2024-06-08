def square(x: int | float) -> int | float:
    """Function that squares a number.

    Args:
        x (int | float): The number to square.

    Returns:
        int | float: The squared number.
    """
    return x * x


def pow(x: int | float) -> int | float:
    """Function that raises a number to the power of itself.

    Args:
        x (int | float): The number to raise to the power of itself.

    Returns:
        int | float: The number raised to the power of itself.
    """
    return x ** x


def outer(x: int | float, function) -> object:
    """Function that returns a function that applies the given function to the

    Args:
        x (int | float): The number to apply the function to.
        function (_type_): The function to apply to the number.

    Returns:
        object: The function that applies the given function to the number.
    """
    assert callable(function), "The function argument is not callable."
    assert isinstance(x, (int, float)), \
        "The x argument should be an integer or a float."

    def inner() -> float:
        """Inner function that applies the given function to the number.

        Returns:
            float: The result of the function applied to the number.
        """
        nonlocal x
        result = function(x)
        x = result
        return result
    return inner
