# 41. lesson - More ways to add items on the list
A = [5, 12, 72, 55, 89]
# A = A + 1
# Output: error

A = A + [1]
# I. add to A this list of one item - 1
print(A)

# A = A + "BCD"
# Output: error

A = A + ["BCD"]
print(A)
# I. Output: [5, 12, 72, 55, 89, 1, 'BCD']

# or II. add list
A = A + list("BCD")
print(A)
# II. Output: [5, 12, 72, 55, 89, 1, 'BCD', 'B', 'C', 'D']