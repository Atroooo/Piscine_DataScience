import sqlalchemy


def main():
    """Main function to test the functions.
    """
    try:
        engine = sqlalchemy.create_engine(
            "postgresql://lcompieg:mysecretpassword@localhost:5432/piscineds")
        connection = engine.connect()
        sql = sqlalchemy.text(
            'SELECT * \
            FROM customers \
            ORDER BY event_time DESC; \
            ALTER TABLE customers \
            RENAME TO customers_base;'
        )
        connection.execute(sql)
        sql = sqlalchemy.text(
            'SELECT * \
            INTO customers \
            FROM item \
            FULL OUTER JOIN customers_base \
            ON customers_base.product_id = item.product_id;'
        )
        connection.execute(sql)
        engine.dispose()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
