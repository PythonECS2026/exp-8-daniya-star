# AIM: Write a Python program to print a 
# triangle pattern (give any), emphasizing
# the transition from C to Python syntax.
# Coder:khan daniya rehman
# Date:03/03/2026

print("--- Pattern Printer ---\n")


# Write your code here 
try:
    n = int(input("Enter number of lines: "))

    for i in range(1, n + 1):
        print("*" * i)

except ValueError:
    print("Invalid input! Please enter integer only.")










