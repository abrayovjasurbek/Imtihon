import sqlite3

def con():
    return sqlite3.connect('markaz.db')

def create_table_yozilganlar():
    conn=con()
    cur=conn.cursor()
    cur.execute("""
            create table if not exists yozilganlar(
                id integer not null primary key autoincrement,
                user_id integer,
                kurs_id integer
            )              
    """)
    conn.commit()
    conn.close()


def insert_yozilganlar(data:dict):
    conn =con()
    cur=conn.cursor()
    query =("""
        insert into yozilganlar(
            foreign key(user_id)
            references user(id),
            foreign key(kurs_id)
            references kurslar(id)
        )values
            (?,?)
    """)
    values=tuple(data.values())
    cur.execute(query, values)
    conn.commit()
    conn.cursor()


def show_yozilganlar():
    conn=con()
    cur=conn.cursor()
    cur.execute("""
        select * from yozilganlar
    """)
    p=cur.fetchall()
    print(p)

def yozilgankurs(id):
    conn=con()
    cur=conn.cursor()
    cur.fetchall(f"""
        select * from where id={id}
    """)
    return cur.fetchall()

def is_active_kurs():
    conn=con()
    cur=conn.cursor()
    cur.fetchall("""
        select count(id) from yozilganlar
    """)