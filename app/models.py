from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, current_user

@login.user_loader
def load_user(id):
    return Person.query.get(int(id))

class Person(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(12), unique=True)
    password_hash = db.Column(db.String(128))
    firstname = db.Column(db.String(64))
    lastname = db.Column(db.String(64))
    email = db.Column(db.String(120), index=True, unique=True)

    def get_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Administrator(Person, db.Model):
    __tablename__ = 'administrator'

    def __repr__(self):
        return '<Administrator {} {} - {}>'.format(self.firstname, self.lastname,
                                                self.username)

class User(Person, db.Model):
    __tablename__ = 'user'
    #id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<User {} {} - {}>'.format(self.firstname, self.lastname,
                                                self.username)