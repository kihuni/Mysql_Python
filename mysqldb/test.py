import MySQLdb

db = MySQLdb.connect(host = 'localhost', user='stevo', passwd='password', db = 'giraffe')
cur = db.cursor()

try:
	cur.execute("SELECT * FROM  student")
	rows = cur.fetchall()
except (MySQLdb.Error, e):
	try:
		print("MySQL Error [%d]: %s" % (e.args[0], e.args[1])

	except:
		p
for row in rows:
	for col in row:
		print("%s," % col)
	print("\n")
cur.close()
db.close()
