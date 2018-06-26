from kafka import KafkaConsumer, KafkaProducer

#mesajlarý okuyor.
# consumer = KafkaConsumer('test')
# for msg in consumer:
#     print (msg)

#mesajlarý gönderiyor.
producer = KafkaProducer(bootstrap_servers='localhost:9092')
for _ in range(100):
    producer.send('test', b'\xf6Mesaj gonderildi !')

# 1) Dizileri üret
# 2) dizileri servera gönder
# 3) serverdan dizleri all
# 4) dizilerin grafiðini çiz