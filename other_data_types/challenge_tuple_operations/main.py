# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")
apple_count = shelf.count("apples")
print(f'Number of Apples: {apple_count}')

if apple_count < 5:
    print("Apples need to be restocked.")
else:
    print("Apples are sufficiently stocked.")

banana_index = shelf.index("bananas")
print(f'First Banana Index: {banana_index}')

if shelf.count("grapes") == 1:
    print("Grapes need to be restocked.")
else:
    print("Grapes are sufficiently stocked.")


orange_index = shelf.index("oranges")
if "oranges" in shelf:
    print(f"Oranges are at index: {orange_index}")
else:
    print("Oranges are out of stock.")

