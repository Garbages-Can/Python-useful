import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='hello')

cur = conn.cursor()

try:
    cur.execute('SELECT * FROM test.users')
    print(cur.fetchall())
finally:
    cur.close()
    conn.close()
