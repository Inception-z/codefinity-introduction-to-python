grocery_inventory = {
    "Milk" : ("Dairy", 3.50, 8),
    "Eggs" : ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50)   
}

egg_price = grocery_inventory["Eggs"][1]
if egg_price > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    new_eggs = (
    grocery_inventory["Eggs"][0],  # category
    egg_price - 1,                 # reduced price
    grocery_inventory["Eggs"][2],  # stock
)
    grocery_inventory["Eggs"] = new_eggs

else:
    print("The price of Eggs is reasonable.")

grocery_inventory.update({"Tomatoes" : ("Produce", 1.20, 30)})

print(f"Inventory after adding Tomatoes: {grocery_inventory}")

milk_stock = grocery_inventory["Milk"][2]
if milk_stock < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    new_milk = (
        grocery_inventory["Milk"][0],
        grocery_inventory["Milk"][1],
        milk_stock + 20
    )
    grocery_inventory["Milk"] = new_milk
else:
    print("Milk has sufficient stock")

apple_price = grocery_inventory["Apples"][1]
if apple_price > 2:
    grocery_inventory.pop["Apples"]
    print("Apples removed from inventory due to high price.")

print(f"Updated inventory: {grocery_inventory}")