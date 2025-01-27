from abc import ABC, abstractmethod
from confluent_kafka import Consumer, KafkaException
import logging

logging.basicConfig(level=logging.INFO)

class InstapEventListener(ABC):
    def __init__(self, address, id):
        kafka_config = {
            'bootstrap.servers': address,
            'group.id': id,
            'auto.offset.reset': 'earliest'
        }
        self.kafka_consumer = Consumer(kafka_config)
        self.topic = 'EVENTS'
        self.kafka_consumer.subscribe([self.topic])

    @abstractmethod
    def on_event(self, event):
        pass

    def start_listening(self):
        logging.info("Starting Kafka listener...")
        try:
            while True:
                msg = self.kafka_consumer.poll(1.0)
                if msg is None:
                    continue
                if msg.error():
                    if msg.error().code() == KafkaException._PARTITION_EOF:
                        continue
                    else:
                        logging.error(f"Kafka error: {msg.error()}")
                        break
                
                event = self.parse_event(msg.value().decode('utf-8'))
                if isinstance(event, CreateRelationSuccessEvent):
                    self.on_event(event)
        except KeyboardInterrupt:
            logging.info("Stopping listener...")
        finally:
            self.kafka_consumer.close()

    def parse_event(self, event_json):
        import json
        event_data = json.loads(event_json)
        if event_data.get('type') == 'CreateRelationSuccessEvent':
            return CreateRelationSuccessEvent(
                event_data['sourceItem'],
                event_data['sourceDefinition'],
                event_data['relation'],
                event_data['targetItem'],
                event_data['targetDefinition'],
                event_data['oneToOne']
            )
        return None
