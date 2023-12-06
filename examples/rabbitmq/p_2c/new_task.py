import pika
import sys

credentials = pika.PlainCredentials('kpubuser', 'Password@12345')
parameters = pika.ConnectionParameters('rabbitmq.selfmade.ninja',
                                       5672,
                                       'Kishore2071_helloworld',
                                       credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue='my_first_queue')

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='',
                      routing_key='my_first_queue',
                      body=message)
print(f" [x] Sent {message}")

connection.close()
