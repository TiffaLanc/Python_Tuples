# Task 1: Customer Order Processing Refine your skills in tuple unpacking by managing customer orders.

# Problem Statement: You are given a list of tuples, each representing a customer's order. 
# Each tuple contains the customer's name, the product ordered, and the quantity. 
# Your task is to unpack each tuple and print the order details in a user-friendly format.
# - Write a function to iterate over the list of orders. - Unpack each tuple in the list and format the details for display.

# Sample Order Data:

orders_tot = [ ("Alice", "Laptop", 1), ("Bob", "Camera", 2), ("Lisa", "Keyboard", 4), ("Axel", "Mouse", 6)]

def orders_unpacked(orders):
    for order in orders:
        name, product, quantity = order
        print(f"\nCustomer Order:\n{name} - {product}: {quantity}")                                                                 #printing off the tuples in a formatted way

orders_unpacked(orders_tot)