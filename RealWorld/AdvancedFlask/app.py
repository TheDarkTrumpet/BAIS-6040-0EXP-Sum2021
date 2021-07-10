from flask import Flask
from flask.templating import render_template
from lib.db import People
import sqlalchemy as sa

app = Flask(__name__)

sqllite_engine = sa.create_engine('sqllite:////db/advanced_flask.db')
people = People(sqllite_engine)



@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/people', methods=['GET'])
def people():
    pass


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
