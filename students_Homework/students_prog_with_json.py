import json
from flask import Flask, request

#save and load functions:
my_file = "students.json"

def load_all():
    try:
        with open (my_file, "r") as f:
            return json.load(f)
    except:
        []

def save_all():
    with open (my_file, "w") as f:
        json.dump(my_data, f)

#program:       
app = Flask(__name__)
my_data = load_all()

#EndPoint read (read- get) , homepage
@app.route ("/")
def homepage():
    return '<h1>welcome to our homepage, please type your method in the URL </h1>'

#EndPoint read (read- get), data
@app.route ("/data/")
@app.route ("/data/<index>")
def show_data(index=-1):
    if int(index) < 0:
        return my_data
    else: 
        return my_data[int(index)]

#EndPoint add (create- post), data
@app.route("/add/", methods = ['POST'])
def add_student():
    data = request.json
    my_data.append({"name":data['name'], "age": data['age']})
    save_all()
    return 'student added'

#EndPoint update (update- Put), data
@app.route("/upd/<index>", methods= ['PUT'])
def update_student(index=-1):
    if int(index) > -1:
        data = request.json
        my_data[int(index)] = ({"name":data['name'], "age":data['age']})
    save_all()
    return 'student update'

#EndPoint delete (delete- delete), data
@app.route("/del/<index>", methods=['DELETE'])
def delete_student(index=-1):
    if int(index) > -1:
        my_data.pop(int(index))
    save_all()
    return 'student delete'


app.run(debug=True)