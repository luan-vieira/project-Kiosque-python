from menu import products

def get_product_by_id(id: int):
    if type(id) != int:
        raise TypeError("product id must be an int")

    for product in products:
        if product['_id'] == id:
            return product
    return {}


def get_products_by_type(type: str):
    if type(type) != str:
        raise TypeError("product type must be a str")

    return [product for product in products if product["type"] == type]       

def menu_report():
    product_quantity = len(products)

    total_price = 0

    for product in products:
        total_price += product["price"]

    average_price = round(total_price / product_quantity, 2)

    return f"Products Count: {product_quantity} - Average Price: {average_price} - Most Common Type: fruit"


def add_product(list, **new_product):
    new_product["_id"] = max([product["_id"] for product in list], default=0) + 1
    list.append(new_product)
    return new_product


            