# 1 @ 1 = (1+1)+(1-1)+(1*1)+(1//1) = 4

def evaluate(equation):
    equation = equation.split()
    value = "null"

    def calculate(x,y):
        x, y = [int(x), int(y)]
        if y == 0: return None
        return ((x+y)+(x-y)+(x*y)+(x//y))

    for simbol in range(len(equation)):
        if equation[simbol] == "@" and value != None and value == "null":
            value = calculate(equation[simbol-1], equation[simbol+1])

        elif equation[simbol] == "@" and value != "null":
            value = calculate(value, equation[simbol+1])


    return(value)

print(evaluate("1 @ 1 @ 0"))