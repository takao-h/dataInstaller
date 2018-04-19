# coding: utf-8
import csv

with open('/Users/k00121/Desktop/【Buzz】社員情報一覧/社員名簿-表1.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    #header = next(reader)  # ヘッダーを読み飛ばしたい時
    for row in spamreader:
        print(', '.join(row))
