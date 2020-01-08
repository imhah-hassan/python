import pymysql
conn = pymysql.connect(host='localhost', user='root', passwd=None, db='mysql')
cur = conn.cursor()
cur.execute("SELECT Host,User FROM user")
for r in cur:
    print(r)
cur.close()
conn.close()
