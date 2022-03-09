import csv
import psycopg2
from postgres_config import user, password, host, port

def create_table(cur, columns):
    sql = """CREATE TABLE stars (
            id bigserial primary key,"""

    for i in range(len(columns)):
        if '"' + list(columns)[i] + '"' in sql:
            sql += '\"' + list(columns)[i] + '_1\" text,\n'
        else:
            sql += '\"' + list(columns)[i] + '\" text,\n'
    sql = sql[:-2]
    sql += ');'
    print(sql)

    cur.execute(sql)

def get_not_empty_columns(reader):
    not_empty_columns = set(range(0, len(columns)))
    empty_columns = set(range(0, len(columns)))
    for row in reader:
        for i in range(len(row)):
            if len(row[i]) != 0 and i in empty_columns:
                empty_columns.remove(i)
        if len(empty_columns) == 25:
            break
    return not_empty_columns - empty_columns


def isTableExists(cur, table_name):
    cur.execute(f'SELECT * FROM information_schema.tables where table_name=\'{table_name}\'')
    return bool(cur.rowcount)


def getLastId(cur):
    cur.execute('SELECT max(id) FROM stars')
    last_id = cur.fetchone()[0]
    print('Last Id: ', last_id)
    return last_id
        

def main():
    CSV_PATH = "datasets/APASSDR9_GALEXGR6PLUS7AIS.csv"
    
    with open(CSV_PATH, "r") as f_obj:
        reader = csv.reader(f_obj)
        arr = next(reader)
        columns = list(arr)

        print(columns)
        print('Columns count: ', len(columns))

        # not_empty_columns = get_not_empty_columns(reader)

        # print('Not empty: ', not_empty_columns)
        # print('not_empty_columns count: ', len(not_empty_columns))

        con = psycopg2.connect(user=user, password=password, host=host, port=port)
        cur = con.cursor()

        if not isTableExists(cur, 'stars'):
            create_table(cur, columns)

        sql = 'INSERT INTO stars ('

        for col in columns:
            if '"' + col + '"' in sql:
                sql += '\"' + col + '_1\"' + ', '
            else:
                sql += '\"' + col + '\"' + ', '
        sql = sql[:-2] + ') VALUES %s;'

        counter = getLastId(cur)
        for row in reader:
            try:
                cur.execute(sql, (tuple(row),))
            except:
                counter += 1
                continue
            else:
                counter += 1
                if counter % 100 == 0:
                    print(counter)
                if counter % 10000 == 0:
                    con.commit()

        cur.close()
        con.close()

if __name__ == "__main__":
    main()

# for resource in votable.resources:
#     for table in resource.tables:
#         print(table.names)


# Определить, является ли звезда переменной
# 1. Собрать датасет
# - 
# 2. Обучить на датасете

# Кривая блеска звезды — функция изменения блеска астрономического объекта во времени
# HD 200466B
# Object classification in SIMBAD
#   ·  V*    	                V*     	Variable Star
#   ·  ·  Irregular_V*    	    Ir*    	Variable Star of irregular type
#   ·  ·  ·  Orion_V*    	    Or*    	Variable Star of Orion Type
#   ·  ·  Eruptive*    	        Er*    	Eruptive variable Star
#   ·  ·  ·  Erupt*RCrB    	    RC*    	Variable Star of R CrB type
#   ·  ·  ·  RCrB_Candidate    	RC?    	Variable Star of R CrB type candiate
#   ·  ·  RotV*    	            Ro*    	Rotationally variable Star
#   ·  ·  ·  RotV*alf2CVn    	a2*    	Variable Star of alpha2 CVn type
#   ·  ·  ·  Pulsar    	        Psr    	Pulsar
#   ·  ·  ·  BYDra    	        BY*    	Variable of BY Dra type    
#   ·  ·  ·  RSCVn    	        RS*    	Variable of RS CVn type    
#   ·  ·  PulsV*    	        Pu*    	Pulsating variable Star    
#   ·  ·  ·  RRLyr    	        RR*    	Variable Star of RR Lyr type    
#   ·  ·  ·  Cepheid    	    Ce*    	Cepheid variable Star    
#   ·  ·  ·  PulsV*delSct    	dS*    	Variable Star of delta Sct type    
#   ·  ·  ·  PulsV*RVTau    	RV*    	Variable Star of RV Tau type    
#   ·  ·  ·  PulsV*WVir    	    WV*    	Variable Star of W Vir type    
#   ·  ·  ·  PulsV*bCep    	    bC*    	Variable Star of beta Cep type    
#   ·  ·  ·  deltaCep    	    cC*    	Classical Cepheid (delta Cep type)    
#   ·  ·  ·  gammaDor    	    gD*    	Variable Star of gamma Dor type    
#   ·  ·  ·  pulsV*SX    	    SX*    	Variable Star of SX Phe type (subdwarf)    
#   ·  ·  LPV*    	            LP*    	Long-period variable star    
#   ·  ·  ·  Mira    	        Mi*    	Variable Star of Mira Cet type    
#   ·  ·  SN    	            SN*    	SuperNova    
#   ·  Sub-stellar    	        su*    	Sub-stellar object    
#   ·  ·  Planet?    	        Pl?    	Extra-solar Planet Candidate    
#   ·  ·  Planet    	        Pl     	Extra-solar Confirmed Planet   