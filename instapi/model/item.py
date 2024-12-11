from instapi.helpers.slugify import slugify
from instapi.model.method import InstapMethod


class InstapItem:
    def __init__(self, ctx: str, definition: str, slug: str):
        self.ctx = slugify(ctx)
        self.definition = slugify(definition)
        self.slug = slugify(slug)

    def create_methods(self) -> [InstapMethod]:
        m = InstapMethod("CREATE_ITEM", {
            "ctx": self.ctx,
            "definition": self.definition,
            "item": self.slug
        })
        return [m]

    def set_value_methods(self, field, value) -> [InstapMethod]:
        m = InstapMethod("SET_VALUE", {
            "definition": self.definition,
            "item": self.slug,
            "field": field,
            "value": value
        })
        return [m]
