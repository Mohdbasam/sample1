# Number of rows for the upper part
rows = 5

# Printing the upper part of the pattern
for i in range(1, rows + 1):
    print('*' * i)

# Printing the lower part of the pattern
for i in range(rows-1, 0, -1):
    print('*' * i)
