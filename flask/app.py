from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin
from config.config import Config

from client.mysql import SQLClient
from client.elasticsearch import ElasticsearchClient
import time

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
@cross_origin()
def hello_world():
    return 'StackBox is running!'


@app.route('/mysql_view_stacks', methods=['GET'])
@cross_origin()
def view_connection():
    j = dict()
    j['res'] = sql_client.fetch_all_stacks()
    return jsonify(j)


@app.route('/elasticsearch_view_stacks', methods=['GET'])
def search_full_text():
    j = dict()
    res = es_client.match_all()
    if res == 500:
        es_client.populate_index_from_mysql()
        res = es_client.match_all()
    j['res'] = res
    return jsonify(j)


if __name__ == '__main__':
    config = Config('./config/config.yaml')
    sql_client = SQLClient(config)
    es_client = ElasticsearchClient(config)
    app.run(host='0.0.0.0', port=80)
