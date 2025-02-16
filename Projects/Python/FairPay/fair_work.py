def salary(hour_of_work, per_hour):
    """
    Calculates the salary based on hours worked and pay rate.

    Conditions:
    - If `per_hour` is 0 or negative, returns an error message.
    - If `hour_of_work` is 0 or negative, returns an error message.
    - If `hour_of_work` exceeds 8, warns the user and suggests reducing hours.
    - Otherwise, calculates and returns the salary.

    Parameters:
    - hour_of_work (float): Number of hours worked in a day.
    - per_hour (float): Hourly wage.

    Returns:
    - str: Salary amount or an appropriate warning message.
    """

    # Validate if per-hour salary is valid
    if per_hour <= 0:
        return "Invalid salary per hour."

    # Validate if work hours are valid
    if hour_of_work <= 0:
        return "Invalid work hours."

    # Limit work hours to a maximum of 8
    if hour_of_work > 8:
        banned_hours = hour_of_work - 8
        return f"Too much work. You can't work for {banned_hours} extra hours on the next days."

    # Calculate and return the salary
    return f"Your salary is {hour_of_work * per_hour}."


# Get user input for work hours and hourly wage
hours = float(input("How many hours did you work today? "))
salary_per_hour = float(input("How much do you get paid per hour? "))

# Display the calculated salary or any warnings
print(salary(hours, salary_per_hour))