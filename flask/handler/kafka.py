from config.config import Config
from kafka import KafkaProducer, KafkaConsumer, TopicPartition
import uuid


class KafkaHandler:

    def __init__(self, config: Config):
        self.bootstrap_servers = config.kafka_host + ":" + str(config.kafka_port)
        self.group_id = 'consumer-1'
        self.kafka_topic = config.kafka_topic

    def get_all_messages(self):
        consumer = KafkaConsumer(group_id=self.group_id,
                                 bootstrap_servers=self.bootstrap_servers)
        tp = TopicPartition(self.kafka_topic, 0)

        # register to the topic
        consumer.assign([tp])

        # obtain the last offset value
        consumer.seek_to_end(tp)
        last_offset = consumer.position(tp)
        consumer.seek_to_beginning(tp)

        arr = []
        for message in consumer:
            arr.append(message.value.decode('utf-8'))
            if message.offset == last_offset - 1:
                break

        consumer.close()
        return arr

    def put_message(self, message):
        producer = KafkaProducer(bootstrap_servers=self.bootstrap_servers)
        producer.send(self.kafka_topic, value=bytes(str(message), encoding='utf-8'), key=bytes(str(uuid.uuid4()), encoding='utf-8'))
        producer.close()


