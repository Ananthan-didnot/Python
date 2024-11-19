

inventory=[
    ('Laptop',5,30000.00),
    ('Headphones',50,1000.00),
    ('mouse',10,3500.00),
    ('keyboard',15,1500.00),
    ('monitor',20,3000.00)
]
highest_stock_value=0
item_with_highest_stock_value=None
for item in inventory:
    item_name,quantity,price=item
    stock_value=quantity*price
    print(f"Total stock value of {item_name}={stock_value}")
    if stock_value>highest_stock_value:
        highest_stock_value=stock_value
        item_with_highest_stock_value=item_name
print(f"{item_with_highest_stock_value} has higest value:{stock_value}")




