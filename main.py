import pybasic

if __name__ == "__main__":
    num_list = [10, 20, 33, 46, 55]
    print("Divisible by 5:")
    divisible = pybasic.divisible_by_5(num_list)
    for i in divisible:
        print(i, end=" ")