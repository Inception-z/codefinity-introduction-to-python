# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

def calculate_revenue(prices, quantities_sold):
    revenue = [prices[i] * quantities_sold[i] for i in range(len(prices))]
    return revenue

revenue = calculate_revenue(prices, quantities_sold)

def formatted_output(products, revenue):
    revenue_per_product = sorted(list(zip(products, revenue)))
    return revenue_per_product

revenue_per_product = formatted_output(products, revenue)

for product_name, revenue in revenue_per_product:
     print(f"{product_name} has total revenue of ${revenue}")





# Example of expected output line (do not remove):
   