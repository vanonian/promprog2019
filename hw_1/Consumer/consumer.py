import pika
import sys
import time
	
pika_url = pika.ConnectionParameters('rabbit', 5672)

def callback(ch, method, properties, body):
  print(body.decode(), file=sys.stdout, flush=True)    
		
while True:
  try:
    connection = pika.BlockingConnection(pika_url)
    channel = connection.channel()
    channel.queue_declare(queue='num')
    
    channel.basic_consume('num', callback )             
    channel.start_consuming()
  
  except Exception as e:
    print(str(e), file=sys.stderr, flush=True)
    time.sleep(1)
