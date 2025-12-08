# Number of rows
number = 5

# Generate the pattern
for row in range(number, 0, -1):
    for column in range(row, 0, -1):
        print(column, end=' ')
    print()  # Move to next line

