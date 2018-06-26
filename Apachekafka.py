from kafka import KafkaConsumer, KafkaProducer

#mesajlar� okuyor.
# consumer = KafkaConsumer('test')
# for msg in consumer:
#     print (msg)

#mesajlar� g�nderiyor.
producer = KafkaProducer(bootstrap_servers='localhost:9092')
for _ in range(100):
    producer.send('test', b'\xf6Mesaj gonderildi !')

# 1) Dizileri �ret
# 2) dizileri servera g�nder
# 3) serverdan dizleri all
# 4) dizilerin grafi�ini �iz