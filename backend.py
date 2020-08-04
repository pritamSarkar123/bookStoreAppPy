import sqlite3
def connect_to_db():
    connect=sqlite3.connect("books.db")
    cursor=connect.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,title TEXT,author TEXT,year INTEGER,isbn INTEGER);")
    connect.commit()
    connect.close()

def insert(title,author,year,isbn):
    connect=sqlite3.connect("books.db")
    cursor=connect.cursor()
    cursor.execute("INSERT INTO book VALUES(NULL,?,?,?,?);",(title,author,year,isbn))
    connect.commit()
    connect.close()

def view():
    connect=sqlite3.connect("books.db")
    cursor=connect.cursor()
    cursor.execute("SELECT * FROM book;")
    books=cursor.fetchall()
    connect.close()
    return books

def search(title="",author="",year=0,isbn=0):
    connect=sqlite3.connect("books.db")
    cursor=connect.cursor()
    cursor.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?;",(title,author,year,isbn))
    books=cursor.fetchall()
    connect.close()
    return books

def delete(id):
    connect=sqlite3.connect("books.db")
    cursor=connect.cursor()
    cursor.execute("DELETE FROM book WHERE id=?",(id,))
    connect.commit()
    connect.close()

def update(id,title,author,year,isbn):
    connect=sqlite3.connect("books.db")
    cursor=connect.cursor()
    cursor.execute("UPDATE book SET title=?,author=?,year=?,isbn=? WHERE id=?;",(title,author,year,isbn,id))
    connect.commit()
    connect.close()
