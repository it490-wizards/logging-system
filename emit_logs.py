#!/usr/bin/env python3

import os
import sys

import dotenv
import pika

dotenv.load_dotenv()


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

message = " ".join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange="logs", routing_key="", body=message)
print(" [x] Sent %r" % message)
connection.close()
