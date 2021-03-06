# projecteuler.net - Problem: 2
# Each new term in the Fibonacci sequence is generated by adding
# the previous two terms. By starting with 1 and 2, the first 10
# terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values
# do not exceed four million, find the sum of the even-valued terms.

# User picks maximum
max_number = input("Enter maximum number:")

# Create list of fibonacci numbers starting with 1
fibonacci_numbers = [1,2]

# Fibonacci sequence
def fibonacci():
    # Finds last number in fibonacci list
    last_number = fibonacci_numbers[(len(fibonacci_numbers) - 1)]
    while last_number > max_number:
        # Adds last two numbers in fibonacci list
        new_number = last_number + fibonacci_numbers[(len(fibonacci_numbers)-2)]
        # Appends new number to list
        fibonacci_numbers.append(new_number)

fibonacci()
print(fibonacci_numbers)
