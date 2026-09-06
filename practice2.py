def sample():
    sum = 0
    print("Printing current and previous number sum in a range(10)")
    for i in range(10): 
        if i == 0:
            sum = 0
            print(f"Current Number 0 Previous Number 0  Sum: {sum}")
        else:
            sum = i + (i-1)
            print(f"Current Number {i} Previous Number {i-1}  Sum: {sum}")

if __name__ == "__main__":
    sample()