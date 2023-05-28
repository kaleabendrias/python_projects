import sqlite3

#create conn

def connect():
    conn=sqlite3.connect('MedicineStore.db')
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS medicine (id INTEGER PRIMARY KEY, title text, numberOfDoses integer)")
    conn.commit()
    conn.close()

def insert(title, numberOfDoses):
    conn = sqlite3.connect('MedicineStore.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO medicine VALUES(NULL,?,?)',(title, numberOfDoses))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect('MedicineStore.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM medicine')
    rows=cur.fetchall()
    conn.close()
    return rows

def search(title="", numberOfDoses=""):
    conn = sqlite3.connect('MedicineStore.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM medicine WHERE title=? OR numberOfDoses=? ", (title, numberOfDoses))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect('MedicineStore.db')
    cur = conn.cursor()
    cur.execute('DELETE FROM medicine WHERE id=?',(id,))
    conn.commit()
    conn.close()




def update(id,title,numberOfDoses):
    conn = sqlite3.connect('MedicineStore.db')
    cur = conn.cursor()
    cur.execute('UPDATE medicine SET title=?,numberOfDoses=? WHERE id=?',(title,numberOfDoses,id,))
    conn.commit()
    conn.close()

def delete_all():
    conn = sqlite3.connect('MedicineStore.db')
    cur = conn.cursor()
    cur.execute('DELETE FROM medicine')
    conn.commit()
    conn.close()

connect()



