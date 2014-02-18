import time
import warnings
import pyradox.txt
from pyradox.game.relations import parse_relation
from pyradox.game.nation import Nation

class Timer:
    def __enter__(self):
        self.start = time.clock()
        return self

    def __exit__(self, *args):
        self.end = time.clock()
        self.interval = self.end - self.start

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
                        relation = parse_relation(of_nation, nation, of_nation_tree)
                        of_nation.set_relation(relation)

    def load(self):
        warnings.simplefilter("ignore", pyradox.txt.ParseWarning)

        t = Timer()

        with t:
            self.save =  pyradox.txt.parseFile(self.game_file)

        self.parse_time = t.interval

