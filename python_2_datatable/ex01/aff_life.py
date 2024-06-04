from matplotlib import pyplot as plt


def aff_life(df):
    """Print the life expectancy of each country in the dataset.

    Args:
        df (pd.DataFrame): dataset containing the life expectancy data
    """
    if df is None:
        return
    data_france = df[df["country"] == "France"]
    life_france = data_france.values[0][1:]
    years = data_france.columns[1:]

    plt.plot(years, life_france, label="France")
    plt.title("Life expectancy in France")
    plt.xlabel("Year")
    plt.xticks(years[::40], rotation=45)
    plt.ylabel("Life expectancy")
    plt.yticks(range(30, 99, 10))
    plt.legend()
    plt.tight_layout()
    plt.show()
