# Restaurant Ordering System

## Description
This is a simple Python script that allows users to place orders from a predefined menu. The script prompts the user to order an item, checks its availability, and calculates the total price. It also allows the user to add another item if they wish.

## Features
- Displays a menu with item names and prices.
- Takes user input for ordering items.
- Checks if the ordered item is available in the menu.
- Allows users to order a second item if they choose to.
- Calculates and displays the total order cost.

## Prerequisites
- Python 3 installed on your system.

## How to Run
1. Clone this repository or download the `main.py` file.
2. Open a terminal or command prompt.
3. Navigate to the directory where the script is located.
4. Run the script using the following command:
   ```bash
   python main.py
   ```
5. Follow the on-screen instructions to place your order.

## Menu
| Item   | Price (tk) |
|--------|----------|
| Pizza  | 40       |
| Pasta  | 50       |
| Burger | 60       |
| Salad  | 70       |
| Coffee | 80       |

## Example Usage
```
Welcome to our hotel
Pizza: 40tk,
Pasta: 50tk,
Burger: 60tk,
Salad: 70tk,
Coffee: 80tk

Enter a menu item that you want to order: Pizza
Anything else that you want to order? (Yes/No): Yes
Enter another menu item that you want to order: Coffee
Your item Pizza has been added to the cart
Your item Coffee has been added to the cart
The total amount is 120 tk.
```

## Future Improvements
- Allow multiple orders dynamically using loops.
- Make input case-insensitive.
- Improve error handling for invalid inputs.

## License
This project is open-source and available under the MIT License.
