import sqlite3
from sqlite3 import Error


def sql_connection():  #establish conection
    try:
        conn=sqlite3.connect('Sales2.db')#creat and open existing data_base
        return conn
    except Error:
        print("error")

def sql_table(conn):
    cursor_obj = conn.cursor()
    # cursor_obj.execute("CREATE TABLE salesman(salesman_id int(5),name char(30),city char(30),commission decimal(7,2));")
    # cursor_obj.executescript("""
    # INSERT INTO salesman VALUES(5002,'ASHOK0','JALANDHAR0',5.09);
    # INSERT INTO salesman VALUES(5003,'ASHOK1','JALANDHAR1',6.09);
    # INSERT INTO salesman VALUES(5004,'ASHOK2','JALANDHAR2',7.09);
    # INSERT INTO salesman VALUES(5005,'ASHOK3','JALANDHAR3',8.09);
    # """)
    # conn.commit()#store the data permanently
    cursor_obj.execute("SELECT *FROM salesman")
    rows=cursor_obj.fetchall()#all the recond in the salesman table
    print("agent detail")
    for data in rows:
        print(data)

    return cursor_obj

def update(conn):
    cursor_obj = conn.cursor()
    cursor_obj.execute('''UPDATE salesman SET salesman_id = 5000 WHERE commission=5.09;''')
    print('\nAfter Updating...\n')
    cursor_obj.execute("SELECT *FROM salesman")
    rows = cursor_obj.fetchall()  # all the recond in the salesman table
    print("agent detail")
    for data in rows:
        print(data)

def deletee(conn):
    cursor_obj = conn.cursor()
    cursor_obj.execute('''DELETE FROM salesman WHERE COMMISSION=7.09;''')
    print('\nAfter deleting...\n')
    cursor_obj.execute("SELECT *FROM salesman")
    rows = cursor_obj.fetchall()  # all the recond in the salesman table
    print("agent detail")
    for data in rows:
        print(data)

def count_1(conn):
    cursor_Obj = conn.cursor()
    cursor_Obj.execute('SELECT * FROM salesman;')
    print(len(cursor_Obj.fetchall()))



sqlite_conn = sql_connection()
sql_table(sqlite_conn)
update(sqlite_conn)
# deletee(sqlite_conn)
count_1(sqlite_conn)
if (sqlite_conn):
    sqlite_conn.close()
    print("connection got closed")
