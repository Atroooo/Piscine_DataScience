from load_csv import load
from aff_pop import aff_pop


def main():
    """Main function to test the functions.
    """
    df = load("population_total.csv")
    print(df.head(1))
    aff_pop(df)

    df = load("population_total1.csv")
    aff_pop(df)


if __name__ == "__main__":
    main()
