



import time
from kafka import KafkaProducer, KafkaConsumer
import threading
from const import *

green_led = False
red_led = False
temperature = 26.6

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER+':'+KAFKA_PORT)
last_reported = 0


def read_led():
    global green_led
    global red_led
    if green_led:
        print("Green Led is on")
    else:
        print("Green Led is off")
    if red_led:
        print("Red Led is on")
    else:
        print("Red Led is off")


def consume_led_command():
    consumer = KafkaConsumer(bootstrap_servers=KAFKA_SERVER+':'+KAFKA_PORT)
    consumer.subscribe(topics=('ledcommand'))
    global red_led
    global green_led
    for msg in consumer:
        print ('Led command received: ', msg.value)
        print ('Led to blink: ', msg.key)
        if msg.key == b'red' and msg.value == b'1':
            red_led = True
        if msg.key == b'red' and msg.value == b'0':
            red_led = False
        if msg.key == b'green' and msg.value == b'1':
            green_led = True
        if msg.key == b'green' and msg.value == b'0':
            green_led = False
        read_led()

trd =threading.Thread(target=consume_led_command)
trd.start()

while True:
    temperature = 26.6
    producer.send('temperature', str(temperature).encode())
    time.sleep(2)
