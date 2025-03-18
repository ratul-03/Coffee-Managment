# Define the menu with item names as keys and their prices as values
menu = {
  'Pizza': 40,
  'Pasta': 50,
  'Burger': 60,
  'Salad': 70,
  'Coffee': 80
}

# Display the welcome message and available menu items with prices
print("Welcome to our hotel")
print("Pizza: 40tk, \nPasta: 50tk, \nBurger: 60tk, \nSalad: 70tk, \nCoffee: 80tk")

# Initialize total_order variable to keep track of the total cost
total_order = 0

# Take the first order input from the user
item1 = input("Enter a menu item that you want to order: ")

# Ask the user if they want to order anything else
item2 = input("Anything else that you want to order? (Yes/No): ")

# Check if the first item exists in the menu
if item1 in menu:
    total_order += menu[item1]  # Add the item's price to the total order
    print(f"Your item {item1} has been added to the cart")  # Confirm order
else:
    print(f"Order item {item1} is not available")  # Inform user if the item is unavailable

# If the user wants to order another item
if item2 == 'Yes':
    item3 = input("Enter another menu item that you want to order: ")
    
    # Check if the second item exists in the menu
    if item3 in menu:
        total_order += menu[item3]  # Add the second item's price to the total order
        print(f"Your item {item3} has been added to the cart")  # Confirm order
    else:
        print(f"Order item {item3} is not available")  # Inform user if the item is unavailable

# Display the final total amount
print(f"The total amount is {total_order} tk.")
