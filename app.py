from datetime import datetime
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, make_response, request, Response, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import *
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres@localhost/roomie'
db = SQLAlchemy(app)

@app.route('/')
def hello():
  return "Hello World!"

@app.route('/login', methods=['GET', 'POST'])
def login():
  email = request.args.get('email')
  print email
  session['id'] = '1'
  return session['id']

@app.route('/tasks', methods=['GET'])
def get_tasks():
  return jsonify({'tasks': tasks})
 
@app.route('/register', methods=['GET', 'POST'])
def create_account():
	email = request.args.get('email')	
	first_name = request.args.get('first_name')
	last_name = request.args.get('last_name')
	if email is None or first_name is None or last_name is None:
		return 'False'
	else:
		try:
			new_user = User(first_name, last_name, email)
			db.session.add(new_user)
			db.session.commit()
		except:
			return 'False'
	return 'True'

@app.route('/create_group')
def create_group():
	name = request.args.get('name')
	print name
	if name is None:
		return 'False'
	else:
		try:
			# add the new group
			new_group = Group(name)
			db.session.add(new_group)
			db.session.commit()
			# create corresponding list and update user.group_id
			new_list = List(new_group.id, 'Groceries', 'A list of household groceries that need to be purchased.')
			current_user = User.query.get(session['id'])
			current_user.group_id = new_group.id
			db.session.merge(current_user)
			db.session.add(new_list)
			db.session.commit()
			return 'True'
		except:
			return 'False'


@app.route('/add_item')
def add_item():
	if session['id'] is None:
		return 'False'
	else:
		list_id = request.args.get('list_id')
		name = request.args.get('name')
		quantity = request.args.get('quantity')
		desc = request.args.get('desc')
		new_item = ListItem(list_id, name, quantity, desc)
		if list_id is None or name is None or quantity is None or desc is None:
			return 'False'
		else:
			try:
				new_item = ListItem(list_id, name, quantity, desc)
				db.session.add(new_item)
				db.session.commit()
				return 'True'
			except:
				return 'False'

@app.route('/get_list')
def get_list():
	if session['id'] is None:
		return 'False'
	else:
		list_id = request.args.get('list_id')
		print 'b'
		items = ListItem.query.filter(ListItem.list_id==list_id).all()
		print 'i'
		# items = items.order_by(date_added)
		print items
		# build json
		data = {}
		for item in items:
			data[item.id] = {
				'name': item.name, 
				'quantity': item.quantity, 
				'desc': item.desc,
				'date_added': item.date_added
			}
			print data
		return jsonify(data)

if __name__ == '__main__':
	app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
	app.run()