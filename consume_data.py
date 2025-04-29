from kafka import KafkaConsumer
import json

# Configuration du Consumer
consumer = KafkaConsumer(
    'cours_bourse',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',  # Pour lire depuis le début du topic
    enable_auto_commit=True,
    group_id='test-consumer-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("✅ Consumer Kafka connecté, écoute sur le topic 'cours_bourse'...\n")

# Boucle d'écoute
for message in consumer:
    print(f"📈 Nouveau message reçu:")
    print(message.value)
