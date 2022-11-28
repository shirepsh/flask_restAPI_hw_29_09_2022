# import json
from flask import Flask,request
from helper_students import *

# #save function
# def save_all(data_file, my_array):
#     with open (data_file, "w") as file:
#         return json.dump(my_array, file, indent=4)

app = Flask(__name__)
my_data=[{"s1":"idan"},{"s2":"matan"},{"s3":"or"}]

#home page
@app.route("/")
def home():
    return '<h1>please type your request in the URL'

#read method
@app.route("/data/<ind>")
@app.route("/data/")
def students(ind=-1):
    if int(ind) < 0:
        return my_data
    else:
        return my_data[int(ind)]

#create method
@app.route("/add/", methods=['POST'])
def add_student():
         # get the data from user
        data= request.json
        print(data["name"])
        print(data["age"])
        my_data.append({len(my_data):data["name"]})
        add_to_db()
        return "student added"


#delete method
@app.route("/del/<ind>", methods=['DELETE'])
def del_student(ind=-1):
        if int(ind) > -1:
            my_data.pop(int(ind))
        return "student del"

#update method        
@app.route("/upd/<ind>", methods=['PUT'])
def upd_student(ind=-1):
        if int(ind) > -1:
            print(ind)
            data= request.json
            my_data[int(ind)]={len(my_data):data['name']}
        return "student update"




app.run(debug=True)