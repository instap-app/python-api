from instapi.helpers.slugify import slugify
from instapi.model.method import InstapMethod


class InstapItem:
    def __init__(self, definition: str, slug: str):
        self.definition = slugify(definition)
        self.slug = slugify(slug)

    def create_methods(self) -> [InstapMethod]:
        m = InstapMethod("CREATE_ITEM", {
            "definition": self.definition,
            "item": self.slug
        })
        return [m]

    def set_value_method(self, field, value) -> [InstapMethod]:
        m = InstapMethod("SET_VALUE", {
            "definition": self.definition,
            "item": self.slug,
            "field": field,
            "value": value
        })
        return [m]
