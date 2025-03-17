import random

class Human:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

class Footballist:    
    
    def __init__(self):
        self.members = {}
        
    def add_member(self, human):
        self.members[human.name] = f"{human.age}, {human.weight}, {human.height}"
        print("Added!")
    
    def seperate_team(self):
        member_list = list(self.members.keys())
        self.team_a = random.sample(member_list, 12)
        self.team_b = {k: v for k, v in self.members.items() if k not in self.team_a}
        
        # Printing Team A
        print("Team A:")
        for a in self.team_a:
            print(f"{a} --> {self.members[a]}")
        
        # Printing Team B
        print("\n\nTeam B:")
        for bk, bv in self.team_b.items():
            print(f"{bk} --> {bv}")


# Creating players
players = [
    Human("Sam", 18, 180, 78),    
    Human("Amir", 18, 185, 80),
    Human("John", 20, 175, 70),
    Human("Michael", 22, 182, 85),
    Human("Sophia", 19, 168, 60),
    Human("Daniel", 21, 178, 75),
    Human("Emma", 18, 165, 55),
    Human("Oliver", 23, 185, 88),
    Human("Ava", 20, 160, 50),
    Human("William", 24, 190, 90),
    Human("Isabella", 22, 170, 58),
    Human("James", 19, 180, 72),
    Human("Benjamin", 21, 176, 73),
    Human("Charlotte", 20, 162, 54),
    Human("Lucas", 23, 183, 82),
    Human("Mia", 19, 158, 49),
    Human("Elijah", 22, 180, 78),
    Human("Amelia", 18, 166, 57),
    Human("Mason", 24, 188, 86),
    Human("Harper", 21, 164, 53),
    Human("Ethan", 20, 177, 74),
    Human("Evelyn", 23, 169, 59),
    Human("Alexander", 22, 181, 79),
    Human("Abigail", 19, 161, 51)
]

# Creating the Footballist team
team = Footballist()

# Adding all players to the team
for player in players:
    team.add_member(player)

# Separating the team into Team A and Team B
team.seperate_team()