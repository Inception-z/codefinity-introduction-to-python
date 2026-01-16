prices = [29.99, 45.50, 12.75, 38.20]

for i in range(len(prices)):
    if i == 0:
        prices[i] = prices[i] * 0.9
    elif i == 1:
        prices[i] = prices[i] * 0.8
    elif i == 2:
        prices[i] = prices[i] * 0.85
    elif i == 3:
        prices[i] = prices[i] * 0.95

    print(f"Updated price for item {i + 1}: ${prices[i]:.2f}")

        
        


