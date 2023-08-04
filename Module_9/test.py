# def interval_generator(x, y):
#     while x <= y:
#         yield x
#         x += 1


# five_to_ten_generator = interval_generator(5, 10)
# for i in five_to_ten_generator:
#     print(i)


# div = lambda x, y : x / y

# print(div(4, 2))


# some_str = 'aaAbbB C F DDd EEe'
# res = ''
# for i in filter(lambda x: x.islower(), some_str):
#     res += i

# print(res)



# def logged(func):
#     def wrapper(x, y):
#         print(f'our x: {x}')
#         result = func(x, y)
#         print(f'our y: {y}')
#         print(f'x + y = {x + y}')
#         return result
#     return wrapper

# @logged
# def mul(x, y):
#     return x * y

# @logged
# def add(x, y):
#     return x - y

# print(add(6, 1))

# print(mul(2, 2))

def rang(x, y):
    while x <= y:
        yield x
        x += 1

ran = rang(1, 5)

for i in ran:
    print(i)