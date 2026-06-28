def apply_store_discount (prices_list):
    final_prices = []
    for price in prices_list:
        if price >= 200:
            discounted_price = price * 0.8
            final_prices.append(discounted_price)
        else:
           final_prices.append(price)
    return final_prices
sahar_catalog = [100, 250, 80, 400, 150]
updated_catalog = apply_store_discount(sahar_catalog)
print(updated_catalog)


#التحدي الأول: محرك البحث المصغر The Mini Search Engine

def search_inventory(catalog, target_item):
    catalog = [target_item]
    for item in catalog:
        if item == target_item:
            print(f"Item Found!")
    return search_inventory(catalog, target_item)
sahar_products = ["Oud", "Musk", "Rose", "Amber"]
search_inventory(sahar_products, "Rose")
search_inventory(sahar_products, "Vanilla")
