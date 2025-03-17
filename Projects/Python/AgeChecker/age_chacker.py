import datetime

class AgeChecker:
    def __init__(self, date):
        try:
            self.birth_date = datetime.datetime(int(date[0]), int(date[1]), int(date[2]))
        except ValueError:
            print("Error: Invalid date format or non-existent date.")
            self.birth_date = None 

    def age(self):
        if self.birth_date:
            current_time = datetime.datetime.now()
            age = current_time.year - self.birth_date.year
            
            if (current_time.month, current_time.day) < (self.birth_date.month, self.birth_date.day):
                age -= 1

            print(f"Your age: {age}")

date = input("Enter your date of birth (yyyy/mm/dd): ").split("/")
if len(date) == 3:
    age_checker = AgeChecker(date)
    age_checker.age()
else:
    print("Error: Please enter your date of birth in the correct format (yyyy/mm/dd).")
