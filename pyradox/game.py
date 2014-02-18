import time
import warnings
import pyradox.txt

class Timer:
    def __enter__(self):
        self.start = time.clock()
        return self

    def __exit__(self, *args):
        self.end = time.clock()
        self.interval = self.end - self.start

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

class Game:
    def __init__(self, game_file):
        self.game_file = game_file
        self.save = None

        self.provinces = {}
        self.nations = {}

    def set_nation(self, nation_name):
        if nation_name not in self.nations:
            self.nations[nation_name] = Nation(nation_name)
        return self.nations[nation_name]

    def parse(self):
        for country_name, country_tree in self.save["countries"].items():
            nation = self.set_nation(country_name)

            for tag_name, tag_tree in country_tree.items():
                if tag_name == "active_relations":
                    for of_nation_name, of_nation_tree in tag_tree.items():
                        of_nation = self.set_nation(of_nation_name)
                        relation = Relation(of_nation, nation)
                        for rel_name, rel_value in of_nation_tree.items():
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
                        of_nation.set_relation(relation)

    def load(self):
        warnings.simplefilter("ignore", pyradox.txt.ParseWarning)

        t = Timer()

        with t:
            self.save =  pyradox.txt.parseFile(self.game_file)

        self.parse_time = t.interval

