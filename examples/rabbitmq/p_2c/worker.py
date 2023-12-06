import pika
import time

credentials = pika.PlainCredentials('kpubuser', 'Password@12345')
parameters = pika.ConnectionParameters('rabbitmq.selfmade.ninja',
                                       5672,
                                       'Kishore2071_helloworld',
                                       credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='my_first_queue')

def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")
    time.sleep(body.count(b'.'))
    print(" [x] Done")    

channel.basic_consume(queue='my_first_queue',
                      auto_ack=True,
                      on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()








