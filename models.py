from app import db

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
 