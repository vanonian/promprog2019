import pika
import random
import sys
import time

pika_url = pika.ConnectionParameters('rabbit', 5672)

while True:
  try:
    connection = pika.BlockingConnection(pika_url)
    channel = connection.channel() 
    channel.queue_declare(queue='num')

    while True:
      data = str(random.randint(1, 1000000)) 
      channel.basic_publish(exchange='', routing_key='num', body=data.encode())
      time.sleep(1)
  
  except Exception as e:
    print(str(e), file=sys.stderr, flush=True)
    time.sleep(1)
