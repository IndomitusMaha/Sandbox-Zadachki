# summa do opredelennoi cifri
"""
def sum(x):
    if x== 0:
        return 0
    elif x == 1:
        return 1
    else:
        return x + sum(x-1)

z = sum(10)
print(z)"""

"""
def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)

print(factorial(4)) """

def fibanacci(x):
    ''' funcia vozvrashaiet cifru fibonacci poryadok
    kotoroi raven x'''
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibanacci(x-1) + fibanacci(x-2)

print(fibanacci(40))



