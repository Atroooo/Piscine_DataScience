from load_csv import load
from projection_life import projection_life


def main():
    """Main function to test the functions.
    """
    income_data = load(
        "income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life_expectancy_data = load("life_expectancy_years.csv")
    projection_life(life_expectancy_data, income_data)

    income_data = load(
        "income_per_person_gdppercapita_ppp_inflation_adjusted1.csv")
    life_expectancy_data = load("life_expectancy_years1.csv")
    projection_life(life_expectancy_data, income_data)


if __name__ == "__main__":
    main()
