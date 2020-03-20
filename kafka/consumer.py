from kafka import KafkaConsumer, TopicPartition

consumer = KafkaConsumer(group_id='consumer-1',
                         bootstrap_servers='localhost:32770')
tp = TopicPartition('stackbox1', 0)
# register to the topic
consumer.assign([tp])

# obtain the last offset value
consumer.seek_to_end(tp)
lastOffset = consumer.position(tp)
print(lastOffset)

consumer.seek_to_beginning(tp)

for message in consumer:
    print("Offset:", message.offset)
    print("Value:", message.value)
    print(lastOffset)
    if message.offset == lastOffset - 2:
        break
