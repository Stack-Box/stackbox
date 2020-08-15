from flask import Flask
from flask import request
from flask import jsonify
from flask_api import status
from flask_cors import CORS, cross_origin
from config.config import Config
from flask_socketio import SocketIO, emit
from client.elasticsearch import ElasticsearchClient
from util.json_utils import JsonUtils
from handler.s3 import S3Handler
from handler.kafka import KafkaHandler
from handler.mysql import MysqlHandler
from handler.dynamodb import DynamoDBHandler

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
i = 0


@app.route('/')
@cross_origin()
def home():
    return 'StackBox is running!'


""" MySQL endpoints """


@app.route('/mysql_view_stacks', methods=['GET'])
@cross_origin()
def mysql_view_stacks():
    return jsonify(mysql_handler.select_all_from_stacks())


""" Elasticsearch endpoints """


@app.route('/elasticsearch_view_stacks', methods=['GET'])
def elasticsearch_view_stacks():
    res = es_client.match_all()
    if (not res) or (res == 500):
        es_client.populate_index()
        res = es_client.match_all()
    return jsonify(JsonUtils.json_obj_to_array(res))


""" Kafka endpoints """


@socketio.on('connect', namespace='/kafka')
def socket_connect():
    emit('logs', {'data': 'Connection established'})


@socketio.on('kafkaconsumer', namespace="/kafka")
def kafka_consume():
    try:
        messages = kakfa_handler.get_all_messages()
        print(messages)
        if len(messages) > 0:
            emit('kafkaconsumer1', {'data': ''})
            for message in messages:
                emit('kafkaconsumer', {'data': message})
    except:
        emit('logs', {'data': 'Unable to consume messages from topic'})


@socketio.on('kafkaproducer', namespace="/kafka")
def kafka_produce(message):
    try:
        kakfa_handler.put_message(message)
        emit('logs', {'data': 'Added ' + message + ' to topic'})
        emit('kafkaproducer', {'data': message})
        kafka_consume()
    except:
        emit('logs', {'data': 'Unable to add ' + message + ' to topic'})


""" S3 endpoints """


@app.route('/s3_object_list', methods=['POST'])
@cross_origin()
def s3_object_list():
    req_body = request.get_json()
    s3_handler = S3Handler(req_body["access_key_id"], req_body["access_key"], req_body["bucket"], req_body["region"])
    res = s3_handler.s3_object_list()
    if res['s3 objects'] is not None:
        return jsonify(res)
    else:
        return jsonify(res), status.HTTP_400_BAD_REQUEST


@app.route('/s3_view_object', methods=['POST'])
@cross_origin()
def s3_view_object():
    req_body = request.get_json()
    s3_handler = S3Handler(req_body["access_key_id"], req_body["access_key"], req_body["bucket"], req_body["region"])
    return jsonify(s3_handler.get_object(req_body["object_key"]))


"""
Dynamo GET endpoint
"""
@app.route('/dynamodb_get_items', methods=['GET'])
@cross_origin()
def s3_view_object():
    req_body = request.get_json()
    req_params = request.params.get_json()
    dynamodb_handler = DynamoDBHandler(req_body["access_key_id"], req_body["access_key"], req_body["region"])
    return jsonify(dynamodb_handler.get_dynamodb_items(req_params["table"]))

"""
Dynamo PUT endpoints
"""
@app.route('/dynamodb_put_item', methods=['POST'])
@cross_origin()
def s3_view_object():
    req_body = request.get_json()
    req_params = request.params.get_json()
    dynamodb_handler = DynamoDBHandler(req_body["access_key_id"], req_body["access_key"], req_body["region"])
    return jsonify(dynamodb_handler.put_dynamodb_item(req_params["table"],req_body["data"]))



if __name__ == '__main__':
    config = Config('./config/config.yaml')
    es_client = ElasticsearchClient(config)
    kakfa_handler = KafkaHandler(config)
    mysql_handler = MysqlHandler(config)
    socketio.run(app, host='0.0.0.0', port=80)
