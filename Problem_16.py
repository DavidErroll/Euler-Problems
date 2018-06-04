# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2^1000?

def digit_sum(number):
    sum_digits = sum(int(x) for x in str(number))
    return sum_digits

def interface():
    base = int(input("Enter the base: "))
    exponent = int(input("Enter the exponent: "))
    print("Sum = ", digit_sum(base ** exponent))

def main():
    interface()

main()

# Result for base = 2, exponent = 1000: 1366
