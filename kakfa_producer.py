import time
import json
from kafka import KafkaProducer
import requests

kafka_bootstrap_servers = 'localhost:9092'
kakfa_topic_name = 'Newtopic'

producer = KafkaProducer(
    bootstrap_servers=kafka_bootstrap_servers,
    value_serializer=lambda v: json.dumps(v).encode('utf-8'))

api_key = '309c668f769743adba1a0494f7d0451a'
url = f'https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}'

while True:
    response = requests.get(url)
    news_list = response.json().get('articles', [])

    for news in news_list:
        producer.send(kakfa_topic_name, {
            'title': news.get('title', ''),
            'description': news.get('description', ''),
            'url': news.get('url', ''),
            'urlToImage': news.get('urlToImage', ''),
            'publishedAt': news.get('publishedAt', '')
        })

    # Sleep for 30 sec before getting the next batch of news
    time.sleep(30)
