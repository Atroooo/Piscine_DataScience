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
        local_dir = os.path.dirname(__file__)
        file_path = os.path.join(local_dir, path)
        if not os.path.exists(file_path):
            raise AssertionError("File not found:", file_path)
        df = pd.read_csv(file_path)
        print("Dataset shape:", df.shape)
        print(df.head(1))
        return df
    except AssertionError as error:
        print(f"{AssertionError.__name__}: {error}")
        return None
