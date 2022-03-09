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
    cur.execute('SELECT "RAJ2000", "DEJ2000" FROM stars2;')
    rows = cur.fetchall()

    v = Vizier(columns=['Type'])
    v.TIMEOUT = 5000

    RAJs = []
    DEJs = []
    
    while True:
        row = cur.fetchone()
        
        if not row:
            break
        
        RAJs.append(float(row[0]))
        DEJs.append(float(row[1]))

    result = v.query_region(coord.SkyCoord(ra=RAJs, dec=DEJs, unit=(u.deg, u.deg), frame='icrs'), 
                            radius=5 * u.arcsec, catalog='B/vsx')
    table = result[0]

    print(table)

    last_q = 0
    for i in range(len(table)):
        q = table[i][0]
        if q != last_q:
            last_q = q
            cur.execute(f'UPDATE stars2 SET "starType"={table[i][1]}')

        if i % 1000 == 0:
            print(q)
            con.commit()

    con.commit()
    result.pprint()

if __name__ == "__main__":
    main()