from flask import Flask, jsonify, json
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

app = Flask(__name__)
CORS(app)
db = SQLAlchemy(app)


# Database

# Copy the uri of the database here!
engine = create_engine('')





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
