inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]
inventory_len = len(inventory)
first = inventory[0]
last = inventory[-1]
inventory_2_6 = inventory[2:6]
first_3 = inventory[:3]
twin_beds = inventory.count("twin bed")
# removes the 5th element from list and puts it in new variable
removed_item = inventory.pop(4)
# inserting a new element in the 11th position
inventory.insert(10, "19th Century Bed Frame")
inventory.sort()
print(inventory)