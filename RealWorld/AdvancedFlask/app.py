from flask import Flask
from flask.templating import render_template
import sqlalchemy as sa

app = Flask(__name__)


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
