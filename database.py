import sqlite3
from hash import hashed

def con():
    return sqlite3.connect('markaz.db')

def create_table_user():
    conn=con()
    cur=conn.cursor()
    cur.execute("""
            create table if not exists user(
                id integer not null primary key autoincrement,
                first_name varchar(30),
                last_name varchar(30),
                birth_day data,
                phone varchar(13),
                username varchar(50),
                password varchar(150),
                is_admin boolean default false
            )              
    """)
    conn.commit()
    conn.close()

def insert_user():
    first_name=input('First name: ')
    last_name=input('Last name: ')
    birth_day=input('Birth day(YYYY:MM:D): ')
    phone=input('Phone: ')
    username=input('Usrename: ')
    password=input('Password: ')
    password=hashed(password)

    data=dict(
        first_name=first_name,
        last_name=last_name,
        birth_day=birth_day,
        phone=phone,
        username=username,
        password=password
    )

    conn =con()
    cur=conn.cursor()
    query =("""
        insert into user(
            first_name,
            last_name,
            birth_day,
            phone,
            username,
            password
        )values
            (?,?,?,?,?,?)
    """)
    values=tuple(data.values())
    cur.execute(query, values)
    conn.commit()
    conn.cursor()


def is_exists(username, password):
    conn=con()
    cur=conn.cursor()
    cur.execute(f"""
        select id, username, password, is_admin from user
    """)
    isThere=cur.fetchone()
    return isThere

    

# data=dict(
#     first_name=input('First name: '),
#     last_name=input('Last name: '),
#     birth_day=input('Birth day(YYYY:MM:D): '),
#     phone=input('Phone: '),
#     username=input('Usrename: '),
#     password=input('Password: '),
#     is_admin =False 
#     )






# foreign key(music_id)
# references music(id)

# . userID – butun tipli son(primary key);
# 	2. first_name – tekst, maksimal uzunligi 30;
# 	3. last_name – tekst, maksimal uzunligi 30;
# 	4. birth_day – sana, YYYY-MM-DD formatida(administrator uchun majburiy emas);
# 	5. phone – tekst, maksimal uzunligi 13(+ belgisi bilan birga)
# 	6. username – tekst, maksimal uzunligi 50;
# 	7. password – tekst, maksimal uzunligi 150
# 	8. is_admin – mantiqiy(boolean), agar foydalanuvchi administrator bo’lsa true, aks xolda false 	    qiymatlarni qabul qiladi


#    sha256 = hashlib.sha256()
#     sha256.update(password.encode('utf-8'))
#     hashed_password = sha256.hexdigest()