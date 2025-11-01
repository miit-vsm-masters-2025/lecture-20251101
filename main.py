import valkey

valkey_connection = valkey.Valkey(host='localhost', port=6379, db=0)

p = valkey_connection.pubsub()

p.subscribe('my_channel')
valkey_connection.publish('my_channel', 'Hello from Valkey Pub/Sub!')

for message in p.listen():
    if message['type'] == 'message':
        print(f"Received message: {message['data'].decode()}")
        # Handle other message types like 'subscribe', 'unsubscribe' if needed

p.unsubscribe('my_channel')