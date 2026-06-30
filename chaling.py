morsi_goods_inventory = {
    "food": {"Rice": 10, "Pasta": 15, "Bread": 20, "Olive Oil": 25},
    "beverages": {"Coffee": 30, "Tea": 35, "Juice": 40, "Water": 45},
    "snacks": {"Chips": 50, "Nuts": 55, "Chocolate": 60, "Cookies": 65}
}

def process_order(requested_items, inventory):
    total_bill = 0
    for item in requested_items:
        item_found = False
        for category in inventory.values():
            if item in category and category[item] > 0:
                total_bill += category[item]
                category[item] -= 1
                print(f"Added {item} to cart")
                item_found = True
                break
        if not item_found:
            print(f"Sorry, {item} is out of stock!")
    return total_bill

customer_order = ["Rice", "Coffee", "Chips", "Olive Oil", "Tea", "Chocolate"]
final_amount = process_order(customer_order, morsi_goods_inventory)

print("-" * 20)
print("Total Amount to Pay:", final_amount)
print("Total Amount to Pay:", final_amount)
print("Updated Inventory for Beverages:", morsi_goods_inventory["beverages"]["Coffee"])