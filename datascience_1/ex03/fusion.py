import sqlalchemy


def main():
    """Main function to test the functions.
    """
    try:
        engine = sqlalchemy.create_engine(
            "postgresql://lcompieg:mysecretpassword@localhost:5432/piscineds")
        connection = engine.connect()
        print("Sorting....")
        sql_sort = sqlalchemy.text(
            'SELECT * \
            FROM customers \
            ORDER BY event_time DESC;'
        )
        connection.execute(sql_sort)
        print("Renaming table....")
        sql_rename = sqlalchemy.text(
            'ALTER TABLE customers \
            RENAME TO customers_base;'
        )
        connection.execute(sql_rename)
        print("Merging...")
        sql_merge = sqlalchemy.text(
            'SELECT customers_base.product_id, \
                    customers_base.event_type, \
                    customers_base.price, \
                    customers_base.user_id, \
                    customers_base.user_session, \
                    items.product_id, \
                    items.category_id, \
                    items.category_code, \
                    items.brand \
            INTO customers \
            FROM items \
            FULL OUTER JOIN customers_base \
            ON customers_base.product_id = items.product_id;'
        )
        connection.execute(sql_merge)
        print("Done")
        connection.commit()
        engine.dispose()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
