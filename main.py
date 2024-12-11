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

api.invoke(parameterDefinition.create_field_methods("parameter-min-value", "Wartość minimalna"))
api.invoke(parameterDefinition.create_field_methods("parameter-max-value", "Wartość maksymalna"))
api.invoke(parameterDefinition.create_field_methods("set-value", "Ustaw wartość"))
api.invoke(parameterDefinition.create_field_methods("factor", "Ustaw wartość"))
