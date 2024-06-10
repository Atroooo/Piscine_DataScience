import sqlalchemy


def main():
    """Main function to test the functions.
    """
    try:
        engine = sqlalchemy.create_engine(
            "postgresql://lcompieg:mysecretpassword@localhost:5432/piscineds")
        connection = engine.connect()
        sql = sqlalchemy.text(
            'CREATE TABLE tmp AS SELECT DISTINCT * FROM customers; \
                DROP TABLE customers; \
                ALTER TABLE tmp RENAME TO customers;')
        print("Deleting duplicates...")
        connection.execute(sql)
        print("Done")
        connection.commit()
        engine.dispose()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
