from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
 
app = Flask(__name__)
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'link'
db = SQLAlchemy(app)
 
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    dob = db.Column(db.DateTime)
    group = db.Column(db.Integer)
    alias = db.Column(db.String(100))

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

class Group(db.Model):
    __tablename__ = "groups"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __init__(self, name):
        self.name = name

class List(db.Model):
    __tablename__ = "lists"

    id = db.Column(db.Integer, primary_key=True)
    group = db.Column(db.Integer)
    name = db.Column(db.String(100))
    desc = db.Column(db.String (500))

    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

class Item(db.Model):
    __tablename__ = "list_items"

    id = db.Column(db.Integer, primary_key=True)
    list = db.Column(db.Integer)
    desc = db.Column(db.String(500))

    def __init__(self, desc):
        self.desc = desc

class Message(db.Model):
    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True)
    group = db.Column(db.Integer)
    user = db.Column(db.Integer)
    created = db.Column(db.DateTime)
    message = db.Column(db.String(500))

    def __init__(self, message):
        self.message = message
 
# tasks = [
#     {
#         'id': 1,
#         'title': u'Buy groceries',
#         'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
#         'done': False
#     },
#     {
#         'id': 2,
#         'title': u'Learn Python',
#         'description': u'Need to find a good Python tutorial on the web', 
#         'done': False
#     }
# ]

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/log_in')
def log_in():
  return "Logging the user in..."

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})
 
if __name__ == '__main__':
    app.run()