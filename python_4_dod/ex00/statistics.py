def ft_statistics(*args: any, **kwargs: any) -> None:
    """This function takes any number of arguments and keyword arguments and
    prints the result of the statistical operation
    specified in the keyword arguments.
    """
    numbers = []

    for arg in args:
        if (isinstance(arg, bool)):
            continue
        if (isinstance(arg, (int, float))):
            numbers.append(arg)

    if len(numbers) == 0:
        for value in kwargs.items():
            print("ERROR")
        return

    for key, value in kwargs.items():
        try:
            if (value == "mean"):
                print(mean(numbers))
            elif (value == "median"):
                print(median(numbers))
            elif (value == "quartile"):
                print(quartile(numbers))
            elif (value == "std"):
                print(standard_deviation(numbers))
            elif (value == "var"):
                print(variance(numbers))
        except Exception:
            print("ERROR")


def mean(nb_list):
    """This function calculates the mean of a list of numbers.

    Args:
        nb_list (list): A list of numbers.

    Returns:
        int | float: The mean of the list of numbers.
    """
    mean_result = sum(nb_list) / len(nb_list)
    return mean_result


def median(nb_list):
    """This function calculates the median of a list of numbers.

    Args:
        nb_list (list): A list of numbers.

    Returns:
        int | float: The median of the list of numbers.
    """
    quotient, remainder = divmod(len(nb_list), 2)
    median_result = 0
    if remainder:
        median_result = sorted(nb_list)[quotient]
        return median_result
    median_result = sum(sorted(nb_list)[quotient - 1:quotient + 1]) / 2
    return median_result


def quartile(nb_list):
    """This function calculates the quartile of a list of numbers.

    Args:
        nb_list (list): A list of numbers.

    Returns:
        int | float: _description_
    """
    nb_list = sorted(nb_list)
    return [float(nb_list[int(len(nb_list) / 4)]),
            float(nb_list[3 * int(len(nb_list) / 4)])]


def variance(nb_list):
    """This function calculates the variance of a list of numbers.

    Args:
        nb_list (list): A list of numbers.

    Returns:
        int | float: _description_
    """
    mean_result = mean(nb_list)
    variance_total = variance_result = 0
    for nb in nb_list:
        variance_total += (nb - mean_result) ** 2
    variance_result = variance_total / len(nb_list)
    return variance_result


def standard_deviation(nb_list):
    """This function calculates the standard deviation of a list of numbers.

    Args:
        nb_list (list): A list of numbers.

    Returns:
        int | float: _description_
    """
    variance_result = variance(nb_list)
    return variance_result ** 0.5
