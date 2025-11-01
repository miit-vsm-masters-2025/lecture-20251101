from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'test',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True
)

print("Starting Kafka consumer...")
for message in consumer:
    print(f"Received message: {message.value.decode('utf-8')}")
