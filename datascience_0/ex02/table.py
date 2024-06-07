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


def process_data(file: str) -> pd.DataFrame:
    data = load(file)
    assert data is not None, "data is empty"
    try:
        data['event_time'] = pd.to_datetime(data['event_time'])
    except Exception as e:
        print(e)
        return None
    return data


def create_table(cursor: object) -> None:
    commands = (
        '''CREATE TABLE data_2022_oct''',
        '''CREATE TABLE data_2022_nov''',
        '''CREATE TABLE data_2022_dec''',
        '''CREATE TABLE data_2023_jan'''
    )
    try:
        for command in commands:
            cursor.execute(command)
    except Exception as e:
        print(e)


def insert_data_in_db() -> None:
    conn = psycopg2.connect(
        database="piscineds",
        user='lcompieg',
        password='mysecretpassword',
        host='localhost',
        port='5432'
    )
    conn.autocommit = True
    cursor = conn.cursor()
    create_table(cursor)

    data_2022_oct = process_data("/home/lcompieg/sgoinfre/subject/ \
                                customer/data_2022_oct.csv")
    data_2022_oct.to_sql('data_2022_oct', con=conn, if_exists='replace')

    data_2022_nov = process_data("/home/lcompieg/sgoinfre/subject/ \
                                customer/data_2022_nov.csv")
    data_2022_nov.to_sql('data_2022_nov', con=conn, if_exists='replace')

    data_2022_dec = process_data("/home/lcompieg/sgoinfre/subject/ \
                                customer/data_2022_dec.csv")
    data_2022_dec.to_sql('data_2022_dec', con=conn, if_exists='replace')

    data_2023_jan = process_data("/home/lcompieg/sgoinfre/subject/ \
                                customer/data_2023_jav.csv")
    data_2023_jan.to_sql('data_2023_jan', con=conn, if_exists='replace')

    conn.close()
