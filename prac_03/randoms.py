import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1?
# The output will be a random integer between 5 and 20(inclusive)

# What was the smallest number you could have seen, what was the largest?
# The smallest number is 5, and the largest is 20


# What did you see on line 2?
# The output will be a random odd number between 3 and 9(inclusive).

# What was the smallest number you could have seen, what was the largest?
# The smallest number is 3, and the largest is 9.

# Could line 2 have produced a 4?
# No, because the step is 2. Only produce odd number.


# What did you see on line 3?
# The output will be a random floating-point number between 2.5 and 5.5(inclusive)

# What was the smallest number you could have seen, what was the largest?
# The smallest number is 2.5, and the largest number is 5.5

# Write code, not a comment, to produce a random number between 1 and 100 inclusive
print(random.randint(1, 100))