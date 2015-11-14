from flask import Flask
from flask.ext.sqlalchemy import SQLAchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAchemy(app)


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/log_in')
def log_in():
	return "Logging the user in..."

if __name__ == '__main__':
    app.run()

