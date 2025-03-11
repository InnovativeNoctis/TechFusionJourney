def steiner(c):
    c = list(map(int, c.split()))  # Convert input to a list of integers
    c.sort()  # Sort the list
    return abs(c[1] - c[0]) + abs(c[2] - c[1])  # Sum of distances

# Get user input
i = input("Enter all three Xs with space: ").strip()
print(steiner(i))
