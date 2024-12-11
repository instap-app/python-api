from dataclasses import dataclass

from slugify import slugify

from instapi.model.method import InstapMethod


@dataclass
class InstapRelation:
    source: str
    relation: str
    target: str

    def create_method(self) -> InstapMethod:
        return InstapMethod("CREATE_RELATION", {
            "sourceItem": self.source,
            "relation": self.relation,
            "targetItem": self.target
        })

    def __post_init__(self):
        self.source = slugify(self.source)
        self.target = slugify(self.target)
        self.relation = slugify(self.relation)
