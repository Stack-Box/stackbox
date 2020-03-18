from kafka import KafkaConsumer

# continuous loop
var = 1
while var == 1:

    # initialize consumer to given topic and broker
    consumer1 = KafkaConsumer('services',
                            group_id='consumer-1',
                            bootstrap_servers='localhost:32770')
    # consumer2 = KafkaConsumer('clients',
    #                          group_id='consumer-1',
    #                          bootstrap_servers='localhost:32770')

    # loop and print messages
    for msg in consumer1:
        print (msg)

    #     # loop and print messages
    # for msg in consumer2:
    #     print(msg)