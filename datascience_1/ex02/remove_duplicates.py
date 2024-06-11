import sqlalchemy


def reset_list(data: list) -> list:
    last = data[-1]
    data_list = []
    data_list.append(last)
    return data_list


def insert_in_db(connection: object, data_list: tuple) -> None:
    values = ''
    for data in data_list:
        if (data[5] == 'None'):
            data = list(data)
            data[5] = '253ac7e2-280a-11ef-8228-d32bf4e3526b'
            data = tuple(data)
        values += str(data) + ", "
    values = values[:-2]
    sql = sqlalchemy.text(f"INSERT INTO customers VALUES {values};")
    connection.execute(sql)


def delete_duplicates(cur: object, connection: object) -> None:
    row = cur.fetchone()
    data_list = []
    count = 0
    while row is not None:
        nxt_row = cur.fetchone()
        if (nxt_row is None):
            data_list.append((str(row[0]), str(row[1]), str(row[2]),
                             str(row[3]), str(row[4]), str(row[5])))
            size = len(data_list)
            insert_in_db(connection, data_list)
            print(f"{count}{size} Done !")
            break

        if (len(data_list) == 100000):
            count += 1
            print(f"{count}00000 lines done.")
            insert_in_db(connection, data_list)
            data_list = reset_list(data_list)

        if (row[1] != nxt_row[1] or row[2] != nxt_row[2] or
            row[3] != nxt_row[3] or row[4] != nxt_row[4] or
                row[5] != nxt_row[5]):
            data_list.append((str(row[0]), str(row[1]), str(row[2]),
                             str(row[3]), str(row[4]), str(row[5])))
            row = nxt_row
        else:
            if (abs(row[0] - nxt_row[0]).total_seconds() > 1):
                data_list.append((str(row[0]), str(row[1]), str(row[2]),
                                 str(row[3]), str(row[4]), str(row[5])))
                row = nxt_row


def main():
    """Main function to test the functions.
    """
    try:
        engine = sqlalchemy.create_engine(
            "postgresql://lcompieg:mysecretpassword@localhost:5432/piscineds")
        connection = engine.connect()

        print("Deleting duplicates....")
        sql_delete = sqlalchemy.text(
            'CREATE TABLE tmp AS SELECT DISTINCT * FROM customers; \
            TRUNCATE TABLE customers;')
        connection.execute(sql_delete)

        print("Get tmp Table....")
        sql_get_tmp = sqlalchemy.text(
            'SELECT * FROM tmp ORDER BY event_type, \
                                        product_id, \
                                        price, \
                                        user_id, \
                                        user_session, \
                                        event_time DESC;')
        cur = connection.execute(sql_get_tmp)

        print("Deleting rest of duplicates....")
        delete_duplicates(cur, connection)
        connection.commit()
        engine.dispose()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
