import valkey

valkey_connection = valkey.Valkey(host='localhost', port=6379, db=0)

def produce_messages():
    while True:
        try:
            message = input(">")
            valkey_connection.publish('my_channel', message)
        except KeyboardInterrupt:
            break
            
if __name__ == "__main__":
    produce_messages()