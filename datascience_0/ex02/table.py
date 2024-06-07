import pandas as pd
import psycopg2
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


def create_columns(data: pd.DataFrame) -> str:
    """Create the columns for the table.

    Args:
        data (pd.DataFrame): data from the CSV file

    Returns:
        str: columns for the table
    """
    res = ''
    columns = data.columns
    type_data = data.dtypes
    for column in columns:
        res += column + ' ' + str(type_data[column]) + ', '
    return res[:-2]


def create_table(conn: object, cursor: object, table_name: str,
                 data: pd.DataFrame) -> bool:
    """Create a table in the database.

    Args:
        conn (object): database connection
        cursor (object): database cursor
        table_name (str): name of the table
        data (pd.DataFrame): data from the CSV file

    Returns:
        bool: Return True if the table is created, False otherwise
    """
    columns = create_columns(data)
    command = \
        '''CREATE TABLE IF NOT EXISTS {name}({columns})''' \
        .format(name=table_name, columns=columns)
    try:
        cursor.execute(command)
        conn.commit()
    except Exception as e:
        print(e)
        return False
    return True


def insert_data_in_db(path: str, table_name: str) -> None:
    """Insert data into the database.

    Args:
        path (str): Path to the CSV file
        tableName (str): Name of the table
    """
    assert isinstance(path, str) or isinstance(table_name, str), \
        "Path and table_name must be a string"
    conn = psycopg2.connect(
        database="piscineds",
        user='lcompieg',
        password='mysecretpassword',
        host='localhost',
        port='5432'
    )
    cursor = conn.cursor()

    data_2022_oct = load(path)
    assert create_table(conn, cursor, table_name, data_2022_oct), \
        "Something went wrong"
    data_2022_oct.to_sql('data_2022_oct', con=conn, if_exists='replace')

    conn.commit()
    conn.close()


def main():
    """Main function to test the functions.
    """
    insert_data_in_db("/home/lcompieg/sgoinfre/data_2022_oct.csv",
                      "data_2022_oct")


if __name__ == "__main__":
    main()
