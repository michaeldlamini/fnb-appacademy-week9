
foods = []
prices = []

while True:
    food = input("Enter a food to buy or press 'q' to quit: ")
    if food.lower() == 'q':
        break
    try:
        price = float(input(f"Enter the price of {food}: R"))
        foods.append(food)
        prices.append(price)
    except ValueError:
        print("Please enter a valid number for the price.")

# Display the shopping cart
print("\n----- YOUR SHOPPING CART -----")
total = 0
for i in range(len(foods)):
    print(f"{foods[i]} - R{prices[i]:.2f}")
    total += prices[i]

print(f"\nTotal: R{total:.2f}")
