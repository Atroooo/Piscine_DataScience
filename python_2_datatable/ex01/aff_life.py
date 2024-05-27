from load_csv import load
from matplotlib import pyplot as plt

def aff_life(df):
    """Print the life expectancy of each country in the dataset.

    Args:
        df (pd.DataFrame): dataset containing the life expectancy data
    """
    try:
        if df is None:
            return None
        data_france = df[df["country"] == "France"]
        years = data_france.columns[1:]
        life_france = data_france.values[0][1:]
        plt.plot(years, life_france, label=None)
        plt.title("Life expectancy in France")
        plt.xlabel("Year")
        plt.xticks(years[::40], rotation=45)
        plt.ylabel("Life expectancy")
        plt.yticks(range(30, 99, 10))
        plt.legend()
        plt.tight_layout()
        plt.show()
    except KeyError as error:
        print(f"{KeyError.__name__}: {error}")
        return None


def main():
    """Main function to test the functions.
    """
    df = load("life_expectancy_years.csv")
    aff_life(df)


if __name__ == "__main__":
    main()
