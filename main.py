import os
from dotenv import load_dotenv
from instapi.api import InstapAPI
from instapi.model.definition import InstapDefinition
from instapi.model.item import InstapItem

load_dotenv()

API_URL = os.getenv('API_URL')
API_TOKEN = os.getenv('API_TOKEN')

api = InstapAPI(API_URL, API_TOKEN)

parameterDefinition = InstapDefinition("parameter")

api.invoke_list(parameterDefinition.create_field_methods("min-value"))
