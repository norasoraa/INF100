from uke_09_oppg_9 import displayInventory

def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item in inventory:
            inventory[item] += 1
        else: 
            inventory[item] = addedItems.count(item)
    return inventory

inv = {"gold coin": 42, "rope": 1}
dragonLoot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]
inv = addToInventory(inv, dragonLoot)
print(displayInventory(inv))