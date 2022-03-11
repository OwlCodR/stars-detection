from astroquery.simbad import Simbad
import astropy.coordinates as coord
import astropy.units as u
import psycopg2
from postgres_config import user, password, host, port
from time import time
import warnings


'''
Adds objects types to Postgres table from Simbad
'''


def main():
    warnings.filterwarnings('ignore') # @TODO Filter 
    
    TABLE_NAME = 'stars2'
    CHUNK_SIZE = 10000
    
    START_INDEX = 20000
    END_INDEX = 500000
    
    rows_count = END_INDEX - START_INDEX
    
    customSimbad = Simbad()
    customSimbad.TIMEOUT = 5000
    customSimbad.add_votable_fields('otype')
    customSimbad.remove_votable_fields('main_id', 'coordinates')

    print('Connecting to postgres...')
    con = psycopg2.connect(user=user, password=password, host=host, port=port)
    cur = con.cursor()
    print('Done!\n')

    cur.execute(f'SELECT "index", "RAJ2000", "DEJ2000" FROM {TABLE_NAME} WHERE index BETWEEN {START_INDEX} AND {END_INDEX};')

    objects = [] # [[index, raj2000, dej2000], ..]

    print('Loading objects...')
    while True:
        row = cur.fetchone()
        
        if not row:
            break
        
        index = int(row[0])
        raj2000 = float(row[1])
        dej2000 = float(row[2])
                
        objects.append([index, raj2000, dej2000])
    print('Done!\n')
    
    star_counter = 0
    start_time = time()
    
    print('Requesting info...')
    for i in range(0, len(objects), CHUNK_SIZE):
        chunk_objects = objects[i:(i + CHUNK_SIZE)]
        
        objects_ra = [object[1] for object in chunk_objects]
        objects_dec = [object[2] for object in chunk_objects]
        
        print('Loading table...')
                
        table = customSimbad.query_region(coord.SkyCoord(ra=objects_ra, dec=objects_dec, unit=(
            u.deg, u.deg), frame='icrs'), radius=5 * u.arcsec)
        
        print('Done!\n', table)
        
        last_script_number = 0
        for row in table:
            script_number = int(row[1])
            if script_number != last_script_number:
                last_script_number = script_number
                index = objects[i + (script_number - 1)][0]
                
                if row[0] == 'Star':
                    star_counter += 1
                
                sql = f'UPDATE stars2 SET otype=\'{row[0]}\' WHERE index={index};'
                
                # print(sql)
                cur.execute(sql)

        if i % CHUNK_SIZE == 0:
            print('Commiting...')
            con.commit()
            print('Done!\n')
            
            print('Last updated object index is', index)
            
            delta = time() - start_time # Seconds per CHUNK_SIZE 
            
            print('Loading table and commit time is', int(delta), 's')
            print('Time remaining:', int((len(objects) - i) / CHUNK_SIZE * delta), 's')
            
            start_time = time()
                
    print('Done!\n')
    print(star_counter, ' / ', rows_count, ' stars')
    
    cur.close()
    con.close()


if __name__ == "__main__":
    main()