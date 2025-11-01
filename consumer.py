import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

channel.basic_consume(queue='test',
                      auto_ack=True,
                      on_message_callback=callback)
channel.start_consuming()