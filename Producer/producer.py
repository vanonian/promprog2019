#!/usr/bin/env python3
import pika
import sys

import random
import time

try:
    connection = pika.BlockingConnection(pika.URLParameters("amqp://guest:guest@localhost:32769"))
    channel = connection.channel()
    channel.queue_declare(queue='rand_num')

    while True:
        data = random.randrange(-sys.maxsize-1, sys.maxsize)
        channel.basic_publish(exchange='', routing_key='rand_num', body=str(data))
        time.sleep(3)

except Exception:
    print('Something goes wrong', file=sys.stderr)
