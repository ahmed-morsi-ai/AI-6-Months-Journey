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



