def test(a, b, *arg, **cwarg):
    return cwarg


result = test(2, 3, 2 ,2 ,2, t=123, c=233 )

print(result['c'])

