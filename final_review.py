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


