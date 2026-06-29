def all_sales(cart):
    total_bill = 0.0  
    
    for item_name, item_price in cart.items():
        
        if item_price >= 450:
            discounted_price = item_price * 0.8
            print("Discount applied to VIP item:", item_name)
            total_bill += discounted_price 
        else:
            total_bill += item_price      
    return total_bill

customer_cart = {
    "Oud Royal": 450,
    "Pure Musk": 180,
    "Amber Night": 320
}

final_amount = all_sales(customer_cart)
print("Total Amount to Pay:", final_amount)