import sqlalchemy
import pandas as pd


def main():
    """Main function to test the functions.
    """
    engine = sqlalchemy.create_engine(
            "postgresql://lcompieg:mysecretpassword@localhost:5432/piscineds")
    data = pd.read_sql_query('select * from customers', con=engine)



if __name__ == "__main__":
    main()
