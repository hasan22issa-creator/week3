
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ── Example 1: Square every number ──

# Old way (loop):
squares_loop = []
for n in numbers:
    squares_loop.append(n ** 2)

# New way (list comprehension):
# Read as: "give me n squared, for every n in numbers"
squares = [n ** 2 for n in numbers]

print("Squares:", squares)


