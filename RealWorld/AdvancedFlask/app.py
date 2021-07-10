from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return 'Hello World!'


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
