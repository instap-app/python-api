class CreateRelationSuccessEvent:
    def __init__(self, source_item, source_definition, relation, target_item, target_definition, one_to_one):
        self.source_item = source_item
        self.source_definition = source_definition
        self.relation = relation
        self.target_item = target_item
        self.target_definition = target_definition
        self.one_to_one = one_to_one
