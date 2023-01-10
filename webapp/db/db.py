import mysql.connector

dbconfig = {'host': 's177.cyber-folks.pl',
            'user': 'nnmyhiacdt_rusz_glowa',
            'password': 'Pandi1992cao@',
            'database': 'nnmyhiacdt_rusz_glowa', }

conn = mysql.connector.connect(**dbconfig)

cursor = conn.cursor()

_SQL_ = """insert into logs
            (phrase, letters, ip, browser_string, results)
            values
            (%s, %s, %s, %s, %s)"""

cursor.execute(_SQL_, ('galaktyka', 'tym', '127.0.0.1', 'Opera',"{'t', 'y'}"))

conn.commit()

_SQL = """select * from logs"""

cursor.execute(_SQL)

for row in cursor.fetchall():
    print(row)

cursor.close()

conn.close()