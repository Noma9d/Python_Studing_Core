def cost_delivery(*quantity, discount=0):
    cost=5+(quantity[0]-1)*2 - (5+(quantity[0]-1)*2)*discount
    return cost


print(cost_delivery(2, 1, 2, 3, discount=0.5))


# def cost_delivery(quantity, *_, discount=0):
#     Функция возвращает общую сумму доставки.
    
#     Первый параметр &mdash; количество товаров в заказу.
#     Параметр скидки discount, передаваемый только по ключу, по умолчанию имеет значение 0.

    
    
#     result = (5 + 2 * (quantity - 1)) * (1 - discount)
#     return result