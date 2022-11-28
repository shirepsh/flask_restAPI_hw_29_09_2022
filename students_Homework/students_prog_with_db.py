from flask import Flask, request
import sqlite3

#connect to the db
con = sqlite3.connect("students.db", check_same_thread=False) 
cur = con.cursor()

#create table
# cur.execute("create TABLE students_details(name ,age)")

#program:       
app = Flask(__name__)

#EndPoint read (action read // method get) , homepage
@app.route ("/")
def homepage():
    return '<h1>welcome to our homepage, please type your method in the URL </h1>'

my_data = []
#EndPoint read (action read // method get) all data
@app.route ("/data/")
def show_all_data():
    data = cur.execute("select * from students_details")
    rows = data.fetchall()
    for row in rows :
        my_data.append({"name":row[0]})
    return my_data

#EndPoint read (action read // method get) with param
@app.route ("/data/<name_2_serach>")
def show_data(name_2_serach):
    data = cur.execute(f"select * from students_details where name = '{name_2_serach}'")
    rows = data.fetchall()
    if len(rows) != 0:
        return rows
    else: 
        res = cur.execute("SELECT * From students_details")
        res_new = res.fetchall()
        return res_new

#EndPoint add (action create // method post)
@app.route("/add/", methods = ['POST'])
def add_2_db():
    data= request.json
    cur.execute(f"insert into students_details (name ,age) VALUES ('{data['name']}', '{data['age']}')")
    con.commit()
    return 'student added'

#EndPoint update (action update // method Put)
@app.route("/upd/<name_2_upd>", methods= ['PUT'])
def update_student(name_2_upd):
    data = cur.execute (f"select * from students_details where name = '{name_2_upd}'")
    rows = data.fetchall()
    if len(rows) != 0:
        data_2_upd = request.json
        cur.execute(f" update students_details set name = '{data_2_upd['name']}', age = '{data_2_upd['age']}'  where name = '{name_2_upd}' ")
        con.commit()
        return 'student update'
    else:
        return 'student not found'

#EndPoint delete (action delete // method delete)
@app.route("/del/<name_2_del>", methods=['DELETE'])
def delete_from_db(name_2_del):
    data = cur.execute (f"select * from students_details where name = '{name_2_del}' ")
    rows = data.fetchall()
    if len(rows) != 0:
        cur.execute(f"delete from students_details where name = '{name_2_del}'")
        con.commit()
        return 'student delete'
    else:
        return 'student not found'
    

app.run(debug=True)