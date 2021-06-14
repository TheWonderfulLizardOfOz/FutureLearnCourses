from character import Character, Enemy
from item import Item
inventory = []
dave = Enemy("Dave", "A smelly zombie")
dave.set_steal("cheese")
stolen_item = dave.steal()
inventory.append(stolen_item)


