number = 5

def loop_factorial(x):
    product = 1
    for i in range(x, 0, -1):
        product *= i
    return product

if __name__ == "__main__":
    print(f"The factorial of 5 is {loop_factorial(number)}")
    