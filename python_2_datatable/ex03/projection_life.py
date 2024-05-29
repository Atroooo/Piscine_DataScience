from load_csv import load
import matplotlib.pyplot as plt


def projection_life(life_expectancy_data, income_data):
    """Displays the country information versus other country information.

    Args:
        df (pd.DataFrame): dataset containing the income data
    """
    life_expectancy_1900 = life_expectancy_data['1900']
    gnp_1900 = income_data['1900']

    plt.scatter(gnp_1900, life_expectancy_1900)
    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life expectancy")
    plt.xscale("log")
    plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
    plt.tight_layout()
    plt.show()


def main():
    """Main function to test the functions.
    """
    income_data = load(
        "income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life_expectancy_data = load("life_expectancy_years.csv")
    projection_life(life_expectancy_data, income_data)


if __name__ == "__main__":
    main()
