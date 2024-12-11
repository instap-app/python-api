from instapi.const import FIELD_SLUG, FIELD_NAME_FIELD
from instapi.model.item import InstapItem
from instapi.model.method import InstapMethod


class InstapField(InstapItem):
    def __init__(self, ctx: str, slug: str, name: str):
        super().__init__(ctx=ctx, definition=FIELD_SLUG, slug=slug)
        self.name = name

    def create_methods(self) -> [InstapMethod]:
        i = super().create_methods()
        m = InstapMethod("SET_VALUE", {
            "definition": self.definition,
            "item": self.slug,
            "field": FIELD_NAME_FIELD,
            "value": self.name
        })
        return i + [m]
