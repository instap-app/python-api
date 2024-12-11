from slugify import slugify
from instapi.model.method import InstapMethod


class InstapRelation:
    def __init__(self, source: str, relation: str, target: str):
        self.source = slugify(source)
        self.relation = slugify(relation)
        self.target = slugify(target)

    def create_method(self) -> InstapMethod:
        return InstapMethod("CREATE_RELATION", {
            "sourceItem": self.source,
            "relation": self.relation,
            "targetItem": self.target
        })
