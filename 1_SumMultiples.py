# projecteuler.net - Problem: 1
# If we list all the natural numbers below
# 10 that are multiples of 3 or 5, we get 3,
# 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

# Create multiples list
multiples = []

# User chooses big number
big_number = input("Enter big number:")
# User chooses multiples
multiple_set = [int(x) for x in input("Enter multiples:").split()]

# loops through each multiple
for multiple in multiple_set:
    m = int(multiple)
    # Loops through the big number
    for i in range(int(big_number)):
        # If number is divisible by multiple
        # without a remainder, it appends to
        # multiple list
        if i % m == 0:
            # Checks if multiple is in list
            if i not in multiples:
                multiples.append(i)
        else:
            continue

# sums multiple list
print(multiples)
print(sum(multiples))
