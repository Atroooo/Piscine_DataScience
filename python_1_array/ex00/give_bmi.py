def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Give the BMI of a person based on their height and weight.

    Args:
        height (list[int  |  float]): height of the person
        weight (list[int  |  float]): weight of the person
    Returns:
        list[int | float]: BMI of the persons
    """
    bmi = []
    try:
        if len(height) != len(weight):
            raise ValueError(
                "Lists of height and weight must have the same length.")
        for height, weight in zip(height, weight):
            if not isinstance(height, (int, float)) \
                    or not isinstance(weight, (int, float)):
                raise \
                    TypeError("Height and weight must be integers or floats.")
            if height <= 0 or weight <= 0:
                raise ValueError("Height and weight must be positive.")
            bmi_result = weight / (height ** 2)
            bmi.append(bmi_result)
    except Exception as error:
        print("An error occurred:", error)
    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Apply a limit to the BMI of a person.

    Args:
        bmi (list[int  |  float]): BMI of the persons
        limit (int): limit to apply

    Returns:
        list[bool]: True if the BMI is above the limit, False otherwise
    """
    above_limit = []
    try:
        if not isinstance(limit, float) and not isinstance(limit, int):
            raise TypeError("Limit must be provided as int or float.")
        for i, value in enumerate(bmi):
            if not isinstance(value, (int, float)):
                raise TypeError("BMI must be integers or floats.")
            above_limit.append(value > limit)
    except Exception as error:
        print("An error occurred:", error)
    return above_limit


def main():
    """Main function to test the functions.
    """
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    main()
