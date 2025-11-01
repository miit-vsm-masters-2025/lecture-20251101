from kafka import KafkaConsumer, ConsumerRebalanceListener


class Listener(ConsumerRebalanceListener):
    def on_partitions_revoked(self, revoked):
        print(f"Partitions revoked: {revoked}")

    def on_partitions_assigned(self, assigned):
        print(f"Partitions assigned: {assigned}")


consumer = KafkaConsumer(
    group_id='python-consumer',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True
)

consumer.subscribe(['test'], listener=Listener())

## Won't work until we start iteration, so we're using ConsumerRebalanceListener
# assigned_partitions = consumer.assignment()
# print(f"Assigned partitions: {[tp.partition for tp in assigned_partitions]}")

print("Starting Kafka consumer...")
for message in consumer:
    print(f"Received message: {message.value.decode('utf-8')}")
