import os
from dotenv import load_dotenv
from instapi.surreal import InstapSurrealAPI
from instapi.model.definition import InstapDefinition
from instapi.model.item import InstapItem
from instapi.listener import InstapEventListener

token = "eyJhbGciOiJIUzI1NiJ9.eyJ1c2VySXNBZG1pbiI6dHJ1ZSwidXNlckVtYWlsIjoiYWRtaW4zMkBnbWFpbC5jb20iLCJ1c2VySWQiOiIwMDAwMDAwMC1jY2NjLWNjY2MtY2NjYy0xMDAwMDAwMDAwMDMiLCJ1c2VyQ3R4IjoiaW5zdGFwK2NvcmUiLCJ1c2VyUm9sZXMiOlsicm9sZS1hZG1pbiJdLCJ1c2VyU2x1ZyI6ImFkbWluMzIiLCJzdWIiOiJhZG1pbjMyQGdtYWlsLmNvbSIsImlhdCI6MTcwNTkzNDcwOSwiZXhwIjo5MjIzMzcyMDM2ODU0Nzc1fQ.nNgRrhV8lK98EZRjmgxWZ9XRP9Wh5OiGwK3oucXmdtU"
surreal = InstapSurrealAPI("dane.imperius.io", token, 80)

i = surreal.get_one_item("definition", "definition")
print("item:", i)

print("")

r = surreal.get_first_related_item("definition", "definition", "field-relation-type-item")
print("related item:", r)
