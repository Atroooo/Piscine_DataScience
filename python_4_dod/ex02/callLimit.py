def callLimit(limit: int):
    """Function that limits the number of calls to a function.

    Args:
        limit (int): The number of calls allowed.

    Raises:
        Exception: No more calls allowed.
    Returns:
        function: Returns the function if the number of
            calls is less than the limit.
    """
    count = 0
    assert isinstance(limit, int), "limit must be an integer."

    def callLimiter(function):
        """This inner function is used to wrap around the target function.
        It tracks the number of times the target function is called
        using the 'count' variable.

        Args:
            function (function): The target function to be limited.
        """
        def limit_function(*args: any, **kwds: any):
            """Used as a wrapper around the decorated function.
            It increments the 'count' variable each time the wrapped
            function is called.

            Raises:
                Exception: No more calls allowed.

            Returns:
                Any: The result of the wrapped function if the number
                    of calls is less than the limit.
            """
            try:
                nonlocal count
                count += 1
                if count > limit:
                    raise Exception(f"No more calls of {function} allowed.")
                else:
                    return function(*args, **kwds)
            except Exception as e:
                print(e)
        return limit_function
    return callLimiter
