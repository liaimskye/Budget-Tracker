import sqlite3
from sqlite3 import Error

db = sqlite3.connect('data/budget_data')
cursor_ob = db.cursor()

cursor_ob.execute('''
INSERT
INTO users
VALUES(001,'liaim','chidori15')
''')
db.commit()