import sqlite3
import tabulate

def con():
    return sqlite3.connect('markaz.db')

def create_table_kurs():
    conn=con()
    cur=conn.cursor()
    cur.execute("""
        create table kuslar(
            id integer not null primary key autoincrement,
            name varchar(50),
            number_of_students integer,
            is_active boolean default true
        )
    """)
    conn.commit()
    conn.close()

def insert_kurs():
    data=dict(
        name_of_kurs=input('Enter name of kurs: '),
        number_of_studetts=input('Enter limit of pupils: ')
    )
    conn=con()
    cur=conn.cursor()
    query=("""
        insert into kuslar(
           name,
           number_of_students
        )values
           (?,?)
    """)
    values=tuple(data.values())
    cur.execute(query, values)
    conn.commit()
    conn.close()


def show_kurs():
    conn=con()
    cur=conn.cursor()
    cur.execute("""
        select * from kuslar
    """)
    p=cur.fetchall()
    print(p)



# 1. courseID – butun tipli son(primary key);
# 	2. name – tekst, maksimal uzunligi 50;
# 	3. number_of_students – butun tipli son(kursga qabul qilinadigan o’quvchilar soni)
# 	4. is_active – mantiqiy(boolean), agar kurs aktiv bo’lsa true, aks xolda false qiymatlarni qabul 	  	    qiladi

