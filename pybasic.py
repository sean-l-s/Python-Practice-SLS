def arith_prod_cond(n1, n2):
    if n1 * n2 <= 1000:
        return n1 * n2
    else:
        return n1 + n2

def cumulative_sum(input_range):
    prev = 0
    sum = 0
    for i in range(input_range):
        sum = prev + i
        print(f"Current Number {i} Previous Number {prev} Sum: {sum}")

        prev = i
    return sum

def str_index_even_slice(input_str):
    for i in range(0, len(input_str)-1, 2):
        print(input_str[i])

def str_index_even_slice2(input_str):
    sliced = input_str[::2]
    for char in sliced:
        print(char)

def str_slice0n(string, n):
    return string[n:]

def var_swap(a, b):
    a, b = b, a
    return a, b

def factorial_loop(x):
    product = 1
    for i in range(x, 0, -1):
        product *= i
    return product

def list_add_remove(list):
    list.pop(1)
    list.append("fig")
    return(list)

def str_reverse(string):
    reversed_str = ""
    for i in range(len(string)-1, -1, -1):
        reversed_str += string[i]
    return reversed_str

def str_reverse2(string):
    reversed_str = string[::-1]
    return reversed_str

def vowel_freq_count(string):
    vowels = "aeiou"
    v_count = 0
    for i in string.lower():
        if i in vowels:
            v_count += 1
    return v_count

def find_extremes(list):
    current_large = list[0]
    current_small = list[0]

    # For largest
    for i in list:
        if i > current_large:
            current_large = i
        else:
            continue

    # For smallest
    for i in list:
        if i < current_small:
            current_small = i
        else:
            continue

    return current_large, current_small

def remove_dupes(input_list):
    new_list = []
    for i in input_list:
        if i not in new_list:
            new_list.append(i)
    return new_list

def remove_dupes2(input_list):
    return list(set(input_list))

def first_last_same(input_list):
    if input_list[0] == input_list[-1]:
        return True
    else:
        return False

def divisible_by_5(input_list):
    nums_divisible = []
    for num in input_list:
        if num % 5 == 0:
            nums_divisible.append(num)
    return nums_divisible