import os
import pandas as pd


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
        if not os.path.exists(file_path) or os.path.isdir(file_path):
            raise AssertionError("File not found:", file_path)
        df = pd.read_csv(file_path)
        return df
    except AssertionError as error:
        print(f"{AssertionError.__name__}: {error}")
        return None


def get_all_files(path: str) -> list:
    files = os.listdir(path)
    for file in files:
        table_name = file.split('.')
        assert len(table_name) == 2, "Error in file name"
    return files


def join_df(files: list, path: str) -> pd.DataFrame:
    assert isinstance(files, list) or isinstance(path, str), \
        "join_df take list and str as parameters"
    final_df = pd.DataFrame()
    for file in files:
        try:
            temp_df = load(path + str(file))
            final_df = pd.concat([final_df, temp_df])
        except Exception as e:
            print(e)
            return None
    final_df = final_df.sort_values(by=['event_time'])
    return final_df


def fusion_items(df: pd.DataFrame) -> pd.DataFrame:
    items = load("/home/lcompieg/sgoinfre/item/item.csv")
    df = df.merge(items, on="product_id", how='left')
    df = df.drop_duplicates()
    df = df.sort_values(by=['event_time'])
    return df


def main():
    """Main function to test the functions.
    """
    path = "/home/lcompieg/sgoinfre/custom/"
    try:
        files = get_all_files(path)
        df = join_df(files, path)
        df = fusion_items(df)
    except Exception as e:
        print(e)
        return
    print(df.head(-5))


if __name__ == "__main__":
    main()
