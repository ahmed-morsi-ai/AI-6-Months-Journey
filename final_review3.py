stock = 5
orders = [250, -10, 400, 0, 150, 500, 300, 200]
successful_sales = []
failed_orders = []

for order in orders:
    if order <= 0:
        print(f"Alert: Invalid order with value {order} was rejected.")
        failed_orders.append(order)
        
    elif stock > 0:
        print(f"Success: A perfume was sold for {order}. Remaining stock: {stock - 1}")
        successful_sales.append(order)
        stock -= 1  
        
    else:
        print(f"Sorry, we were unable to fulfill the order for {order} due to out-of-stock items.")
        failed_orders.append(order)

print("--- Final Report ---")
print("Successful sales:", successful_sales)
print("Rejected orders:", failed_orders)