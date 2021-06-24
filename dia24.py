""" Día 24."""

from prettytable import PrettyTable

table = PrettyTable()
pokemones = {"Pikachu" : "Electric", "Squirtle" : "Water", "Charmander" : "Fire"}
table.add_column("Pokemon Name", [x for x in pokemones.keys()])
table.add_column("Type", [x for x in pokemones.values()])
table.align = "l"
print(table)