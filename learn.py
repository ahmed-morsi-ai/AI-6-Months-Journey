sahar_products = ["Oud", "Musk", "Rose", "Amber"]


def search_inventory(catalog, target_item):
    for item in catalog:
        if item == target_item:
            print("Item Found!")
            return True
    return False


result = search_inventory(sahar_products, "Rose")
search_inventory(sahar_products, "Vanilla")
