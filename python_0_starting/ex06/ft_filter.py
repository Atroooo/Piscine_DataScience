def ft_filter(function, input):
    """
    Description:
        ft_filter(function, input) filters the input based
        on the function to apply.
    Args:
        function: function that returns a boolean value.
        input: list of input to be filtered.
    Returns:
        Returns a list of inputs that satisfy the function to apply.
    """
    if function:
        return [x for x in input if function(x)]
    return [x for x in input if x]
