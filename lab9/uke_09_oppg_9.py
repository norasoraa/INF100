def displayInventory(inventory):
    print("Inventory:")
    total_number = 0
    for key in inventory.keys():
        number = inventory[key]
        print(number, key)
    for value in inventory.values():
        total_number += int(value)
    return total_number
    
stuff = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}
print(displayInventory(stuff))