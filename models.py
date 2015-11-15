from app import db
import datetime

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    dob = db.Column(db.DateTime)
    group_id = db.Column(db.Integer)
    alias = db.Column(db.String(100))

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.first_name + self.last_name)

class Group(db.Model):
    __tablename__ = "groups"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Group %r>' % self.name 

class List(db.Model):
    __tablename__ = "lists"

    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer)
    name = db.Column(db.String(100))
    desc = db.Column(db.String (500))

    def __init__(self, group_id, name, desc):
        self.group_id = group_id
        self.name = name
        self.desc = desc

    def __repr__(self):
        return '<List %r>' % self.name

class ListItem(db.Model):
    __tablename__ = "list_items"

    id = db.Column(db.Integer, primary_key=True)
    list_id = db.Column(db.Integer)
    name = db.Column(db.String(100))
    quantity = db.Column(db.String(100))
    desc = db.Column(db.String(500))
    date_added = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def __init__(self, list_id, name, quantity, desc):
        self.list_id = list_id
        self.name = name
        self.quantity = quantity
        self.desc = desc

    def __repr__(self):
        return '<Item %r>' % self.name

class Message(db.Model):
    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    message = db.Column(db.String(500))

    def __init__(self, group_id, user_id, created_at, message):
        self.group_id = group_id
        self.user_id = user_id
        self.created_at = created_at
        self.message = message

    def __repr__(self):
        return '<Message %r' % self.message
 