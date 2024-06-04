import matplotlib.pyplot as plt


def projection_life(life_expectancy_data, income_data):
    """Displays a scatter plot of the life expectancy based on
        the income data in 1900

    Args:
        life_expectancy_data (pd.DataFrame): dataset containing
            the life expectancy
        income_data (pd.DataFrame): dataset containing the income data
    """
    if life_expectancy_data is None or income_data is None:
        return
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
