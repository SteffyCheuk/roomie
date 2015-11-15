from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres@localhost/roomie'
db = SQLAlchemy(app)

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