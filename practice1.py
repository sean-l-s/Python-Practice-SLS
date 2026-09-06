number1 = 40
number2 = 30


def logic(x, y): 
    if x * y <= 1000:
        return x * y
    else:
        return x + y

print(logic(number1, number2))