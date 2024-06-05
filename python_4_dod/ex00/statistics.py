def ft_statistics(*args: any, **kwargs: any) -> None:
    numbers = []

    for arg in args:
        if (isinstance(arg, int) or isinstance(arg, float)):
            numbers.append(arg)

    for key, value in kwargs.items():
        try:
            if (value == "mean"):
                mean(numbers)
            elif (value == "median"):
                median(numbers)
            elif (value == "quartile"):
                quartile(numbers)
            elif (value == "std"):
                standard_deviation(numbers)
            elif (value == "var"):
                variance(numbers)
        except Exception:
            print("ERROR")


def mean(nb_list):
    print(sum(nb_list) / len(nb_list))


def median(nb_list):
    quotient, remainder = divmod(len(nb_list), 2)
    if remainder:
        print(sorted(nb_list)[quotient])
        return
    print(sum(sorted(nb_list)[quotient - 1:quotient + 1]) / 2)


def quartile(nb_list):
    nb_list = sorted(nb_list)
    print(nb_list[int(len(nb_list) / 4)], nb_list[3 * int(len(nb_list) / 4)])


def standard_deviation(nb_list):
    pass


def variance(nb_list):
    pass
