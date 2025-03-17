from statistics import mean

class School_Health: # Calculates averages and can show them
    def __init__(self, amount, age, weight, height):
        self.amount = amount
        self.age = [float(a) for a in age]
        self.weight = [float(w) for w in weight]
        self.height = [float(h) for h in height]

    def average(self):
        age_avg = mean(self.age)
        weight_avg = mean(self.weight)
        height_avg = mean(self.height)
        return [age_avg, weight_avg, height_avg]

    def show_average(self):
        average_dict = {
            "Age": mean(self.age),
            "Weight": mean(self.weight),
            "Height": mean(self.height)
        }
        for key, value in average_dict.items():
            print(f"{key}: {value:.2f}")

class Comparison: # To compare both rooms
    def __init__(self, A_Room, B_Room):
        self.A_Room = A_Room
        self.B_Room = B_Room

    def compare(self):
        if self.A_Room[-1] > self.B_Room[-1]:
            print("(A) Has a much more positive result.")
        elif self.A_Room[-1] < self.B_Room[-1]:
            print("(B) Has a much more positive result.")
        elif self.A_Room[-2] < self.B_Room[-2]:
            print("(A) Has a much more positive result.")
        elif self.A_Room[-2] > self.B_Room[-2]:
            print("(B) Has a much more positive result.")
        else:
            print("Both had the same progress.")

# Input for Class (A)
print("Class (A):")
a_amount = int(input("Their amount: "))
a_ages = input("Enter their ages (comma-separated): ").split(",")
a_weights = input("Enter their weights (comma-separated): ").split(",")
a_heights = input("Enter their heights (comma-separated): ").split(",")

# Input for Class (B)
print("\nClass (B):")
b_amount = int(input("Their amount: "))
b_ages = input("Enter their ages (comma-separated): ").split(",")
b_weights = input("Enter their weights (comma-separated): ").split(",")
b_heights = input("Enter their heights (comma-separated): ").split(",")

# Create Objects
ARoom = School_Health(a_amount, a_ages, a_weights, a_heights)
BRoom = School_Health(b_amount, b_ages, b_weights, b_heights)

# Show Averages
print("\n(A) Averages:")
ARoom.show_average()
print("\n(B) Averages:")
BRoom.show_average()

# Comparison
print("\n\nResult of comparison:")
Compare = Comparison(ARoom.average(), BRoom.average())
Compare.compare()