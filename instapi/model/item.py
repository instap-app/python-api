from dataclasses import dataclass

from slugify import slugify

from instapi.model.method import InstapMethod


@dataclass
class InstapItem:
    definition: str
    slug: str

    def create_method(self) -> InstapMethod:
        return InstapMethod("CREATE_ITEM", {
            "definition": self.definition,
            "item": self.slug
        })

    def set_value_method(self, field, value) -> InstapMethod:
        return InstapMethod("SET_VALUE", {
            "definition": self.definition,
            "item": self.slug,
            "field": field,
            "value": value
        })

    def __post_init__(self):
        self.definition = slugify(self.definition)
        self.slug = slugify(self.slug)
