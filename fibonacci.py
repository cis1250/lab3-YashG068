#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

# Fibonacci Sequence Exercise
# Asking the user how many terms they want
num = input("Enter how many terms you want: ")

# check if input is a number 
if num.isdigit(): # check if the input only has digits (0-9)
    num = int(num)# making it a whole number using int

    # check if number is positive
    if num > 0:
              # first two numbers of fibonacci
        a, b = 0, 1
      # using the for loop to print fibonacci numbers
        for i in range(num):
          # print the currect number 
            print(a, end=" ")
          # updating the vaule for the next numbers
            a, b = b, a + b
        print()  # goes to a new line at the end
    else: # if the number is not postive 
        print("Please enter a positive integer.")
else: # if the input is not a number
    print("Please enter a positive integer.")

  
