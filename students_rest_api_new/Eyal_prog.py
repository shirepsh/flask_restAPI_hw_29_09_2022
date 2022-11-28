from flask import Flask,request

app = Flask(__name__)
my_data=[{"s1":"idan"},{"s2":"matan"},{"s3":"or"}]

@app.route("/")
def home():
    return '<h1>please type your request in the URL'


@app.route("/data/<ind>")
@app.route("/data/")
def students(ind=-1):
    if int(ind) < 0:
        return my_data
    else:
        return my_data[int(ind)]

@app.route("/add/", methods=['POST'])
def add_student():
        # get the data from user
        data= request.json
        print(data["name"])
        print(data["age"])
        my_data.append({len(my_data):data['name']})
        return "student added"

@app.route("/del/<ind>", methods=['DELETE'])
def del_student(ind=-1):
        if int(ind) > -1:
            my_data.pop(int(ind))
        return "student del"

@app.route("/upd/<ind>", methods=['PUT'])
def upd_student(ind=-1):
        if int(ind) > -1:
            print(ind)
            data= request.json
            my_data[int(ind)]={len(my_data):data['name']}
        return "student update"



app.run(debug=True)