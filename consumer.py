import valkey

valkey_connection = valkey.Valkey(host='localhost', port=6379, db=0)
def consume_messages():
    while True:
        try:
            p = valkey_connection.pubsub()
            p.subscribe('my_channel')
            for message in p.listen():
                if message['type'] == 'message':
                    print(f"Received message: {message['data'].decode()}")
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    consume_messages()