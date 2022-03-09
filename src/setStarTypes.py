from astroquery.vizier import Vizier
import astropy.coordinates as coord
import astropy.units as u
from astropy.coordinates import Angle
import psycopg2

from postgres_config import user, password, host, port




'''
Sets stars' type from the VSX

This file sets star's type to the postgres 
table's column "starType"
'''


def main():
    catalog_list = Vizier.find_catalogs('VSX')
    print(f'Catalog_list:\n {catalog_list}')

    vsx = Vizier.get_catalogs(catalog_list.values())[0]
    print(f'VSX:\n {vsx}')

    con = psycopg2.connect(user=user, password=password, host=host, port=port)
    cur = con.cursor()
    cur.execute(
        'SELECT "index", "RAJ2000", "DEJ2000" FROM stars2;')

    v = Vizier(columns=['Type', 'Name'])
    v.TIMEOUT = 5000
    objects = []
    
    CHUNK_SIZE = 1000
    
    while True:
        row = cur.fetchone()
        
        if not row:
            break
        
        index = int(row[0])
        raj2000 = float(row[1])
        dej2000 = float(row[2])
                
        objects.append([index, raj2000, dej2000])
        
    tables = []

    for i in range(0, len(objects), CHUNK_SIZE):
        chunk_objects = objects[i:(i + CHUNK_SIZE)]
        
        objects_ra = [object[1] for object in chunk_objects]
        objects_dec = [object[2] for object in chunk_objects]
        
        result = v.query_region(coord.SkyCoord(ra=objects_ra, dec=objects_dec, unit=(u.deg, u.deg), frame='icrs'),
                                radius=5 * u.arcsec, catalog='B/vsx')
        if result:
            tables.append(result[0])
            print(f'APPEND\n {result[0]}\n')

    # print(f'TABLES {tables}')
    
    for j in range(len(tables)):
        table = tables[j]
        last_q = 0
        for row in table:
            q = row[0]
            if q != last_q:
                last_q = q
                # print(f'UPDATE stars2 SET "starType"="{row[1]}" WHERE index={objects[q + j * CHUNK_SIZE - 1][0]};')
                
                cur.execute(
                    f'UPDATE stars2 SET "starType"={table[i][1]} WHERE id={q + j * CHUNK_SIZE}')

            if i % 1000 == 0:
                print(q + j * CHUNK_SIZE)
                con.commit()

    con.commit()
    
    cur.close()
    con.close()


if __name__ == "__main__":
    main()