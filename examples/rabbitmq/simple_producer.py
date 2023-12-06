import pika
import random
import time

credentials = pika.PlainCredentials('kpubuser', 'Password@12345')
parameters = pika.ConnectionParameters('rabbitmq.selfmade.ninja',
                                       5672,
                                       'Kishore2071_helloworld',
                                       credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue='my_first_queue')

while True:
    message= str(random.random())
    channel.basic_publish(exchange='',
                        routing_key='my_first_queue',
                        body=message)
    print(" [x] Sent '{}!'".format(message))
    time.sleep(0.1)

connection.close()
