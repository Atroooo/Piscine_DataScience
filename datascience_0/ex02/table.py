import pandas as pd
import psycopg2
import re
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


def process_data(file: str) -> pd.DataFrame:
    data = load(file)
    assert data is not None, "data is empty"
    try:
        data['event_time'] = pd.to_datetime(data['event_time'])
    except Exception as e:
        print(e)
        return None
    return data


def create_columns(data: pd.DataFrame) -> str:
    res = ''
    columns = data.columns
    type_data = data.dtypes
    for column in columns:
        res += column + ' ' + str(type_data[column]) + ', '
    res = re.sub(r"[\(\[].*?[\)\]]", "", res)
    for c in res:
        if not c.isalpha() and not c.isdigit() and not c.isspace() \
                and c not in ",_":
            res = res.replace(c, '')
    return res[:-2]


def create_table(conn: object, cursor: object, table_name: str,
                 data: pd.DataFrame) -> None:
    
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


def insert_data_in_db() -> None:
    conn = psycopg2.connect(
        database="piscineds",
        user='lcompieg',
        password='mysecretpassword',
        host='localhost',
        port='5432'
    )
    cursor = conn.cursor()

    data_2022_oct = \
        process_data("/home/lcompieg/sgoinfre/data_2022_oct.csv")
    assert create_table(conn, cursor, "data_2022_oct", data_2022_oct), \
        "Something went wrong"
    data_2022_oct.to_sql('data_2022_oct', con=conn, if_exists='replace')

    data_2022_nov = \
        process_data("/home/lcompieg/sgoinfre/data_2022_nov.csv")
    assert create_table(conn, cursor, "data_2022_nov", data_2022_nov), \
        "Something went wrong"
    data_2022_nov.to_sql('data_2022_nov', con=conn, if_exists='replace')

    data_2022_dec = \
        process_data("/home/lcompieg/sgoinfre/data_2022_dec.csv")
    assert create_table(conn, cursor, "data_2022_dec", data_2022_dec), \
        "Something went wrong"
    data_2022_dec.to_sql('data_2022_dec', con=conn, if_exists='replace')

    data_2023_jan = \
        process_data("/home/lcompieg/sgoinfre/data_2023_jav.csv")
    assert create_table(conn, cursor, "data_2023_jan", data_2023_jan), \
        "Something went wrong"
    data_2023_jan.to_sql('data_2023_jan', con=conn, if_exists='replace')

    conn.commit()
    conn.close()


def main():
    """Main function to test the functions.
    """
    insert_data_in_db()


if __name__ == "__main__":
    main()
