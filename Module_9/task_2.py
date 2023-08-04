DEFAULT_DISCOUNT = 0.05


def get_discount_price_customer(price, customer):
    if customer.get('discount') == None:
        return price * (1 - DEFAULT_DISCOUNT)
    else:
        return price * (1 - customer.get('discount'))
    



print(get_discount_price_customer(100, {"name": "Dima"}))

print(get_discount_price_customer(100, {"name": "Boris", "discount": 0.15}))