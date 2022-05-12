# Copyright (c) 2022 Kandakov Danil (p2034 or the_lll_end)
# https://github.com/p2034

from astroquery.vizier import Vizier
import astropy.coordinates as coord
import astropy.units as u
from astropy.coordinates import Angle
import psycopg2

# data from csv file: 2MASS_APASS.csv

# 0: angDist           0.254301          0.854817          4.489911          
# 1: 2MASS             03005432+0032350  03005432+0032350  03005432+0032350  
# 2: RAJ2000           45.226351         45.226351         45.226351         
# 3: DEJ2000           +0.543061         +0.543061         +0.543061         
# 4: errHalfMaj        0.080             0.080             0.080             
# 5: errHalfMin        0.080             0.080             0.080             
# 6: errPosAng         45                45                45                
# 7: Jmag              15.213            15.213            15.213            
# 8: Hmag              14.841            14.841            14.841            
# 9: Kmag              14.627            14.627            14.627            
# 10: e_Jmag            0.053             0.053             0.053             
# 11: e_Hmag            0.070             0.070             0.070             
# 12: e_Kmag            0.112             0.112             0.112             
# 13: Qfl               AAB               AAB               AAB               
# 14: Rfl               222               222               222               
# 15: X                 0                 0                 0                 
# 16: MeasureJD         2451813.9022      2451813.9022      2451813.9022      
# 17: RAJ2000           45.226295         45.226305         45.226539         
# 18: DEJ2000           0.543104          0.543294          0.541828          
# 19: errHalfMaj        1.042             1.323             1.436             
# 20: errHalfMin        0.915             1.062             0.728             
# 21: errPosAng         0                 0                 0                 
# 22: field             20110018          20110018          20110018          
# 23: nobs              33                8                 2                 
# 24: mobs              102               16                2                 
# 25: B-V               0.720                                                 
# 26: e_B-V             0.128                                                 
# 27: Vmag              16.592            16.619                              
# 28: e_Vmag            0.078             0.118                               
# 29: u_e_Vmag          0                 1                                   
# 30: Bmag              17.312                                                
# 31: e_Bmag            0.101                                                 
# 32: u_e_Bmag          0                                                     
# 33: gpmag             16.944                                                
# 34: e_gpmag           0.041                                                 
# 35: u_e_gpmag         0                                                     
# 36: rpmag             16.423                                                
# 37: e_rpmag           0.055                                                 
# 38: u_e_rpmag         0                                                     
# 39: ipmag             16.294                                                
# 40: e_ipmag           0.231                                                 
# 41: u_e_ipmag



# just start it, it does NOT break something
def parse_csv(strings_count):
  CSV_PATH = '/Users/danilkandakov/Desktop/projects/starset/2MASS_APASS.csv'

  arr=[['0' for i in range(42)]  for i in range(strings_count)] 
  count = 0
  
  with open(CSV_PATH, 'r') as f:
    i = 0
    for line in f:
      harr = line.split(',')
      print(f'split {i} string, count of objects: {len(harr)}')
      arr[i] = harr
      if i == 0:
        count = len(arr[0])
      if i == strings_count - 1:
        break
      i+=1
  
  print(count)
  for i in range(count):
    print(f'{i}: ', end="")
    for j in range(strings_count):
      print(f"{arr[j][i]:<17} ", sep="; ", end="")
    print(end="\n")



def parse_into_db():
  CHUNK_SIZE = 10000
  CSV_PATH = '/Users/danilkandakov/Desktop/projects/starset/2MASS_APASS.csv'
  FIELDS_COUNT = 42 + 0 # 42 in csv file, 0 in vsx
  table_name = "sky_2MASS_APASS_01_with_VSX_type"

  # init postgres connection
  con = psycopg2.connect(
    dbname='star_db',
    user='star_admin',
    password='stars',
    host='localhost')
  cur = con.cursor()

  arr=[['' for i in range(FIELDS_COUNT)] for i in range(CHUNK_SIZE)]

  # init vsx connection
  v = Vizier(columns=['Type', 'Name', 'min', 'max', 'n_max', 'f_min', 'V', 'Period'])
  v.TIMEOUT = 5000
  objects = []
  
  with open(CSV_PATH, 'r') as f:
    line = f.readline() # skip first line with fields names

    # iterations on every object in csv file
    while True:
      # we use this limitation for preventing ddos attack :) on vizier
      objects_count = 0
      for i in range(CHUNK_SIZE):
        if not line: # if this is the end
          break
        arr[i] = f.readline().split(',')
        objects_count+=1
      
      # every chunk we will talk with visiers
      # create ra & dec arrays
      objects_ra = [float(arr[i][2]) for i in range(objects_count)]
      objects_dec = [float(arr[i][3]) for i in range(objects_count)]
      # get objects from vsx around our objects
      result = v.query_region(coord.SkyCoord(
        ra=objects_ra, dec=objects_dec, unit=(u.deg, u.deg), frame='icrs'),
        radius=5 * u.arcsec, catalog='B/vsx')

      print("result:\n", result)
      print("result:\n", result[0][0])
      print("result:\n", result[0][0][0])
      
      break

      # if we are not able to create full chunk (this is the end of file)
      if objects_count < CHUNK_SIZE:
        break

      
      # cur.execute(
      #   f'''INSERT INTO "{table_name}" ("angDist", "RAJ2000", "DEJ2000",
      #   "Jmag", "Hmag", "Kmag", "e_Jmag", "e_Hmag", "e_Kmag",
      #   "nobs", "mobs",
      #   "B-V", "e_B-V", "Vmag", "e_Vmag", "Bmag", "e_Bmag", 
      #   "gpmag", "e_gpmag", "rpmag", "e_rpmag", "ipmag", "e_ipmag")
      #   VALUES ({arr[0]:.6f}, {arr[2]:.6f}, {arr[3]:.6f}, 
      #   {arr[7]:.3f}, {arr[8]:.3f}, {arr[9]:.3f}, {arr[10]:.3f}, {arr[11]:.3f}, {arr[12]:.3f},
      #   {arr[7], arr[7]})''', ()
      # )



if __name__ == "__main__":
  parse_into_db()