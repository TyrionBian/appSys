from kafka import KafkaConsumer
import json
import os
from threading import Timer,Thread,Event
from random import randint
import time

kafka_server = os.environ['KAFKA_SERVER']
# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer('data',
                         group_id='my-group',
                         bootstrap_servers=[kafka_server])


bag = []

class MyThread(Thread):
    def __init__(self, event):
        Thread.__init__(self)
        self.stopped = event

    def run(self):
        global bag
        while not self.stopped.wait(1):
            if len(bag)>0:
                ## TODO send jobs in bag to model API
                print(*bag)
                bag = []

stopFlag = Event()
thread = MyThread(stopFlag)
thread.start()
for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))
    # add to bag
    bag.append((message.key,message.value))

time.sleep(1.1)
stopFlag.set()
