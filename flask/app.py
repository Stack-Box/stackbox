from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin
from config.config import Config

from client.mysql import SQLClient
from client.elasticsearch import ElasticsearchClient
from util.json_utils import JsonUtils
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
def mysql_view_stacks():
    return jsonify(JsonUtils.array_to_json_array(sql_client.fetch_all_stacks()))


@app.route('/elasticsearch_view_stacks', methods=['GET'])
def elasticsearch_view_stacks():
    res = es_client.match_all()
    if (not res) or (res == 500):
        es_client.populate_index()
        res = es_client.match_all()
    return jsonify(JsonUtils.json_obj_to_array(res))


if __name__ == '__main__':
    config = Config('./config/config.yaml')
    sql_client = SQLClient(config)
    es_client = ElasticsearchClient(config)
    app.run(host='0.0.0.0', port=80)
