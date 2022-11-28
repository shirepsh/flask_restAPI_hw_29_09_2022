import json
from flask import Flask,request

#start of the prog
app = Flask(__name__)

my_data=[]
MY_FILE= "Dataset.json"

#load ans save functions in order to save the data and changes into json file
def save_2_file():
    with open(MY_FILE, "w") as f:
            json.dump(my_data, f)

def load_from_file():
    try:
        with open(MY_FILE, "r") as f:
                return json.load( f)
    except:
        return []

#use the load func in the start (load into the arry), at the save func we will use after every change
my_data=load_from_file()

#the homePage EndPoint
@app.route("/")
def home():
    return '<h1>please type your request in the URL'

#EndPoint = read(get) method (1 for all the data, 1 for specific value)
#in order to look for specific value you need to write the index at thr url
@app.route("/data/<ind>")
@app.route("/data/")
def students(ind=-1): 
    #we will give this defult value in order to show all the data 
    # (and dont block the user at asking for value) if the user dont ask for a specific value. 
    if int(ind) < 0:
        return my_data
    else:
        return my_data[int(ind)]

#EndPoint = POST (add) method
#in order to add data you need to write at the body of the request (for now the thunder)
@app.route("/add/", methods=['POST'])
def add_student():
        # get the data from user
        data= request.json
        print(data["name"])
        print(data["age"])
        my_data.append({"name":data['name']})
        print(my_data)
        save_2_file()
        return "student added"

#EndPoint = DELETE method
# in order to delete you need to put at the URL the index you want to delet 
# pop = remove the elemnt in the index who given        
@app.route("/del/<ind>", methods=['DELETE'])
def del_student(ind=-1):
        if int(ind) > -1:
            my_data.pop(int(ind))
        return "student del"

#EndPoint = PUT (update)
# in order to update data you need to write at the URL the index of the data u want to update
# and in the body the index you want to update = new data.
@app.route("/upd/<ind>", methods=['PUT'])
def upd_student(ind=-1):
        if int(ind) > -1:
            print(ind)
            data= request.json
            my_data[int(ind)]={"name":data['name']}
        return "student update"

#end of the prog
app.run(debug=True)