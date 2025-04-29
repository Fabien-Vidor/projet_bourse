import yfinance as yf
import feedparser
from kafka import KafkaProducer
import json
import time

# Configuration Kafka
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def get_stock_price(ticker):
    stock = yf.Ticker(ticker)
    todays_data = stock.history(period='1d')
    price = todays_data['Close'].iloc[-1]
    message = {
        'symbol': ticker,
        'price': float(price),
        'timestamp': str(todays_data.index[-1])
    }
    print("Sending to Kafka (cours_bourse):", message)
    producer.send('cours_bourse', message)
    producer.flush()



def get_rss_feed(url):
    feed = feedparser.parse(url)
    for entry in feed.entries[:5]:  # Juste les 5 premiers
        message = {
            'title': entry.title,
            'link': entry.link,
            'published': entry.published if hasattr(entry, 'published') else ''
        }
        print("Sending to Kafka (news_finance):", message)
        producer.send('news_finance', message)
        time.sleep(0.2)  # Petite pause pour éviter la saturation rapide
    producer.flush()

# Exécutions
get_stock_price('AAPL')
get_rss_feed("https://www.lesechos.fr/rss/finance-marches.xml")
get_rss_feed("https://www.latribune.fr/rss/rubrique/finance.xml")
