#!/usr/bin/python3

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

channel.exchange_declare(exchange='logs', exchange_type='fanout')


path = "PATH TO STD ERROR LOGS"
fil = open(path, "r")
exe = file.read()
file.close()

path = "PATH TO APACHE ERROR LOGS"
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