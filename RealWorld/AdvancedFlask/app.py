from flask import Flask
from flask.templating import render_template
from lib.db import db
import sqlalchemy as sa

app = Flask(__name__)

sqlite_engine = sa.create_engine('sqlite:///db/advanced_flask.db')
db_object = db(sqlite_engine)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/people', methods=['GET'])
def people():
    people = db_object.get_people()
    return render_template('people.html', people=people)


@app.route('/new/person', methods=['POST'])
def new_person():
    pass


@app.route('/api/people/get', methods=['GET'])
def get_people():
    pass


@app.route('/api/people/put', methods=['POST'])
def put_people():
    pass


if __name__ == '__main__':
    app.run()
