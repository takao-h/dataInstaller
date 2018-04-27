# coding: utf-8
from urllib.parse import urlparse
import mysql.connector

url = urlparse('mysql://user:pass@localhost:3306/test_for_py')

config = {
  'user': 'root',
  'password': 'root',
  'host': 'localhost',
  'database': 'test_for_py',
}
cnx = mysql.connector.connect(**config)
cur = cnx.cursor(buffered=True)
cur.execute("SHOW STATUS LIKE 'Uptime'")
print(cur.fetchone())
# => ('Uptime', '22073875')

stm = "select * from test"
cur.execute(stm)
print(cur.fetchone())

# => True
cnx.close()
