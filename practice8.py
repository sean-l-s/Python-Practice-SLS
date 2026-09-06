def str_reverse(input_str):
    reversed_str = ""
    for i in range(len(input_str)-1, -1, -1):
        reversed_str += input_str[i]
    return reversed_str

def str_reverse2(input_str):
    reversed_str = input_str[::-1]
    return reversed_str

if __name__ == "__main__":
    print(str_reverse2("Python"))