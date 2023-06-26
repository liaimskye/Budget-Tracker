import sqlite3
from sqlite3 import Error
from modules import menu
from modules import *
from random import randint

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


# in option selecton tree, create an add user option that calls the user class and store user function
# create checks to ensure username/ids dont already exist to avoid duplicates

# user creation loop
# get existing user credentials for checking of duplicates
existing_id,existing_username,existing_password = existing_books()

while True:
    ids = randint(10000,99999)
    if ids not in existing_id:
        username = input("Enter username: ")
        if username not in existing_username:
            password = input("Enter password: ")
            user = User(ids,username,password)
            user.store_info()
            break
        else:
            print("Username already in use")
            break



cursor_ob.execute('''
SELECT *
FROM users
''')
print(cursor_ob.fetchall())


""" id,username,password = existing_books()


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
            user_id = id[index]
            print(user_id)
            print(type(user_id))
            break

        else:
            print("incorrect password")
            continue




while True:
    selection = menu()
    if selection == '1':
        cursor_ob.execute("SELECT * FROM account WHERE id =?",(user_id,))
        for row in cursor_ob:
            print(row)
        
    elif selection == '2':
        current_total = 0
        new_expense = int(input("Enter total expense: "))
        cursor_ob.execute("SELECT expenses FROM account WHERE id=?",(user_id,))
        for row in cursor_ob:
            current_total = row
        new_total = current_total + new_expense
        print(new_total)
        cursor_ob.execute("UPDATE account SET expenses=? WHERE id=?",(new_total,user_id))
        db.commit()
         """