from flask import Flask, jsonify, json
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

app = Flask(__name__)
CORS(app)
db = SQLAlchemy(app)


# Database
engine = create_engine('postgresql://postgres:12345@localhost:5432/overlog')





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


@app.route("/veri", methods = ["GET"])
def get():
    return "asdasda"




if __name__ == '__main__':
    app.run()
