from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin
from config.config import Config
from flask_socketio import SocketIO, emit, send

from client.mysql import SQLClient
from client.elasticsearch import ElasticsearchClient
from util.json_utils import JsonUtils

from kafka import KafkaProducer, KafkaConsumer, TopicPartition

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
i = 0


@socketio.on('connect', namespace='/kafka')
def test_connect():
    emit('logs', {'data': 'Connection established'})


@socketio.on('kafkaconsumer', namespace="/kafka")
def kafkaconsumer(message):
    consumer = KafkaConsumer(group_id='consumer-1',
                             bootstrap_servers='kafka:9092')
    tp = TopicPartition('stackbox2', 0)
    # register to the topic
    consumer.assign([tp])

    # obtain the last offset value
    consumer.seek_to_end(tp)
    lastOffset = consumer.position(tp)
    consumer.seek_to_beginning(tp)
    emit('kafkaconsumer1', {'data': ''})
    for message in consumer:
        emit('kafkaconsumer', {'data': message.value.decode('utf-8')})
        if message.offset == lastOffset - 1:
            break
    consumer.close()


@socketio.on('kafkaproducer', namespace="/kafka")
def kafkaproducer(message):
    producer = KafkaProducer(bootstrap_servers='kafka:9092')
    global i
    i = i + 1
    producer.send('stackbox2', value=bytes(str(message), encoding='utf-8'), key=bytes(str(i), encoding='utf-8'))
    emit('logs', {'data': 'Added ' + message + ' to topic'})
    emit('kafkaproducer', {'data': message})
    producer.close()
    kafkaconsumer(message)


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
    socketio.run(app, host='0.0.0.0', port=80)
