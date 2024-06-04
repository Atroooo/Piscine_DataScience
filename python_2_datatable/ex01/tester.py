from aff_life import aff_life
from load_csv import load


def main():
    """Main function to test the functions.
    """
    df = load("life_expectancy_years.csv")
    aff_life(df)

    df = load("life_expectancy_years1.csv")
    aff_life(df)


if __name__ == "__main__":
    main()
