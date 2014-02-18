class Nation:
    def __init__(self, name):
        self.name = name

        self.relations = {}

    def set_relation(self, relation):
        self.relations[relation.from_nation] = relation

    def all_relations(self):
        for relation_name, relation in self.relations.items():
            print(relation)
            relation.all_modifiers()

    def __str__(self):
        return self.name