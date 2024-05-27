import pandas as pd
import os


def load(path: str) -> pd.DataFrame:
    """Load a CSV file into a Dataset object.

    Args:
        path (str): path to the CSV file

    Returns:
        Dataset: object containing the data
    """
    try:
        if not path.lower().endswith(("csv")):
            raise AssertionError("Only csv formats are supported.")
        if not os.path.exists(path):
            raise AssertionError("File not found:", path)
        df = pd.read_csv(path)
        print("Dataset shape:", df.shape)
        print(df.head(1))
        return df
    except AssertionError as error:
        print(f"{AssertionError.__name__}: {error}")
        return None


def main():
    """Main function to test the functions.
    """
    df = load("life_expectancy_years.csv")
    print(df)


if __name__ == "__main__":
    main()
