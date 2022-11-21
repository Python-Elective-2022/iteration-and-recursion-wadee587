'''
iterativePower is a base and exponential function.
    if the base power is equal to 0 
        the result is equal to 1
    else the base will multiply with the exponent
print base 1 and exponent 2 in iterativePower.

'''

def iterativePower(base, exp):
    if exp == 0:
        return 1
    else:
        OriginalBase = base
        for i in range (exp - 1):
            base = OriginalBase
        return base

print(iterativePower(1,2))

'''
recursivePower ia a base and exponential function
    if the base power is equal to 0 
        the result is equal to 1
    else the base will multiply with the exponent
print base 1 and exponent 2 in recursivePower.

'''

def recursivePower(base, exp):
    if exp == 0:
        return 1
    else:
        return base (recursivePower(base, exp - 1))

print(recursivePower(1,2))