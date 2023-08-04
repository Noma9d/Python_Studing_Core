def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)
    
       

def number_of_groups(n, k):
    Cnk=factorial(n)/((factorial(n-k))*factorial(k))

    return int(Cnk)


result = number_of_groups(50, 7)

print(result)

print(factorial(5))  

# Cnk = n! / ((n - k)! · k!)
