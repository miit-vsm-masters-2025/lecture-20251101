import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.basic_publish(exchange='',
                      routing_key='test',
                      body='Hello World!')

connection.close()