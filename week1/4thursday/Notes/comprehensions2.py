names = ['bOB', 'Jo', 'MoRGAn', 'kita', 'HAZY']

# fixedNames = []
# # for loop
# for name in names:
#     # value to add
#     fixedNames.append(name.title())

#            [expression for value in iterable]
titleNames = [name.title() for name in names]


nums = [1, 11, 12, 13, 17, 19, 21, 27, 33, 40, 22]

# div3 = []
# # for loop
# for n in nums:
#     # condition
#     if n % 3 == 0:
#         # value to add
#         div3.append(n)

#          [value for-loop if conditional]
divThree = [n for n in nums if n % 3 == 0]


letters = ['a', 'b', 'c']
nums = [1, 2, 3]

combinations = []
# outter for loop
for n in nums:
    # inner for lop
    for l in letters:
        # value to add
        combinations.append((n, l))


# [value outter-for-loop inner-for-loop]

# tupleList = [(n, l) for n in nums for l in letters]
tupleList = [((n, l) for n in nums) for l in letters]
tupleList = [(n, l) 
            for n in nums 
            for l in letters]



# Dictionary Comprehension

keys = ['age', 'name', 'height']
values = [32, 'corina', 1.4]

# d = {}
# # for loop
# for i in range(len(keys)):
#     #          key     = value
#     d[keys[i].title()] = values[i]


#  {key: value for-loop}
d = {keys[i].title(): values[i] for i in range(len(keys))}

# ***************************************************
# More pythony way of solving
# Zip
# ***************************************************

# Python destructuring - destructures into implied tuple
d2 = {k: v for (k, v) in zip(keys, values)}



