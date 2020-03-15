from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin
from config.config import Config

from client.sql import SQLClient

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
@cross_origin()
def hello_world():
    return 'StackBox is running!'


@app.route('/view_stacks', methods=['GET'])
@cross_origin()
def view_connection():
    j = dict()
    j['res'] = sql_client.fetch_all_stacks()
    return jsonify(j)


if __name__ == '__main__':
    config = Config('./config/config.yaml')
    sql_client = SQLClient(config)
    app.run(host='0.0.0.0', port=80)
