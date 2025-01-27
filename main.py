import os
from dotenv import load_dotenv
from instapi.api import InstapAPI
from instapi.model.definition import InstapDefinition
from instapi.model.item import InstapItem
from instapi.listener import InstapEventListener

load_dotenv()

# API_URL = os.getenv('API_URL')
# API_TOKEN = os.getenv('API_TOKEN')

# api = InstapAPI(API_URL, API_TOKEN)

# parameterDefinition = InstapDefinition("parameter")

# api.invoke(parameterDefinition.create_field_methods("parameter-min-value", "Wartość minimalna"))
# api.invoke(parameterDefinition.create_field_methods("parameter-max-value", "Wartość maksymalna"))
# api.invoke(parameterDefinition.create_field_methods("set-value", "Ustaw wartość"))
# api.invoke(parameterDefinition.create_field_methods("factor", "Ustaw wartość"))

class SimpleEventConsumer(InstapEventListener):
    def on_event(self, event):
        logging.info(f"Consuming event: {event.__dict__}")

kafka_config = {
    'bootstrap.servers': 'ibombo.rosapp.com:9092',
    'group.id': 'SimpleEventConsumer',
    'auto.offset.reset': 'earliest'
}
consumer = SimpleEventConsumer(kafka_config)
consumer.start_listening()
