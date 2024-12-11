from instapi.const import DEFINITION_SLUG, FIELD_RELATION_TYPE
from instapi.model.field import InstapField
from instapi.model.item import InstapItem
from instapi.model.method import InstapMethod
from instapi.model.relation import InstapRelation


class InstapDefinition(InstapItem):
    def __init__(self, slug: str):
        super().__init__(definition=DEFINITION_SLUG, slug=slug)

    def create_field_methods(self, slug: str) -> [InstapMethod]:
        field = InstapField(slug)
        relation = InstapRelation(field.slug, FIELD_RELATION_TYPE, self.slug)
        return [
            field.create_method(),
            relation.create_method(),
        ]
