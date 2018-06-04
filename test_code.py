x = 999999
chain_length = 1

while x != 1:

    if x % 2:
        x = 3 * x + 1
        chain_length += 1
    else:
        x = x / 2
        chain_length += 1

print(chain_length)
