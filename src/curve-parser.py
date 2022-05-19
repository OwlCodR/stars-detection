# Copyright (c) 2022 Kandakov Danil (p2034 or the_lll_end)
# https://github.com/p2034

from astropy.coordinates import SkyCoord
import astropy.units as u
import lightkurve as lk
# from astroquery.mast import Observations
# from astroquery.mast import Catalogs

# disable logging for lightkurve
import logging; logging.disable(logging.CRITICAL)
lk.log.disabled = True

import time
import os
import sys

import psycopg2

# matplot lib init
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('MacOSX')
matplotlib.rcParams['interactive'] == True

# psql inserting
BLOCK_SIZE = 4
ROWS_COUNT = 10

# indexes in table's rows
OID_INDEX = 0
RADEG_INDEX = 2
DEDEG_INDEX = 3

# lightkurve searching parameters
ARCSEC_RADIUS = 5

def show_lc_plot(lc):
  period = lc.to_periodogram("ls").period_at_max_power
  # lc.plot() # print graph
  lc.fold(period).plot() # print period of graph
  plt.show()

def show_lc_table(lc):
  print(lc)

def star_table_processor(star_table):
  lc = star_table[0].download()
  show_lc_table(lc)
  show_lc_plot(lc)

# start_index from 1
def parse_db(start_index, last_index):
  table_name = "vsx_dat_stars"

  print('Connecting to postgres...')
  con = psycopg2.connect(
    user="star_admin",
    password="stars",
    host="localhost",
    port=5432,
    database="star_db")
  cur = con.cursor()
  print('Done!')

  # go through the table
  current_count = 0
  block_ids = []
  for i in range(start_index, last_index):
    try:
      # get row from db
      cur.execute(f'SELECT oid, name, radeg, dedeg FROM {table_name} WHERE id = {i};')
      row = cur.fetchone()
      if not row:
        break

      # request objects on special distance
      star_table = lk.search_lightcurve(
        SkyCoord(
          ra=row[RADEG_INDEX],
          dec=row[DEDEG_INDEX],
          unit="deg"),
        radius = u.arcsec * ARCSEC_RADIUS)

      # append new row, if it is normal
      if len(star_table) > 0:
        block_ids.append(i)
        current_count += 1
        print(i, ": ", star_table[0].distance)
        star_table_processor(star_table)

      # if block is full => commit changes in psql
      if (current_count == BLOCK_SIZE) or (i == last_index - 1):
        print(block_ids)
        block_ids = []
        current_count = 0
        # cur.execute(
        #   f'''UPDATE {table_name} SET function={1} WHERE id = {i};''', ()
        # )
    except Exception as err:
      print(err)
      return i

    # remove lightkurve cache
    os.system('rm -rf ~/.lightkurve-cache')

  return 0

if __name__ == "__main__":
  if len(sys.argv) < 3:
    print("Not enough arguments.")
    exit(0)

  start_time = time.time()
  last_index = parse_db(int(sys.argv[1]), int(sys.argv[2]) + 1)
  print(f'{time.time() - start_time} seconds in {ROWS_COUNT} stars')

  if last_index != 0:
    print("Error, parsed: from", sys.argv[1], "to", last_index, ", error on:", last_index)
  else:
    print("Parsed: from", sys.argv[1], "to", sys.argv[2])