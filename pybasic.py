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

def substring_freq_analysis(input_string, str_target):
    return input_string.count(str_target)

def nested_loop_pattern(input_range):
    input_range += 1
    for i in range(input_range):
        for j in range(i):
            print(i, end=" ")
        print()

def nested_loop_pattern2(input_range):
    for num in range(1, input_range+1):
        for i in range(num):
            print(num, end=" ")
        print()

def num_palindrome(num):
    usual = str(num)
    reverse = usual[::-1]
    return usual == reverse

def oddlist1_evenlist2(list1, list2):
    result = []
    for item in list1:
        if item % 2 != 0:
            result.append(item)
    for item in list2:
        if item % 2 == 0:
            result.append(item)
    return result

def digit_extract_reverse(input_int):
    while input_int > 0:
        digit = input_int % 10
        input_int //= 10
        print(digit, end=" ")

def multi_tier_tax(income):
    if income < 10000:
        return 0
    elif income < 20000:
        return (income - 10000) * 0.1
    else:
        income = income - 20000
        return 1000 + (income * 0.2)

def mult_table_nested(input_range):
    for i in range(1, input_range+1):
        for j in range(1, 11):
            print(j*i, end="\t")
        print()

def downward_half_pyramid(input_rows):
    for i in range(input_rows, 0, -1):
        for j in range(i):
            print("* ", end="")
        print()

def exponent(base, exp):
    result = 1
    for i in range(exp):
        result *= base
    return result

# Skipped Exercise 23 due to being similar to num_palindrome(num)

def fibonacci(steps):
    num1 = 0
    num2 = 1
    for i in range(steps):
        print(num1, end=" ")
        res = num1 + num2
        num1 = num2
        num2 = res

def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

def merge_two_dicts(dict1, dict2):
    return dict1 | dict2

def find_common_elems(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1 & set2

def split_odd_even(list_num):
    even_list = []
    odd_list = []
    for num in list_num:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)
    return even_list, odd_list

def word_length_analysis(input_list):
    for word in input_list:
        print(f"{word} - {len(word)}", end=" ")

def histogram(text):
    word_list = text.split()
    word_counter = {}
    for word in word_list:
        if word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1
    return word_counter

def print_alternate_primes(limit):
    prime_list = []
    for i in range(2, limit+1):
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                break
        else:
            prime_list.append(i)
    alt_primes = prime_list[::2]
    print(alt_primes)


def dict_of_squares(start_range, end_range):
    square_dict = dict()
    for i in range(start_range, end_range+1):
        square_dict[i] = i**2
    return square_dict

def char_replace_underscore(sentence, char_to_change):
    return(sentence.replace(char_to_change, "_"))

def reverse_nested_loop_pattern(input_range):
    for num in range(input_range, 0, -1):
        for i in range(num, 0, -1):
            print(i, end=" ")
        print()

def digit_detection(input_string):
    for char in input_string:
        if char.isdigit():
            return True

def capitalize_first_letter(input_text):
    list_words = input_text.split()
    new_list = []
    for word in list_words:
        new_list.append(word.capitalize())
    return(" ".join(new_list))

def simple_countdown_timer(start_count):
    while start_count > 0:
        print(start_count, end=" ")
        start_count -= 1
    print("Blast off!")

def file_creation_basic_io(): 
    filename = "notes.txt"

    with open(filename, "w") as f:
        f.write("Hello, this is my first note.\n")
        f.write("Python file handling is simple.\n")
        f.write("End of file.")
    with open(filename) as f:   # No need for "r" to read it, apparently
        print(f.read())

def ext_file_word_counter(text_file):
    try:
        with open(text_file, "r") as f:
            data = f.read()
            words = data.split()
            word_count = len(words)
            print(f"The file contains {word_count} words.")
    except FileNotFoundError:
        print("Error: The file {text_file} was not found.")

