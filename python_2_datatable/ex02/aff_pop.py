from load_csv import load
from matplotlib import pyplot as plt

def aff_pop(df):
    """Displays the country information versus other country information.

    Args:
        df (pd.DataFrame): dataset containing the population data
    """
    try:
        if df is None:
            return None
        data_france = df[df["country"] == "France"]
        data_belgium = df[df["country"] == "Belgium"]

        years = data_france.columns[1:]

        plt.plot(years, data_france.values[0][1:], label="France")
        plt.plot(years, data_belgium.values[0][1:], label="Belgium")

        plt.show()
    except KeyError as error:
        print(f"{KeyError.__name__}: {error}")
        return None


def main():
    """Main function to test the functions.
    """
    df = load("population_total.csv")
    print(df.head(1))
    aff_pop(df)


if __name__ == "__main__":
    main()
