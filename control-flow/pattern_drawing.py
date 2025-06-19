# pattern_drawing.py

# Prompt user for a positive integer
size = int(input("Enter the size of the pattern: "))

# Validate input is positive
if size <= 0:
    print("Please enter a positive integer.")
else:
    row = 0
    # Outer loop using while
    while row < size:
        # Inner loop using for
        for col in range(size):
            print("*", end="")
        print()  # Move to next line after one row
        row += 1
