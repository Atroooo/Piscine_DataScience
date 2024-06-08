import pandas as pd
import sqlalchemy


def get_table_from_db(engine: object, table_name: str) -> pd.DataFrame:
    return pd.read_sql_query(f'select * from {table_name}', con=engine)


def get_all_table(connection: object, name: str) -> list:
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


def create_table(engine: object, data: pd.DataFrame) -> None:
    data_types = {
            "event_time": sqlalchemy.DateTime(),
            "event_type": sqlalchemy.types.String(length=255),
            "product_id": sqlalchemy.types.Integer(),
            "price": sqlalchemy.types.Float(),
            "user_id": sqlalchemy.types.BigInteger(),
            "user_session": sqlalchemy.types.UUID(as_uuid=True)
        }
    data.to_sql("customers", engine, index=False, dtype=data_types,
                if_exists='replace')


def join_df(engine: object, tables: list) -> pd.DataFrame:
    assert isinstance(tables, list), "join_df take list as parameter"
    final_df = pd.DataFrame()
    for table in tables:
        try:
            temp_df = get_table_from_db(engine, table)
            final_df = pd.concat([final_df, temp_df])
        except Exception as e:
            print(e)
            return None
    print("Before sort")
    final_df = final_df.sort_values(by=['event_time'])
    print("Final dataFrame created")
    create_table(engine, final_df)
    return final_df


def main():
    """Main function to test the functions.
    """
    try:
        engine = sqlalchemy.create_engine(
            "postgresql://lcompieg:mysecretpassword@localhost:5432/piscineds")
        connection = engine.connect()
        tables = get_all_table(connection, "data_20")
        df = join_df(engine, tables)
    except Exception as e:
        print(e)
        return


if __name__ == "__main__":
    main()
