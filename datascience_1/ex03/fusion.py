import sqlalchemy


def main():
    """Main function to test the functions.
    """
    try:
        engine = sqlalchemy.create_engine(
            "postgresql://lcompieg:mysecretpassword@localhost:5432/piscineds")
        connection = engine.connect()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
