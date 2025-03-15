def vote_counter(amount):
    # Dictionary to store candidate names and their vote counts
    votes = {}

    print("Enter the votes:")
    for _ in range(amount):  # Loop exactly 'amount' times
        name = input().strip()  # Get user input and remove any extra spaces
        votes[name] = votes.get(name, 0) + 1  # Increase vote count for the candidate

    print("\nVote Results:")
    # Sort candidates by highest votes first, then alphabetically if votes are the same
    for candidate, count in sorted(votes.items(), key=lambda x: (-x[1], x[0])):
        print(f"{candidate} : {count}")  # Print the candidate name and vote count

# Keep asking the user for a valid number of votes
while True:
    try:
        n = int(input("Please enter number of votes: "))  # Ask user for the number of votes
        if n <= 0:  # Ensure input is a positive number
            print("Number of votes must be positive. Try again.")
            continue  # Ask again if input is invalid
        break  # Exit the loop if input is valid
    except ValueError:  # Catch cases where the input is not a number
        print("Invalid input. Please enter a valid integer.")

# Call the function with the user-provided number of votes
vote_counter(n)