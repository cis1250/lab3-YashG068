#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

# Fibonacci Sequence Exercise
# Asking the user how many terms they want
def get_postive_int();

While True:  # keep asking until we get a good number
    s = input("Enter how many terms you want: ")
    if s.isdigit():      #Checks: only digits like "5", "12"
            n = int(s)
            if n > 0:  # must be positive (1, 2, 3, ...)
                return n
        print("Please enter a positive integer.") # show error and ask again

def generate_fibonacci(n):
    seq = []     # this will store the numbers
    a = 0           # first Fibonacci number
    b = 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

def print_sequence(seq):
    # print the sequence in a simple, readable way
    print("Fibonacci sequence:", end=" ")
    for x in seq:
        print(x, end=" ")
    print()  # new line

# check if input is a number 



  
