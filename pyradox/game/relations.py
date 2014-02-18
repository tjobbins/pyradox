def parse_relation(of_nation, from_nation, relation_tree):
    relation = Relation(of_nation, from_nation)

    for rel_name, rel_value in relation_tree.items():
        if rel_name == "attitude":
            relation.attitude = rel_value
        elif rel_name == "trust":
            relation.trust = rel_value
        elif rel_name == "cached_sum":
            relation.opinion = rel_value
        elif rel_name == "opinion":
            for opinion_name, opinion_val in rel_value.items():
                if opinion_name == 'modifier':
                    modifier_name = opinion_val
                elif opinion_name == 'date':
                    date = opinion_val
                elif opinion_name == 'current_opinion':
                    relation.set_modifier(Opinion(modifier_name, date, opinion_val))
    return relation

class Opinion:
    def __init__(self, modifier_name, from_date, current):
        self.modifier_name = modifier_name

        self.from_date = from_date
        self.current = current

    def __str__(self):
        return 'Modifier: "{0}", from: "{1}", value: "{2}"'.format(
            self.modifier_name, self.from_date, self.current
        )

class Relation:
    def __init__(self, of_nation, from_nation):
        self.of_nation = of_nation
        self.from_nation = from_nation

        self.attitude = 'undiscovered'
        self.opinion = 0
        self.trust = 0

        self.modifiers = {}

    def set_modifier(self, modifier):
        self.modifiers[modifier.modifier_name] = modifier

    def all_modifiers(self):
        for modifier_name, modifier in self.modifiers.items():
            print(modifier)

    def __str__(self):
        return 'Relation of "{0}" from "{1}", attitude: "{2}", value: "{3}"'.format(
            str(self.of_nation), str(self.from_nation), self.attitude, self.opinion
        )
