#!/usr/bin/env python3
import pika
import sys

def callback(ch, method, properties, data):
    print(data)

try:
    connection = pika.BlockingConnection(pika.URLParameters("amqp://guest:guest@localhost:32769"))
    channel = connection.channel()
    channel.queue_declare(queue='rand_num')

    while True:
        chanel.basic_consume(callback, queue='hello', no_ack=True)
        
except Exception:
    print('Something goes wrong', file=sys.stderr)
