# Copyright (c) 2022 Kandakov Danil (p2034 or the_lll_end)
# https://github.com/p2034

from astropy.coordinates import SkyCoord
import astropy.units as u
import os
from astroquery.mast import Observations
import psycopg2
# import matplotlib
# import matplotlib.pyplot as plt

# matplotlib.use('MacOSX')
# matplotlib.rcParams['interactive'] == True

# lightkurve data getter

BLOCK_SIZE = 2
ROWS_COUNT = 10

# indexes in table's rows
RADEG_INDEX = 3
DEDEG_INDEX = 4

print('Connecting to postgres...')
con = psycopg2.connect(user="star_admin", password="stars", host="localhost", port=5432, database="star_db")
cur = con.cursor()
print('Done!\n')

# run blocks on the table

for i in range(ROWS_COUNT):
  for id in range(i + 1, BLOCK_SIZE + i):
    print("Start block")
    # get row from db
    cur.execute(f'SELECT oid, name, v, radeg, dedeg, type, period FROM vsx_dat_stars WHERE id = {id};')
    row = cur.fetchone()
    # rows.append(row)
    # insert it in block
    lcs = lk.search_lightcurve(SkyCoord(row[RADEG_INDEX], row[DEDEG_INDEX], unit="deg"), u.arcsec * 5)
    print(len(lcs.table))
    if len(lcs.table) > 0:
      lc = lcs[0].download()
      print(lc)

  # work with rows

  # lc = lcs[0].download()
  # rows=[]


# lcs = lk.search_lightcurve(SkyCoord(300.47715, 37.94670, unit="deg"), u.arcsec * 50)

# lc = lcs[0].download()
# print(lc)