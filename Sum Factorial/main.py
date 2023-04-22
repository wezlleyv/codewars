def sum_factorial(lst):
    def fac(integer):
        value = 1
        for x in range(0,integer):
            value *= integer-x
        return value
    value = 0
    for x in lst:
        value += fac(x)
    
    return value


if sum_factorial([4,9]) == 362904:
    print("pass")