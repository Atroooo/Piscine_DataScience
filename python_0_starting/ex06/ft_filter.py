def ft_filter(function, input):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if function:
        return [x for x in input if function(x)]
    return [x for x in input if x]
