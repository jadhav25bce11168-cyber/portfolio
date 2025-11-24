import sys

# Format: { "item_name": { "quantity": int, "wholesale": float, "retail": float } }
inventory = {}

def get_positive_integer(prompt):
    """Ensures valid whole numbers (for quantity)."""
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Error: Quantity cannot be negative. Try again.")
            else:
                return value
        except ValueError:
            print("Error: Invalid input. Please enter a whole number.")

def get_positive_float(prompt):
    """Ensures valid decimal numbers (for prices)."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Error: Price cannot be negative. Try again.")
            else:
                return value
        except ValueError:
            print("Error: Invalid input. Please enter a number (e.g., 10.50).")

def view_inventory():
    """Displays quantity AND prices in Indian Rupees."""
    print("\n" + "="*76)
    # Added (₹) to the headers
    print(f"{'Item Name':<15} | {'Qty':<8} | {'Wholesale(₹)':<13} | {'Retail(₹)':<10} | {'Profit(₹)'}")
    print("-" * 76)
    
    if not inventory:
        print("(Inventory is currently empty)")
    else:
        for item, data in inventory.items():
            qty = data['quantity']
            w_price = data['wholesale']
            r_price = data['retail']
            profit = r_price - w_price
            
            # Added ₹ symbol to the numbers
            print(f"{item.title():<15} | {qty:<8} | ₹{w_price:<12.2f} | ₹{r_price:<9.2f} | ₹{profit:<.2f}")
    print("="*76 + "\n")

def add_stock():
    """Asks for prices ONLY if the item is new."""
    print("\n--- Add / Restock Items ---")
    item_name = input("Enter item name to add: ").strip().lower()
    
    if not item_name:
        print("Error: Item name cannot be empty.")
        return

    if item_name not in inventory:
        # If it's a NEW item, ask for all details
        print(f"New item detected! Please set details for '{item_name.title()}'.")
        quantity = get_positive_integer(f"Enter initial quantity: ")
        
        # Updated prompts to specify INR
        wholesale = get_positive_float(f"Enter WHOLESALE price (₹): ")
        retail = get_positive_float(f"Enter RETAIL price (₹): ")
        
        # Create the nested dictionary
        inventory[item_name] = {
            "quantity": quantity, 
            "wholesale": wholesale, 
            "retail": retail
        }
        print(f"Success! {item_name.title()} added to database.")
        
    else:
        # If item EXISTS, just add quantity (Prices stay the same)
        print(f"'{item_name.title()}' exists. Updating stock level only.")
        quantity_to_add = get_positive_integer(f"Enter quantity to add: ")
        inventory[item_name]['quantity'] += quantity_to_add
        print(f"Success! Stock updated. Total: {inventory[item_name]['quantity']}")

def remove_stock():
    """Reduces stock and calculates Sale Value in Rupees."""
    print("\n--- Remove Stock (Sale/Usage) ---")
    if not inventory:
        print("Error: Inventory is empty.")
        return

    item_name = input("Enter item name to sell: ").strip().lower()

    if item_name not in inventory:
        print(f"Error: Item '{item_name.title()}' not found.")
        return

    current_qty = inventory[item_name]['quantity']
    # Show price to user before selling
    print(f"Selling: {item_name.title()} (Price: ₹{inventory[item_name]['retail']})")
    print(f"Current Stock: {current_qty}")
    
    quantity_to_remove = get_positive_integer("Enter quantity to sell: ")

    if quantity_to_remove > current_qty:
        print(f"Error: Cannot sell {quantity_to_remove}. Only {current_qty} in stock.")
    else:
        inventory[item_name]['quantity'] -= quantity_to_remove
        
        # Calculate Total Sale Amount
        total_sale_value = quantity_to_remove * inventory[item_name]['retail']
        
        print(f"Success! Sold {quantity_to_remove} items.")
        print(f"Total Sale Amount: ₹{total_sale_value:.2f}")
        
        if inventory[item_name]['quantity'] == 0:
             del inventory[item_name]
             print(f"Item is out of stock and removed.")

def main():
    while True:
        print("\n=== INVENTORY & PRICING SYSTEM (INR) ===")
        print("1. View Inventory")
        print("2. Add Stock (Sets Price for New Items)")
        print("3. Sell Stock")
        print("4. Exit")
        
        choice = input("Enter choice: ")

        if choice == '1': view_inventory()
        elif choice == '2': add_stock()
        elif choice == '3': remove_stock()
        elif choice == '4': sys.exit()
        else: print("Invalid choice.")

if __name__ == "__main__":
    main()