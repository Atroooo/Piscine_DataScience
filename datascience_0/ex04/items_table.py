import pandas as pd
import sqlalchemy
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
        if not os.path.exists(file_path) or os.path.isdir(file_path):
            raise AssertionError("File not found:", file_path)
        df = pd.read_csv(file_path)
        return df
    except AssertionError as error:
        print(f"{AssertionError.__name__}: {error}")
        return None


def insert_data_in_db(path: str, table_name: str) -> None:
    """Insert data into the database.

    Args:
        path (str): Path to the CSV file
        tableName (str): Name of the table
    """
    assert isinstance(path, str) or isinstance(table_name, str), \
        "Path and table_name must be a string"

    data = load(path)
    if data is None:
        print("Error while opening the file")
        return
    try:
        engine = sqlalchemy.create_engine(
            "postgresql://lcompieg:mysecretpassword@localhost:5432/piscineds")
        data_types = {
            "product_id": sqlalchemy.types.Integer(),
            "category_id": sqlalchemy.types.Float(),
            "category_code": sqlalchemy.types.String(length=255),
            "brand": sqlalchemy.types.String(length=255)
        }
        data = data.drop_duplicates(keep="first", subset=['product_id'])
        data.to_sql(table_name, engine, index=False, dtype=data_types,
                    if_exists='replace')
        engine.dispose()
    except Exception as e:
        print(e)


def main():
    """Main function to test the functions.
    """
    insert_data_in_db("/home/lcompieg/sgoinfre/item/item.csv",
                      "items")


if __name__ == "__main__":
    main()
