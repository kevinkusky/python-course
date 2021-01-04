print('THREE CASES FOR RANGE')
print('A) End Value')

# STEP 1: Change the zero in the range to 10
#         Notice how "10" is not included in the output
for i in range(10):
    print(i)

print('B) Start & End Values')

# STEP 2: Code a `for` loop to print numbers 5 through 9

for i in range(5, 10):
  print(i)

print('C) Only Even Values')

# STEP 3: Print 0, 2, 4, 6 and 8 using a for loop
#         Hint - range can take a 3rd parameter for the step distance


for i in range(0, 10, 2):
  print(i)

  # Powers of 2 from 1 to 16
# Write a for loop that uses the range function to
# print the powers of 2 from 2 - 65536, that is
# from 2^1st - 2^16th powers

for i in range(1, 17):
    print(2**i)