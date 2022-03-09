import psycopg2
import pandas
from sqlalchemy import create_engine
from postgres_config import user, password, host, port


def isTableExists(cur, table_name):
    cur.execute(
        f'SELECT * FROM information_schema.tables where table_name=\'{table_name}\'')
    return bool(cur.rowcount)


def main():
    CSV_PATH = 'C:\Download\APASSDR9_GALEXGR6PLUS7AIS.csv'
    TABLE_NAME = 'stars2'

    con = psycopg2.connect(
        user=user, password=password, host=host, port=port)

    df = pandas.read_csv(CSV_PATH)

    engine = create_engine(
        f'postgresql://{user}:{password}@{host}:{port}/postgres')
    df.to_sql(TABLE_NAME, engine)

    con.close()


if __name__ == "__main__":
    main()
