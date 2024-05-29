from load_csv import load
from matplotlib import pyplot as plt


def aff_pop(df):
    """Displays the country information versus other country information.

    Args:
        df (pd.DataFrame): dataset containing the population data
    """
    data_france = df[df['country'] == "France"].iloc[:, 1:]
    data_belgium = df[df['country'] == "Belgium"].iloc[:, 1:]

    years = data_france.columns.astype(int)

    france_pop = data_france.values.flatten()
    belgium_pop = data_belgium.values.flatten()

    france_pop = [float(pop[:-1]) * 1e6 for pop in france_pop]
    belgium_pop = [float(pop[:-1]) * 1e6 for pop in belgium_pop]

    plt.title("Population in France and Belgium")
    plt.plot(years, france_pop, label="France")
    plt.plot(years, belgium_pop, label="Belgium")
    plt.legend()
    plt.xlabel("Year")
    plt.xticks(range(1800, 2051, 40), range(1800, 2051, 40))
    plt.xlim(1800, 2040)
    plt.ylabel("Population")
    max_pop = max(max(france_pop), max(belgium_pop))
    y_ticks = [i * 1e7 for i in range(int(max_pop / 1e7) + 1)]
    plt.yticks(y_ticks, ["{:,.0f}M".format(pop / 1e6) for pop in y_ticks])
    plt.tight_layout()
    plt.show()


def main():
    """Main function to test the functions.
    """
    df = load("population_total.csv")
    print(df.head(1))
    aff_pop(df)


if __name__ == "__main__":
    main()
