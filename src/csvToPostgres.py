# Copyright (c) 2022 OwlCodR (Max)
# https://github.com/OwlCodR

import psycopg2
import pandas
from sqlalchemy import create_engine
from postgres_config import user, password, host, port


'''
Copies all data from CSV to Postgres table
'''


def main():
    CSV_PATH = 'C:\Download\APASSDR9_GALEXGR6PLUS7AIS.csv'
    TABLE_NAME = 'stars2'

    print('Connecting to database...')
    con = psycopg2.connect(
        user=user, password=password, host=host, port=port)
    print('Done!')

    df = pandas.read_csv(CSV_PATH)

    engine = create_engine(
        f'postgresql://{user}:{password}@{host}:{port}/postgres')
    
    print('Parsing into postgres...')
    df.to_sql(TABLE_NAME, engine)
    print('Done!')

    con.close()


if __name__ == "__main__":
    main()
