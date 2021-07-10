from flask import Flask, request, abort, jsonify
from flask.templating import render_template
from lib.db import db
import sqlalchemy as sa
from lib.People import Person
import json

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


@app.route('/new/person', methods=['GET'])
def new_person_view():
    return render_template('person_add.html')


@app.route('/new/person', methods=['POST'])
def new_person():
    person = Person(
        fname=request.form["fname"],
        lname=request.form["lname"],
        address=request.form["address"],
        phone=request.form["phone"]
    )

    db_object.new(person)
    return render_template('person_added.html')


# API CALLS BELOW

@app.route('/api/people/', methods=['GET'])
def get_people():
    dPeople = list(map(lambda x: x.as_dict(), db_object.get_people()))
    return json.dumps(dPeople)


@app.route('/api/people/', methods=['POST'])
def post_people():
    if not request.json:
        abort(400)
    person = Person.from_json(request.json)
    db_object.new(person)
    return jsonify({'result': True})


if __name__ == '__main__':
    app.run()
