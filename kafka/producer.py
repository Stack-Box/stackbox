import time
import random
from kafka import KafkaProducer

# give broker IP from docker
producer = KafkaProducer(bootstrap_servers='localhost:32770')

clients = ['vue', 'flask']
services = ['kafka', 'mysql', 'elasticsearch', 'kibana', 'nginx']

var = 1
c = 0
s = 0
while var == 1:

    # generate a random integer
    num = random.randint(0, 10)
    num_bytes = bytes(str(num), encoding='utf-8')
    client = bytes(str(clients[c]), encoding='utf-8')
    service = bytes(str(services[s]), encoding='utf-8')
    c = (c + 1) % len(clients)
    s = (s + 1) % len(services)
    # send to topic on broker
    producer.send('stackbox1', value=client, key=num_bytes)
    # wait 1 second
    time.sleep(1)
