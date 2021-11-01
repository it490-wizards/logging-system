#!/bin/python3
import pika
import sys


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

channel.exchange_declare(exchange='logs', exchange_type='fanout')


path = ""
file = open(path, "r")
exe = file.read()
file.close()





#try:
 #   inputNum = int(input(" input a number"))
#except Exception as e:

  #  print (e)
 #   exe = str(e)
 
message = exe
channel.basic_publish(exchange='logs', routing_key='', body=message)
print(" [x] Sent %r" % message)
connection.close