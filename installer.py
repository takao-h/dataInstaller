# coding: utf-8
import csv
from urllib.parse import urlparse
import mysql.connector

url = urlparse('mysql://user:pass@localhost:3306/test_for_py')
filepath = '/Users/k00121/Desktop/【Buzz】社員情報一覧/社員名簿-表1.csv'
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


with open(filepath, 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    header = next(spamreader)  # ヘッダーを読み飛ばしたい時
    for row in spamreader:
        print(', '.join(row))
        cur.execute('INSERT INTO test VALUES (%s, "%s")' % tuple(row))
cur.commit()
