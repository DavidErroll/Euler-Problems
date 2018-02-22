# Problem 1

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

import time

# Start timing
machine_start = time.clock()

# Set a variable to calculate the sum as each digit is checked:
accumulator = 0

# I'm not sure there is a way to confirm all multiples without checking each digit.
# This loop checks digits 1 to 1000:

for natural_number in range(1, 1001):

# Check if digit is evenly divisible by 3; if so, increment the running sum by the digit:
    if natural_number % 3 == 0:
        accumulator = accumulator + natural_number

# Check if digit is evenly divisible by 5; if so, increment the running sum by the digit:
    elif natural_number % 5 == 0:
        accumulator = accumulator + natural_number

machine_time = time.clock() - machine_start

# Read out the sum:
print('Brute force 3s & 5s: ', accumulator, ' | Time: ', machine_time)


#This version uses the mnemonic for multiples of 3 (sum of digits is a multiple of 3):

human3s_start = time.clock()
accumulator = 0
for natural_number in range(1, 1001):

# Define sum of digits:
    digit_sum = sum(int(digit) for digit in str(natural_number))

    if digit_sum % 3 == 0:
        accumulator = accumulator + natural_number
    elif natural_number % 5 == 0:
        accumulator = accumulator + natural_number
human3s_time = time.clock() - human3s_start
print('Human 3s: ', accumulator, ' | Time: ', human3s_time)


#This version uses the mnemonic for multiples of 5 (final digit is 0 or 5):

human5s_start = time.clock()
accumulator = 0
for natural_number in range(1, 1001):
    if natural_number % 3 == 0:
        accumulator = accumulator + natural_number

# Check string version of final digit against list of 0, 5:
    elif str(natural_number)[-1] in ['0', '5']:

        accumulator = accumulator + natural_number
human5s_time = time.clock() - human5s_start
print('Human 5s: ', accumulator, ' | Time: ', human5s_time)


# This version uses both mnemoincs:

human3and5s_start = time.clock()
accumulator = 0
for natural_number in range(1, 1001):

# Define number as string of characters
    chars = str(natural_number)

    digit_sum = sum(int(digit) for digit in chars)
    if digit_sum % 3 == 0:
        accumulator = accumulator + natural_number
    elif chars[-1] in ["0", "5"]:
        accumulator = accumulator + natural_number
human3and5s_time = time.clock() - human3and5s_start
print("Human 3s & 5s: ", accumulator, ' | Time: ', human3and5s_time)
