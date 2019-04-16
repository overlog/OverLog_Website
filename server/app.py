from flask import Flask, jsonify, json
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

app = Flask(__name__)
CORS(app)
db = SQLAlchemy(app)


# Database
engine = create_engine('postgres://wwignxrncfkuoj:42995cfd99e0913fe7385a6237401e81bd88c735c2285cb590f8c1a874a732bf@ec2-54-246-92-116.eu-west-1.compute.amazonaws.com:5432/d11mskt5lrs57u')





@app.route('/')
def hello_world():


    print("asdasd")
    connection = engine.connect()
    query = ("select * from log")
    result = connection.execute(query)
    dict = {}
    for i in result:
        dict[i["id"]] = {"type": i["type"], "text": i["text"]}

    print(dict)

    return jsonify(dict)




@app.route('/logs')
def logs():

    connection = engine.connect()
    query = ("select * from log")
    result = connection.execute(query)
    dict = {}
    for i in result:
        log = i["text"].split(",")
        if(len(log)>2):
            dict[i["id"]] = {"date": log[0], "type": log[2]}

    print(dict)

    return jsonify(dict)



if __name__ == '__main__':
    app.run()
