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


def how_many_legs(ch, cow, pig):
    return (ch * 2) + 4 * (cow + pig)


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
