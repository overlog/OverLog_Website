from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import jwt
import datetime
from functools import wraps

app = Flask(__name__)
CORS(app)
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = 'OVERLOG'


# Database

# Copy the uri of the database here!
engine = create_engine('postgres://wwignxrncfkuoj:42995cfd99e0913fe7385a6237401e81bd88c735c2285cb590f8c1a874a732bf@ec2-54-246-92-116.eu-west-1.compute.amazonaws.com:5432/d11mskt5lrs57u')

def auth(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            token = kwargs['token']
        except:
            token = request.args.get('token') or \
                    request.form.get('token')

        if not token:
            return jsonify({'message': 'Token required!'}), 403
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'message': 'Token invalid!'}), 403

        return f(*args, **kwargs)

    return wrapper



@app.route('/')
def hello_world():
    return "am"



    print("asdasd")
    connection = engine.connect()
    query = ("select * from log")
    result = connection.execute(query)
    dict = {}
    for i in result:
        dict[i["id"]] = {"type": i["type"], "text": i["text"]}

    print(dict)

    return jsonify(dict)


@app.route('/logs/<token>')
@auth
def logs(token):
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


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    print(username)
    print(password)
    token = ''
    if username == 'admin' and password == 'admin':
        token = jwt.encode({
            'user': username,
            'password': password,
        }, app.config['SECRET_KEY'])
    else:
        token = 'Invalid username or password'

    return jsonify({'token': token.decode("utf-8")})







if __name__ == '__main__':
    app.run()
