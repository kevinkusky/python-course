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

# # STEP 1 - Write a function named `welcome` that prints a welcome message


# def welcome():
#     print("welcome, ya'll")


# # Step 2 - Write a function named `calc_sum` that
# #   - takes in two numbers and
# #   - returns their sum


# def calc_sum(n1, n2):
#     return n1 + n2


# # DO NOT EDIT - The guts of the program
# welcome()
# print(calc_sum(1, 2), "is 3?", calc_sum(1, 2) == 3)
# print(calc_sum(-10, -2), "is -12?", calc_sum(-10, -2) == -12)
# print(calc_sum(1.1, -2.2), "is -1.1?", calc_sum(1.1, -2.2) == -1.1)
# print(calc_sum("a", "b"), "is ab?", calc_sum("a", "b") == "ab")
# print(
#     calc_sum([1, 2], [3, 4]), "is [1,2,3,4]?", calc_sum([1, 2], [3, 4]) == [1, 2, 3, 4]
# )
