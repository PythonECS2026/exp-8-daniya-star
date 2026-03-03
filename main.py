# AIM: Write a Python program to print a 
# triangle pattern (give any), emphasizing
# the transition from C to Python syntax.
# Coder:khan daniya rehman
# Date:03/03/2026

print("--- Pattern Printer ---\n")


# Write your code here
print("--- Pattern Printer ---")

rows = int(input("Enter Rows: "))

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end="")
    print()


