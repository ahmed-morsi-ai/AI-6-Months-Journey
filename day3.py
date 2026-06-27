prices = [60,100,200,275.5,199,300]
print("the prices are:",prices)
for price in prices:
    if price >=344 or price <=0:
        print("the price is outside the valid range:", price)
    elif price >=300:
        category = "Ultra Quality"
    elif price >=200:
        category = "High Quality"
    elif price >=100:
        category = "Medium Quality"
    else:
        category = "Standard Quality"
    print (f"the price {price} is category {category}")
print ("---classification complete---")
print (len (prices))
stock = 6
while stock > 0:
    print (f"product sold, remaining {stock}")
    stock -= 1 
    # ادريب 1
    prices = [15, 0, 120, 5, 45]
print("---Product List---")
for item in prices:
    print(item)
    if item == 0:
        print("Out of Stock - Urgent Restock!")
    elif item <= 10:
        print("Low Stock - Almost sold out.")
    else:
        print("In Stock")

# تدريب 2 


exclusive_stock = 3
while exclusive_stock > 0:
    print(f"Exclusive Perfume Sold! Remaining stock: {exclusive_stock}")
    exclusive_stock -= 1
print("The Exclusive Edition is Completely Sold Out!")
 # تدريب 3 
Orders = [150,450,80,1200,200]
total_revenue = 0
for order in Orders:
    if order >= 400:
        print ("VIP Order : Add Luxury Gift Box")
        total_revenue += order
    elif order <100:
        print ("Small Order : Add 15 Shipping Fee")
        total_revenue += order + 15
    else:
        print ("Standard Order : Free Shipping")
        total_revenue += order
print (" Total revenue For Today Is :", total_revenue) 
# تدريب 4 

prices = [150, 450, 80, 200]
categories = []
for price in prices:
    if price >=200:
        categories.append("VIP")
    elif price <200:
        categories.append("Normal")
print ("the categories are:", categories)

# تدريب 5 
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

