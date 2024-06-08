import os
import pandas as pd
import sqlalchemy


def get_table_from_db(table_name: str) -> pd.DataFrame:
    engine = sqlalchemy.create_engine(
            "postgresql://lcompieg:mysecretpassword@localhost:5432/piscineds")
    return pd.read_sql_query(f'select * from {table_name}', con=engine)


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
            # temp_df = load(path + str(file))
            final_df = pd.concat([final_df, temp_df])
        except Exception as e:
            print(e)
            return None
    final_df = final_df.sort_values(by=['event_time'])
    return final_df


def main():
    """Main function to test the functions.
    """
    path = "/home/lcompieg/sgoinfre/custom/"
    try:
        # files = get_all_files(path)
        print(get_table_from_db("data_2022_oct"))
        # df = join_df(files, path)
    except Exception as e:
        print(e)
        return
    # print(df.head(-5))


if __name__ == "__main__":
    main()
