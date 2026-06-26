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


