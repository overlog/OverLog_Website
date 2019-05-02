from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import jwt
from sqlalchemy.orm.exc import NoResultFound
from functools import wraps
import csv

app = Flask(__name__)
CORS(app)
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = 'OVERLOG'


# Database

# Copy the uri of the database here!
#engine = create_engine('postgres://wwignxrncfkuoj:42995cfd99e0913fe7385a6237401e81bd88c735c2285cb590f8c1a874a732bf@ec2-54-246-92-116.eu-west-1.compute.amazonaws.com:5432/d11mskt5lrs57u')
engine = create_engine('postgres://postgres:bewelko@localhost:5432/overlog')


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
def hello_world(): #write weather datas to database
    connection = engine.connect()
    ##

    with open('/home/konik/Desktop/weatherHistory.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            elif line_count == 100: #how many lines will write to database
                break
            date = "'" + row["Formatted Date"] + "'"
            type = "'" + row["Precip Type"] + "'"
            text = "'" + row["Summary"] + "'"

            query = ("insert into log(type, text, userID, date) values(" + type + ", " + text + ", 1, " + date +")")
            connection.execute(query)
            #print(f'\t{row["Summary"]} ')
            line_count += 1
    return "success"



@app.route('/logs/<token>')
@auth
def logs(token):
    connection = engine.connect()
    query = ("select * from log")
    result = connection.execute(query)
    JSONArray = []
    for i in result:
        JSONArray.append({"date": i[0]})

    print(JSONArray)

    return jsonify(JSONArray)


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    token = ''

    connection = engine.connect()
    query = ("select id from users where username = '" + username + "' and passwd = '" +  str(password) + "'")
    result = connection.execute(query)

    user = result.first()
    if user is not None:
        token = jwt.encode({
            'user': username,
            'password': password,
        }, app.config['SECRET_KEY'])
        token = token.decode("utf-8")
        userID = user[0]
    else:
        token = 'Invalid username or password'
        userID = -1

    return jsonify({'token': token, 'userID': userID})




if __name__ == '__main__':
    app.run()
