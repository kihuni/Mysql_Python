import MySQLdb

db = MySQLdb.connect(host = 'localhost', user='stevo', passwd='password', db = 'giraffe')
cur = db.cursor()

cur.execute("SELECT * FROM  student")
rows = cur.fetchall()

for row in rows:
	for col in row:
		print("%s," % col)
	print("\n")
cur.close()
db.close()
