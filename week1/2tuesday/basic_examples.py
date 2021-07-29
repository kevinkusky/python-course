# Formatting Strings
name = input("What is your name?\n")

# concat
print("Hi, " + name + ".")

# %s - indicated output is string
# % name - value to be outputted
print("Hi, %s." % name)

# {0} - order of variables into format
# 0 indexed - mult {0} {1} {2} ...  
print("Hi, {0}.".format(name))

# Python formatted string
print(f'Hi, {name}.')

# print("** Doubling Penny **")

# # How many times would a penny need to double to generate a million dollars?
# count = 0
# total = 0

# # STEP 2: Write the while loop

# while total < 1000000:
#   count += 1
#   if total == 0:
#     total += 0.01
#   else:
#     total *= 2

# print('Double', count, 'times')

# # How much money has been generated at that point?
# print('${:,}'.format(total))


"""
This is a simple script to practice creating a few functions in Python

Please follow the steps outlined below.
"""

# STEP 1 - Write a function named `welcome` that prints a welcome message


def welcome():
    print("welcome, ya'll")


# # Step 2 - Write a function named `calc_sum` that
# #   - takes in two numbers and
# #   - returns their sum


def calc_sum(n1, n2):
    return n1 + n2


# # DO NOT EDIT - The guts of the program
# welcome()
# print(calc_sum(1, 2), "is 3?", calc_sum(1, 2) == 3)
# print(calc_sum(-10, -2), "is -12?", calc_sum(-10, -2) == -12)
# print(calc_sum(1.1, -2.2), "is -1.1?", calc_sum(1.1, -2.2) == -1.1)
# print(calc_sum("a", "b"), "is ab?", calc_sum("a", "b") == "ab")
# print(
#     calc_sum([1, 2], [3, 4]), "is [1,2,3,4]?", calc_sum([1, 2], [3, 4]) == [1, 2, 3, 4]
# )

# Define your function "addition" here


def addition(n1, n2):
    return n1 + n2


# print(addition(2, 3))  # > 5
# print(addition(-3, -6))  # > -9
# print(addition(7, 3))  # > 10

# Write your function, here.
# Parameters are in this order: chickens, cows, pigs


def how_many_legs(chk, cow, pig):
    return (chk * 2) + 4 * (cow + pig)


# print(how_many_legs(2, 3, 5))  # > 36
# print(how_many_legs(1, 2, 3))  # > 22
# print(how_many_legs(5, 2, 8))  # > 50


def string_int(str):
    return int(str)


# print(string_int("6"))  # > 6
# print(string_int("1000"))  # > 1000
# print(string_int("12"))  # > 12

# Write your function, here.


def calculate_exponent(b, e):
    return b ** e


# print(calculate_exponent(5, 5))  # > 3125
# print(calculate_exponent(10, 10))  # > 10000000000
# print(calculate_exponent(3, 3))  # > 27

# Write your function, here.


def And(test1, test2):
    return test1 and test2


# print(And(True, False))  # > False
# print(And(True, True))  # > True
# print(And(False, True))  # > False
# print(And(False, False))  # > False

# Write your function, here.


def long_burp(length):
    r_train = "r" * length
    return f"Bu{r_train}p"


# print(long_burp(3))  # > "Burrrp"
# print(long_burp(5))  # > "Burrrrrp"
# print(long_burp(9))  # > "Burrrrrrrrrp"


# Write your function, here.


def cap_space(str):
    length = len(str)
    i = 0
    formatted = ""

    while i < length:
        if str[i].isupper():
            formatted += f" {str[i]}"
        else:
            formatted += str[i]
        i += 1

    return formatted


# print(cap_space("helloWorld"))  # > "hello world"
# print(cap_space("iLoveMyTeapot"))  # > "i love my teapot"
# print(cap_space("stayIndoors"))  # > "stay indoors"


# Write your function, here.


def concat_name(fname, lname):
    return f"{lname}, {fname}"


# print(concat_name("First", "Last"))  # > "Last, First"
# print(concat_name("John", "Doe"))  # > "Doe, John"
# print(concat_name("Mary", "Jane"))  # > "Jane, Mary"

# Write your function, here.


def char_count(char, string):
    return string.count(char)


# print(char_count("a", "App Academy"))  # > 1
# print(char_count("c", "Chamber of Secrets"))  # > 1
# print(char_count("b", "big fat bubble"))  # > 4


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


# print(factorial(1))  # > 1
# print(factorial(8))  # > 40320
# print(factorial(12))  # > 479001600


def divisible_by_five(num):
    return num % 5 == 0


# print(divisible_by_five(5))  # > True
# print(divisible_by_five(-55))  # > True
# print(divisible_by_five(37))  # > False


def is_last_char_n(string):
    return string.endswith("n")


# print(is_last_char_n("Aiden"))  # > True
# print(is_last_char_n("Piet"))  # > False
# print(is_last_char_n("Bert"))  # > False
# print(is_last_char_n("Dean"))  # > True


def compare_str(str1, str2):
    return len(str1) == len(str2)


# print(compare_str("AB", "CD"))  # > True
# print(compare_str("ABC", "DE"))  # > False
# print(compare_str("hello", "App Academy"))  # > False


def is_valid_hex(color):
    if color[0] != "#" or len(color) != 7:
        return False

    color_chars = list("abcdef0123456789")
    for char in color[1:].lower():
        if char not in color_chars:
            return False
    return True


# print(is_valid_hex("#CD5C5C")) #> True
# print(is_valid_hex("#EAECEE")) #> True
# print(is_valid_hex("#eaecee")) #> True

# print(is_valid_hex("#CD5C58C"))
# # Prints False
# # Length exceeds 6

# print(is_valid_hex("#CD5C5Z"))
# # Prints False
# # Not all alphabetic characters in A-F

# print(is_valid_hex("#CD5C&C"))
# # Prints false
# # Contains unacceptable character

# print(is_valid_hex("CD5C5C"))
# # Prints False
# # Missing '#'
