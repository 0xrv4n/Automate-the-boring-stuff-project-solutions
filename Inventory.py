# You are creating a fantasy video game. The data structure to model the
# player’s inventory will be a dictionary where the keys are string values
# describing the item in the inventory and the value is an integer value detail-
# ing how many of that item the player has.

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayinventory(inventory):
	print('Inventory:')
	total_items = 0
	for k, v in inventory.items():
		print(v, k)
		total_items += v
	print('Total number of items: ' + str(total_items))

display = displayinventory(stuff)


# List to Dictionary Function for Fantasy Game Inventory
# Write a function named addToInventory(inventory, addedItems) , where the
# inventory parameter is a dictionary representing the player’s inventory (like
# in the previous project) and the addedItems parameter is a list like dragonLoot .
# The addToInventory() function should return a dictionary that represents the
# # updated inventory.

def addToInventory(inventory, addedItems):
	print('Inventory:')
	for item in addedItems:
		inventory.setdefault(item, 0)
		inventory[item] += 1
	return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
uptd_inv = addToInventory(inv, dragonLoot)
displayinventory(uptd_inv)

