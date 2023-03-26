import json
from kafka import KafkaConsumer
import csv

kafka_bootstrap_servers = 'localhost:9092'
kakfa_topic_name = 'Newtopic'
csv_file_name = 'news.csv'

consumer = KafkaConsumer(kakfa_topic_name, bootstrap_servers=kafka_bootstrap_servers,
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))

# Continuously consume Kafka messages
# for message in consumer:
#     print(message.value)

with open(csv_file_name, mode='a') as csv_file:
    fieldnames = ['title', 'description', 'url', 'urlToImage', 'publishedAt']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for message in consumer:
        news = message.value
        writer.writerow({
            'title': news['title'],
            'description': news['description'],
            'url': news['url'],
            'urlToImage': news['urlToImage'],
            'publishedAt': news['publishedAt']
        })
