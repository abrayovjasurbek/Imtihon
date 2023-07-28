import sqlite3
from hash import hashed
from database import insert_user, is_exists

def con():
    return sqlite3.connect('markaz.db')

def registr_user():
    insert_user()

def login():
    for i in range(2):
        username=input('Enter username: ')
        password=input('Enter password: ')
        password=hashed(password)
        res=is_exists(username, password)
        if res[1]==username and res[2]==password and res[3]==True:
            return 'admin'
        elif res[1]==username and res[2]==password:
            return [True, res[0]]
    return False

# try:
#         cur.execute(f"""
#             select * from user where username={username} and password ={password}
#         """)
#         p=cur.fetchall()
#     except:
#         print('There is not user that ID')
#         for i in range(2):
#             print('1.Registr\t2.Login')
#             choise=int(input('<<< '))
#             try:
#                 if choise==1:
#                     registr_user()
#                 elif choise==2:
#                     login()
#             except:
#                 raise IndentationError('Dasturni qayta ishga tushiring!!!😔')