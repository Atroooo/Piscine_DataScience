import pandas as pd
import sqlalchemy


def get_table_data_from_db(engine: object, table_name: str) -> pd.DataFrame:
    """Get data from a table in the database.

    Args:
        engine (object): database engine
        table_name (str): name of the table

    Returns:
        pd.DataFrame: data from the table
    """
    return pd.read_sql_query(f'select * from {table_name}', con=engine)


def get_all_table_names(connection: object, name: str) -> list:
    sql = sqlalchemy.text(
        'SELECT * FROM pg_catalog.pg_tables WHERE schemaname != \'pg_catalog\'\
        AND schemaname != \'information_schema\'')
    sql_result = connection.execute(sql)
    results_as_dict = sql_result.mappings().all()
    table_list = []
    for key in results_as_dict:
        table_list.append(key["tablename"])
    for table in table_list:
        if not table.startswith(name):
            table_list.remove(table)
    return table_list


def insert_in_table(engine: object, data: pd.DataFrame) -> None:
    """Insert data into the database.

    Args:
        engine (object): database engine
        data (pd.DataFrame): data to insert
    """
    data_types = {
            "event_time": sqlalchemy.DateTime(),
            "event_type": sqlalchemy.types.String(length=255),
            "product_id": sqlalchemy.types.Integer(),
            "price": sqlalchemy.types.Float(),
            "user_id": sqlalchemy.types.BigInteger(),
            "user_session": sqlalchemy.types.UUID(as_uuid=True)
        }
    data.to_sql("customers", engine, index=False, dtype=data_types,
                if_exists='append')


def join_tables(engine: object, tables: list) -> None:
    """Join tables and insert the data into the customers table.

    Args:
        engine (object): database engine
        tables (list): list of table's names to join
    """
    assert isinstance(tables, list), "join_df take list as parameter"
    for table in tables:
        try:
            temp_df = get_table_data_from_db(engine, table)
            insert_in_table(engine, temp_df)
            print(f"{table} has been added to customers")
        except Exception as e:
            print(e)
            return


def main():
    """Main function to test the functions.
    """
    try:
        engine = sqlalchemy.create_engine(
            "postgresql://lcompieg:mysecretpassword@localhost:5432/piscineds")
        connection = engine.connect()
        tables = get_all_table_names(connection, "data_20")
        join_tables(engine, tables)
        engine.dispose()
    except Exception as e:
        print(e)
        return


if __name__ == "__main__":
    main()
