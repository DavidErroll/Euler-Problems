# Problem 3

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

# Quick comment:
# Since prime factorization is the basis of current encryption methods, I am confident that:
#   1. a brute-force loop of some type is necessary; and
#   2. people who know how to optimize code for speed will have written superior loops.


test_value = 600851475143
test_check = 0

while not test_check:

  test_divisor = 2
  test_factor = test_value / test_divisor
  
  if test_factor % 1 == 0:

    if str(test_factor) in ['2', '3', '5', '7', '11', '13']:
      test_check = 1
      return test_factor
    
    elif str(test_factor)[-1] in ['0', '2', '4', '5', '6', '8'] or sum(int(digit) for digit in str(test_factor)) % 3 == 0 or 4 rule % 4 == 0 or 7 rule % 7 == 0 or 11 rule % 11 == 0:
      test_divisor += 1

    else:
      brute_divisor = test_factor // 7
      while test_factor % brute_divisor != 0 or brute_divisor == 1:
        brute_divisor = brute_divisor - 1
        test_check = 1
        return brute_divisor

  else:
    test_divisor += 1
    
return test_factor 
