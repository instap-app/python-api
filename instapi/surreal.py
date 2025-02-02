import requests
from instapi.model.method import InstapMethod


class InstapSurrealAPI:
    
    def __init__(self, host: str, token: str, port: int = 80):
        self.host = host
        self.token = token
        self.port = port
        self.headers = {
            "Authorization": f"Bearer {self.token}"
        }

    def get_one_item(self, definition: str, slug: str):
        # url = f"{self.host}:{self.port}/item/one"
        url = "http://dane.imperius.io/api/surreal/item/one"
        params = {
            "definition": definition,
            "item": slug
        }
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()  # Rzuci wyjątek, jeśli status nie jest 2xx
        return response.json()

    def get_related_items(self, definition: str, item: str, relation: str):
        url = "http://dane.imperius.io/api/surreal/item/related"
        params = {
            "definition": definition,
            "item": item,
            "relation": relation
        }
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()  # Rzuci wyjątek, jeśli status nie jest 2xx
        return response.json()
    
    def get_first_related_item(self, definition: str, item: str, relation: str):
        items = self.get_related_items(definition, item, relation)
        return items[0] if items else None
