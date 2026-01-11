# The item's discount and stock status have been defined
discounted = False
lowStock = True
movingProduct = not discounted or lowStock
promotion = discounted and not lowStock
print(f"Is the item eligible for promotion? {promotion}")