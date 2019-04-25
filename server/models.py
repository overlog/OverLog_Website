from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()



class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    passwd = db.Column(db.String(255), nullable=False)


    def __init__(self, username, passwd):
        self.username = username
        self.passwd = generate_password_hash(passwd, method='sha256')

    @classmethod
    def authenticate(cls, **kwargs):
        username = kwargs.get('username')
        passwd = kwargs.get('passwd')

        if not username or not passwd:
            return None

        user = cls.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, passwd):
            return None

        return user

    def to_dict(self):
        return dict(id=self.id, email=self.username)