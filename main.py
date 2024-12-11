from instapi.api import InstapAPI
from instapi.model.item import InstapItem

API_URL = f"http://address.com/command"
API_TOKEN = "TOKEN"

api = InstapAPI(API_URL, API_TOKEN)
item = InstapItem("parameter", "test")
api.invoke(item.create_method())
