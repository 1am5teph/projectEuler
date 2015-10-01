# projecteuler.net - Problem: 1
# If we list all the natural numbers below
# 10 that are multiples of 3 or 5, we get 3,
# 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

# Create multiples list
multiples = []
multiple_set = []

# User chooses big number
big_number = input("Enter big number:")
multiple_set = iter[(input("Enter multiples:")]

for multiple in multiple_set:
    print(multiple)
    # while new_multiple < big_number:
    #     new_multiple = new_multiple + new_multiple
    #     multiples.append(new_multiple)

# User chooses multiples
# find_multiple = [input("Enter multiples:")

# User chooses maximum number
# for i in range((input("Pick a number, any number:")+1)):
#     # creates list of multiples
#     if i % 3 == 0:
#         continue
#     elif i % 5 ==0:
#         multiples.append(i)
#     else:
#         continue

# sum multiples list
multiple_total = sum(multiples)
print(multiple_total)
