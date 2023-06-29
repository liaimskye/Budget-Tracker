import sqlite3
from random import randint

db = sqlite3.connect('data/budget_data')
cursor_ob = db.cursor()


def main_menu(existing_id,existing_username,existing_password):
    selection = input('''
    1. Create user
    2. login
    3. Exit
    ''')
    if selection == '1':
        
        ids = randint(10000,99999)
        if ids not in existing_id:
            username = input("Enter username: ")
            if username not in existing_username:
                password = input("Enter password: ")
                user = User(ids,username,password)
                user.store_info()
                print("User created")
                main_menu(existing_id,existing_username,existing_password)
            else:
                print("Username already in use")
                main_menu(existing_id,existing_username,existing_password)

    if selection == '2':
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
                    user_id = id[index]
                    print(user_id)
                    print(type(user_id))
                    break

                else:
                    print("incorrect password")
                    continue


def menu():
    '''
    - Takes zero arguments
    - Displays menu optons to the user
    - Requests user input on menu selection
    - Returns the selection made 
    '''

    selection = input('''
Select an option below:
1. display info
2. enter expenses
3. update info
0. Exit
: ''')
    return selection


# edit to return id, name, password
def existing_books():
    '''
    - Takes zero arguments.
    - Stores the values of id, Title and Author columns in lists to use for comparison
    '''
    # creates empty lists for the 3 columns
    existing_id = []
    existing_username = []
    existing_password = []


    # selects each records values for the 3 coluns
    cursor_ob.execute('''
    SELECT id, name, password
    FROM users
    ''')

    # appends column data to lists
    for row in cursor_ob:
        existing_id.append(row[0])
        existing_username.append(row[1])
        existing_password.append(row[2])
    
    return existing_id,existing_username,existing_password



class User:
    def __init__(self, ids, username, password):
        self.ids = ids
        self.username = username
        self.password = password
    
    def store_info(self):
        cursor_ob.execute('''
        INSERT INTO users(id,name,password)
        VALUES (?,?,?)
        ''',(self.ids,self.username,self.password))
        db.commit()
