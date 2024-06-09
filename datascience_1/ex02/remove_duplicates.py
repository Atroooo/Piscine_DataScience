import sqlalchemy


def main():
    """Main function to test the functions.
    """
    try:
        engine = sqlalchemy.create_engine(
            "postgresql://lcompieg:mysecretpassword@localhost:5432/piscineds")
        connection = engine.connect()
        sql = sqlalchemy.text(
            'CREATE TEMPORARY TABLE tmp AS SELECT DISTINCT * FROM customers; \
                TRUNCATE customers; \
                INSERT INTO customers SELECT * FROM tmp; \
                DROP TABLE tmp;')
        connection.execute(sql)
        engine.dispose()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
