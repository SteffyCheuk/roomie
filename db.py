from app import db
import datetime
from sqlalchemy import Column, Integer, String

class User(db.Model):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    email = Column(String(100))
    dob = Column(DateTime)
    group = Column(Integer)
    alias = Column(String(100))

class Group(db.Model):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))

class List(db.Model):
    __tablename__ = "lists"

    id = Column(Integer, primary_key=True)
    group = Column(Integer)
    name = Column(String(100))
    desc = Column(String (500))

class Item(db.Model):
    __tablename__ = "list_items"

    id = Column(Integer, primary_key=True)
    list = Column(Integer)
    desc = Column(String(500))

class Message(db.Model):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)
    group = Column(Integer)
    user = Column(Integer)
    created_date = Column(DateTime)
    message = Column(String(500))