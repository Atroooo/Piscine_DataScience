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
            "event_time": sqlalchemy.DateTime(),
            "event_type": sqlalchemy.types.String(length=255),
            "product_id": sqlalchemy.types.Integer(),
            "price": sqlalchemy.types.Float(),
            "user_id": sqlalchemy.types.BigInteger(),
            "user_session": sqlalchemy.types.UUID(as_uuid=True)
        }
        data.to_sql(table_name, engine, index=False, dtype=data_types,
                    if_exists='replace')
        engine.dispose()
    except Exception as e:
        print(e)


def create_tables(path: str) -> None:
    files = os.listdir(path)
    for file in files:
        table_name = file.split('.')
        if (len(table_name) > 2):
            print("Error in file name ", file)
            continue
        insert_data_in_db(path + str(file), table_name[0])


def main():
    """Main function to test the functions.
    """
    path = "/home/lcompieg/sgoinfre/custom/"
    create_tables(path)
    

if __name__ == "__main__":
    main()
