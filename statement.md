 Inventory & Pricing System (INR)

 Problem Statement

Small businesses and individual retailers require a simple, local tool to efficiently manage their product stock levels and pricing information. This tool must:

Accurately track item quantities.

Store both wholesale and retail prices in a fixed currency (Indian Rupees, ₹).

Calculate the potential profit margin per item.

Provide clear, formatted reports for viewing current stock and profit figures.

Distinguish between adding a new item (which requires setting prices) and restocking an existing item (which only requires updating quantity).

The challenge is to provide this functionality in a robust, command-line interface using fundamental Python data structures and input validation techniques.

 Scope of the Project

The Inventory & Pricing System is a minimalist, command-line utility designed purely for in-session inventory management and pricing simulation.

In Scope:

In-Memory Data Storage: All inventory data is stored in a Python dictionary (inventory) for the duration of the current session. Data is volatile and is lost upon program exit.

CRUD-like Operations: Functionality to add/restock items, sell items (reduce stock), and view all current stock.

Pricing Logic: Stores and displays prices and calculates profit margin (retail - wholesale).

Currency: All transactions and displays are fixed to Indian Rupees (₹).

Input Validation: Ensures user inputs for quantity are positive integers and prices are positive floats.

Out of Scope:

Data Persistence (no file saving, database integration, or session logging).

User Authentication or multi-user support.

Complex features like bulk discounts, vendor tracking, or order management.

Reporting beyond the single, detailed inventory list.

 Target Users

Small Shop Owners/Inventory Clerks: Individuals managing small, localized inventory who need a quick, no-frills method to track stock levels and gross profit margins.

Educational Users/Learners: Students and developers learning advanced Python I/O, function modularity, dictionary manipulation, and basic input validation.

Demonstrators: Anyone needing a clean, simple example of CRUD operations on in-memory dictionary data structures.

 High-Level Features

Feature

Description

Session-Based Inventory

Stores all item name, quantity, and pricing data within a persistent dictionary for the current session.

Smart Stock Addition

When adding stock, it automatically identifies if the item is new (prompts for wholesale/retail price) or existing (only prompts for quantity).

Sale Value Calculation

When stock is removed (sold), the system calculates and displays the total sales value generated for that specific transaction.

Profit Transparency

The "View Inventory" function clearly calculates and displays the profit margin (Wholesale vs. Retail) for every item.

Robust Input Handling

Dedicated helper functions (get_positive_integer, get_positive_float) ensure numerical data is entered correctly and prevents negative quantities or prices.

Formatted Output

Presents the inventory data in a clean, table format with appropriate alignment and the Indian Rupee symbol (₹).