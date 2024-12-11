from dataclasses import dataclass, field

import requests

from model.method import InstapMethod


@dataclass
class InstapAPI:
    endpoint: str
    token: str
    command_endpoint: str = field(init=False)

    def __post_init__(self):
        self.command_endpoint = f"{self.endpoint}/api/write/command"

    def post(self, method: InstapMethod):
        r = requests.post(self.command_endpoint, json=method.json(), headers={"Authorization": f"Bearer {self.token}"})
        print(f"HTTP:{r.status_code} - POST to {self.command_endpoint} with body: {method.json()}")

    def invoke(self, *methods: InstapMethod):
        for method in methods:
            print(f"Invoking {method} on {self.command_endpoint}")
            self.post(method)
        print(f"Invoked {len(methods)} methods on {self.command_endpoint}")
