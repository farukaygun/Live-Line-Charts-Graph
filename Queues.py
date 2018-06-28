import random
from kafka import KafkaProducer
import json
from collections import deque

while True:
    randomData = random.randint(1, 100)
    print(randomData)
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    producer.send('queue', json.dumps(randomData).encode('utf-8'))