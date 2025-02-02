import os
from dotenv import load_dotenv
from instapi.api import InstapAPI
from instapi.model.definition import InstapDefinition
from instapi.model.item import InstapItem
from instapi.listener import InstapEventListener

load_dotenv()

API_URL = os.getenv('API_URL')
API_TOKEN = os.getenv('API_TOKEN')

api = InstapAPI(API_URL, API_TOKEN)

# parameterDefinition = InstapDefinition("parameter")

# api.invoke(parameterDefinition.create_field_methods("parameter-min-value", "Wartość minimalna"))
# api.invoke(parameterDefinition.create_field_methods("parameter-max-value", "Wartość maksymalna"))
# api.invoke(parameterDefinition.create_field_methods("set-value", "Ustaw wartość"))
# api.invoke(parameterDefinition.create_field_methods("factor", "Ustaw wartość"))

def handle_ibombo_other_tasks_status_change(event):
    # Potwierdzenie rozpoczęcia zadania
    if (event.source_item == "ibombo-task-status-started"):
        # Konkretne zadanie
        item = api.read_item("ibombo-other-tasks", event.target_item)
        recipe = item.get_related_item("ibombo-recipe-2-other-tasks")
        steps = recipe.get_related_items("ibombo-steps-2-recipe")
        for step in steps:
            t = api.create_item("ibombo-other-tasks-steps")
            t.set_field("ibombo-other-tasks-steps-name", step.get_field("ibombo-steps-name"))
            t.set_field("ibombo-other-tasks-steps-id", step.slug)
            t.set_field("ibombo-other-tasks-amount", step.get_field("ibombo-steps-amount"))
            t.create_relation("ibombo-other-tasks-status-2-other-tasks-steps", "TODO-id-tego-statusu")
            t.create_relation("ibombo-other-tasks-2-other-tasks-steps", recipe)
    logging.info(f"Handled CreateRelationSuccessEvent: {event}")

listener = InstapEventListener(address="ibombo.rosapp.com:9092", group_id="ibombo-steps-1")
listener.subscribe("CreateRelationSuccessEvent", handle_ibombo_other_tasks_status_change)
listener.start_listening()
