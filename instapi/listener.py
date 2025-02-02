class InstapEventListener:
    def __init__(self, address, group_id):
        kafka_config = {
            'bootstrap.servers': address,
            'group.id': group_id,
            'auto.offset.reset': 'earliest'
        }
        self.kafka_consumer = Consumer(kafka_config)
        self.topic = 'EVENTS'
        self.kafka_consumer.subscribe([self.topic])
        self.subscriptions = {}

    def subscribe(self, event_type, handler_function):
        """
        Subscribe a handler function to a specific event type.

        :param event_type: The type of event to subscribe to (string).
        :param handler_function: The function to execute when the event is received.
        """
        if event_type not in self.subscriptions:
            self.subscriptions[event_type] = []
        self.subscriptions[event_type].append(handler_function)

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
                if event and event['type'] in self.subscriptions:
                    for handler in self.subscriptions[event['type']]:
                        handler(event)
        except KeyboardInterrupt:
            logging.info("Stopping listener...")
        finally:
            self.kafka_consumer.close()

    def parse_event(self, event_json):
        """
        Parse the raw JSON string into an event dictionary.

        :param event_json: Raw JSON string of the event.
        :return: Parsed event dictionary.
        """
        try:
            return json.loads(event_json)
        except json.JSONDecodeError as e:
            logging.error(f"Failed to parse event JSON: {e}")
            return None