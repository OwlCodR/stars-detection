from astroquery.simbad import Simbad
import astropy.coordinates as coord
import astropy.units as u
import psycopg2
from postgres_config import user, password, host, port

def main():
    customSimbad = Simbad()
    customSimbad.add_votable_fields('otype')

    conn = psycopg2.connect(user=user, password=password,
                            host=host, port=port)
    cur = conn.cursor()

    cur.execute('SELECT min(id) FROM stars WHERE type is NULL')
    min_id = cur.fetchone()[0]

    # min_id = 1

    cur.execute(f'SELECT "RAJ2000", "DEJ2000" FROM stars WHERE id > {min_id};')
    rows = cur.fetchall()

    object_number = 0
    main_id = 0

    id_index = 0

    chunk_size = 10

    RAJs = []
    DEJs = []

    for i in range(len(rows)):
        RAJs.append(float(rows[i][0]))
        DEJs.append(float(rows[i][1]))

        if i % chunk_size == 0 and i != 0:
            tables = []

            for j in range(len(RAJs)):
                print(f'Checking {RAJs[j]}, {DEJs[j]}...')
                table = Simbad.query_region(coord.SkyCoord(
                    ra=RAJs[j], dec=DEJs[j], unit=(u.deg, u.deg), frame='icrs'), radius=2 * u.arcmin)
                tables.append(table)
                print(f'Found ', table)

            types_tables = customSimbad.query_objects(
                [table[object_number][main_id] if table is not None else '' for table in tables])
            for j in range(len(types_tables)):
                if types_tables[j] is None:
                    continue

                otype = types_tables[j]['OTYPE']
                simbad_name = types_tables[j]['MAIN_ID']

                if i - chunk_size + j + 1 < len(rows):
                    cur.execute(
                        f'UPDATE stars SET type = \'{otype}\', \"simbadName\" = \'{simbad_name}\' WHERE id = {rows[i - chunk_size + j + 1][id_index]}')

                    print(simbad_name)
                    print(i - chunk_size + j + 1)
                    print(rows[i - chunk_size + j + 1][id_index])

            conn.commit()

    cur.close()
    conn.close()
    
if __name__ == "__main__":
    main()