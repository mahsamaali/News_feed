from confluent_kafka import Consumer, KafkaError

KAFKA_BROKER = "localhost:9092"  # Update with your Kafka broker address
KAFKA_TOPIC = "feed_topic1"  # Update with the Kafka topic you want to consume

# Create a Kafka consumer
consumer = Consumer({
    'bootstrap.servers': KAFKA_BROKER,
    'group.id': 'my_consumer_group',
    'auto.offset.reset': 'earliest'
})

# Subscribe to the Kafka topic
consumer.subscribe([KAFKA_TOPIC])

while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue

    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            continue
        else:
            print(f"Error while consuming from Kafka: {msg.error()}")
            break

    # Process the message (e.g., pass it through a model)
    data = json.loads(msg.value())  # Assuming data is in JSON format
    # Call your model or processing logic here
    # result = your_model(data)

    # You can print or process the result as needed
    # print(result)
