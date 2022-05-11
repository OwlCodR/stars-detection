# Copyright (c) 2022 OwlCodR (Max)
# https://github.com/OwlCodR

from astroquery.vizier import Vizier
import astropy.coordinates as coord
import astropy.units as u
from astropy.coordinates import Angle
import psycopg2
import numpy
from postgres_config import user, password, host, port


'''
Sets stars' type from the VSX

This file sets star's type to the postgres 
table's column "starType"
'''


def main():
    print('Connecting to database...')
    con = psycopg2.connect(user=user, password=password, host=host, port=port)
    cur = con.cursor()
    print('Done!')

    cur.execute(
        'SELECT "index", "RAJ2000", "DEJ2000" FROM stars2 WHERE index > 500000;')

    v = Vizier(columns=['Type', 'Name', 'min', 'max', 'n_max', 'f_min', 'V', 'Period'])
    v.TIMEOUT = 5000
    objects = []
    
    CHUNK_SIZE = 10000
    
    print('Loading objects...')
    while True:
        row = cur.fetchone()
        
        if not row:
            break
        
        index = int(row[0])
        raj2000 = float(row[1])
        dej2000 = float(row[2])
                
        objects.append([index, raj2000, dej2000])
    print('Done!')
        
    for i in range(0, len(objects), CHUNK_SIZE):
        chunk_objects = objects[i:(i + CHUNK_SIZE)]
        
        objects_ra = [object[1] for object in chunk_objects]
        objects_dec = [object[2] for object in chunk_objects]
        
        print('Requesting objects...')
        result = v.query_region(coord.SkyCoord(ra=objects_ra, dec=objects_dec, unit=(u.deg, u.deg), frame='icrs'),
                                radius=5 * u.arcsec, catalog='B/vsx')
        print('Done!')
        
        last_q = 0
        for row in result[0]:
            q = row[0]
            if q != last_q:
                last_q = q
                
                period = None
                
                if str(row[8]) != '--':
                    period = row[8]
                
                # print(f'''UPDATE stars2 SET 
                #     "starType"=%s,
                #     "sName"=%s,
                #     "min"=%s,
                #     "max"=%s, 
                #     "n_max"=%s,
                #     "f_min"=%s,
                #     "V"=%s,
                #     "Period"=%s
                #     WHERE index=%s;''',
                #     (
                #         row[1], row[2], float(row[3]), float(row[4]), 
                #         row[5], row[6], int(row[7]), period,
                #         objects[q + i - 1][0]
                #     ))
                
                cur.execute(
                    f'''UPDATE stars2 SET 
                    "starType"=%s,
                    "sName"=%s,
                    "min"=%s,
                    "max"=%s, 
                    "n_max"=%s,
                    "f_min"=%s,
                    "V"=%s,
                    "Period"=%s
                    WHERE index=%s;''',
                    (
                        row[1], row[2], float(row[3]), float(row[4]), 
                        row[5], row[6], int(row[7]), period,
                        objects[q + i - 1][0]
                    )
                )

            if i % 1000 == 0:
                print(i + (q - 1))
                con.commit()

    con.commit()
    
    cur.close()
    con.close()


if __name__ == "__main__":
    main()