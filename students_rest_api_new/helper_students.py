import sqlite3

from flask import request

#connect the prog into the db:
con = sqlite3.connect('students.db', check_same_thread=False)
cur = con.cursor()
# cur.execute("create TABLE students_details(studentNAME ,studentAGE)")

#create
def add_to_db():
    data= request.json
    cur.execute(f"insert into students_details (studentNAME ,studentAGE) VALUES ('{data['name']}', '{data['age']}')")
    con.commit()