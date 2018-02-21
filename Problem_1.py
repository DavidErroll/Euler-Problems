# Problem 1

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


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

# Read out the sum:
print("Brute force 3s & 5s: ", accumulator)


accumulator = 0

# I'm not sure there is a way to confirm all multiples without checking each digit.
# This loop checks digits 1 to 1000:

for natural_number in range(1, 1001):

# Define sum of digits:
    digit_sum = sum(int(digit) for digit in str(natural_number))

# Check if digit is evenly divisible by 3; if so, increment the running sum by the digit:
    if digit_sum % 3 == 0:
        accumulator = accumulator + natural_number

# Check if digit is evenly divisible by 5; if so, increment the running sum by the digit:
    elif natural_number % 5 == 0:
        accumulator = accumulator + natural_number

# Read out the sum:
print("Human 3s: ", accumulator)


accumulator = 0

# I'm not sure there is a way to confirm all multiples without checking each digit.
# This loop checks digits 1 to 1000:

for natural_number in range(1, 1001):

    chars = str(natural_number)

# Define sum of digit:
    digit_sum = sum(int(digit) for digit in chars)

# Check if digit is evenly divisible by 3; if so, increment the running sum by the digit:
    if digit_sum % 3 == 0:
        accumulator = accumulator + natural_number

# Check if digit is evenly divisible by 5; if so, increment the running sum by the digit:
    elif chars[-1] in ["0", "5"]:
        accumulator = accumulator + natural_number

# Read out the sum:
print("Human 3s & 5s: ", accumulator)
