def ft_statistics(*args: any, **kwargs: any) -> None:
    numbers = []

    for arg in args:
        if isinstance(arg, int) or isinstance(arg, float):
            numbers.append(arg)
    
    if (len(numbers) <= 0):
        print("ERROR")
        return

    for key, value in kwargs.items():
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
        else:
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
    pass


def standard_deviation(nb_list):
    pass


def variance(nb_list):
    pass
