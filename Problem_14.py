# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.


def collatz_chain_length(start_point):

    x = start_point
    chain_length = 1
    limit = 0

    while x != 1 and limit < 10000000:

        if x % 2:
            x = 3 * x + 1
            chain_length, limit += 1
        else:
            x = x / 2
            chain_length, limit += 1

    return(chain_length)

def max_length(max_value):

    current_max_length = 1
    max_iteration = 1

    for i in range(max_value + 1):

        test_iteration_length = collatz_chain_length(i)

        if test_iteration_length >= current_max_length:

            max_iteration = i
            current_max_length = test_iteration_length

        else:
            pass

    return(max_iteration, current_max_length)

def interface():
     max_val = int(input("Maximum Collatz chain value = "))
     print(max_length(max_val))

def main():
    interface()

main()
