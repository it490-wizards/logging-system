#!/bin/python3

import os
import pika


connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host=os.getenv("PIKA_HOST"),
        port=os.getenv("PIKA_PORT"),
        virtual_host=os.getenv("PIKA_VIRTUAL_HOST"),
        credentials=pika.PlainCredentials(
            username=os.getenv("PIKA_USERNAME"),
            password=os.getenv("PIKA_PASSWORD"),
        ),
    )
)
channel = connection.channel()

channel.exchange_declare(exchange="logs", exchange_type="fanout")

result = channel.queue_declare(queue="", exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange="logs", queue=queue_name)

print(" [*] Waiting for logs. To exit press CTRL+C")


def callback(ch, method, properties, body):
    print(" [x] %r" % body)


channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
