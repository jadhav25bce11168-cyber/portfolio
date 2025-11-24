
# Project Title

A🛒 Inventory & Pricing Management System(INR)
A robust, command-line interface (CLI) Python application designed for small businesses or personal use to track stock levels, manage wholesale/retail pricing, and calculate potential profits. This system is specifically formatted for Indian Rupees (₹). 




## Features

- Stock Management: Add new items or restock existing inventory easily.
- Price Tracking: Stores both Wholesale (Cost Price) and Retail (Selling Price) for every item.
- INR Formatting: All financial figures are automatically formatted with the Indian Rupee symbol (₹) and two decimal places.
- Profit Calculation: Automatically calculates and displays the profit margin per unit for every item in the inventory view.
- Robust Input Validation: Prevents crashes by ensuring users enter valid numbers (e.g., prevents entering negative prices or text where numbers are required).
- Sales Logic: Calculates total sale value upon checkout and prevents selling more items than are currently in stock.


## Prerequisites
- Python 3.12.4 installed on your system.
- No external libraries are required (uses standard sys library).
## How to Run
1.Save the code: Save the Python script as inventory_system.py.
2.Open Terminal/Command Prompt: Navigate to the folder where you saved the file.
3.Run the command:

## Usage/Examples

Upon running the program, you will see the following menu:
1. View Inventory
Displays a formatted table showing:

- Item Name

- Current Quantity

- Wholesale Price (₹)

- Retail Price (₹)
- Profit per unit (₹) (Calculated as Retail - Wholesale)
2. Add Stock
- New Items: If you enter a name that doesn't exist, the system will ask for the Initial Quantity, Wholesale Price, and Retail Price.

- Existing Items: If the item already exists, the system will only ask for the quantity to add (prices remain unchanged).
3. Sell Stock
- Enter the name of the item to sell.

- The system displays the current Retail Price and Stock Level.

- Enter the quantity to sell.

- -Output: The system calculates the Total Sale Amount (Price × Quantity) and updates the inventory.

- Note: If stock reaches 0, the item is removed from the list.
4. Exit
Closes the application.

## Technical Details
Data Structure
The data is stored in a nested Python dictionary format for fast lookups:

inventory = {
    "apple": {
        "quantity": 50,
        "wholesale": 80.00,
        "retail": 120.00
    },
    "notebook": {
        "quantity": 20,
        "wholesale": 30.50,
        "retail": 45.00
    }
}

## Functions
- get_positive_integer() / get_positive_float(): Error handling wrappers to ensure clean user input.

- view_inventory(): Iterates through the dictionary and uses f-strings for table formatting.

- add_stock(): Logic to distinguish between updating quantities vs. creating new records.

- remove_stock(): Logic to validate stock availability before processing a "sale."
## Important Notes
This program uses Runtime Memory. This means the inventory data is stored in variables while the program is running. If you close the program, the data will be reset.

(To make data persistent, future versions would require file handling using CSV, JSON, or a database).