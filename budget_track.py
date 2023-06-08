import sqlite3
from sqlite3 import Error
from modules import menu
from modules import existing_books

db = sqlite3.connect('data/budget_data')
cursor_ob = db.cursor()

try:
    cursor_ob.execute('''
    CREATE TABLE users(id INTEGER,name TEXT, password CHAR)
    ''')
except Error as e:
    pass

try:
    cursor_ob.execute('''
    CREATE TABLE account(id INTEGER,month TEXT PRIMARY KEY,balance INTEGER,intended_savings INTEGER,expenses INTEGER, FOREIGN KEY(id) REFERENCES users (id))
    ''')
except Error as e:
    pass

id,username,password = existing_books()


index = None
while True:
    login = input("enter your username: ")
    for i in range(len(username)):
        if login == username[i]:
            index = i
    if index == None:
        print("invalid username")
        continue
    else:
        pass_check = input("Enter password: ")
        if pass_check == password[index]:
            print("Logged in")
            break

        else:
            print("incorrect password")
            continue


selection = menu()

while True:
    if selection == '1':
        cursor_ob.execute('''
        SELECT *
        FROM account
        WHERE id = 
        ''')
        
