prices = [150, 450, 80, 200]
categories = []
for price in prices:
    if price >=200:
        categories.append("VIP")
    elif price <200:
        categories.append("Normal")
print ("the categories are:", categories)
