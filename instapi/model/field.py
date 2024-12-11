from instapi.const import FIELD_SLUG
from instapi.model.item import InstapItem


class InstapField(InstapItem):
    def __init__(self, slug: str):
        super().__init__(definition=FIELD_SLUG, slug=slug)
