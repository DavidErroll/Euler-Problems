# Problem 1

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

import time
import fractions

# Start timing
machine_start = time.clock()

# Set a variable to calculate the sum as each digit is checked:
accumulator = 0

# Loop checks digits 1 to 999:
for natural_number in range(1, 1000):

# Check if digit is evenly divisible by 3; if so, increment the running sum by the digit:
    if natural_number % 3 == 0:
        accumulator = accumulator + natural_number

# Check if digit is evenly divisible by 5; if so, increment the running sum by the digit:
    elif natural_number % 5 == 0:
        accumulator = accumulator + natural_number

machine_time = time.clock() - machine_start

# Read out the sum and elapsed time:
print('Brute force 3s & 5s: ', accumulator, ' | Time: ', machine_time)


#This version uses the mnemonic for multiples of 3 (sum of digits is a multiple of 3):

human3s_start = time.clock()
accumulator = 0
for natural_number in range(1, 1000):

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
for natural_number in range(1, 1000):
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
for natural_number in range(1, 1000):

# Define number as string
    chars = str(natural_number)

    digit_sum = sum(int(digit) for digit in chars)
    if digit_sum % 3 == 0:
        accumulator = accumulator + natural_number
    elif chars[-1] in ["0", "5"]:
        accumulator = accumulator + natural_number
human3and5s_time = time.clock() - human3and5s_start
print('Human 3s & 5s: ', accumulator, ' | Time: ', human3and5s_time)


# This version implements the kn(n+1)/2 method:
import fractions

summation_start = time.clock()

max_value = 999
test_value_1 = 3
test_value_2 = 5

# Find least common multiple of test values
test_value_gcd = fractions.gcd(test_value_1, test_value_2)
test_value_lcm = int( (test_value_1 * test_value_2) / test_value_gcd )

# sum = kn(n+1)/2
def summation(k, n):
    z = k * (n // k) * ( (n // k) + 1) // 2
    return z

# Calculate sum for each test value and double-counted values
test_value_1_sum = summation(test_value_1, max_value)
test_value_2_sum = summation(test_value_2, max_value)
overlap = summation(test_value_lcm, max_value)

total = test_value_1_sum + test_value_2_sum - overlap

summation_time = time.clock() - summation_start
print('Summation method: ', total, ' | Time: ', summation_time)
