from pyradox.game.game import Game

nation = 'ENG'

game = Game("R:\\AE.eu4")

game.load()
game.parse()

print ("Time to load save: ", game.parse_time)

print("Nation: ", nation)

game.nations[nation].all_relations()

#for nation_name, nation in game.nations.items():
    #print("Nation: ", nation)
    #nation.all_relations()





