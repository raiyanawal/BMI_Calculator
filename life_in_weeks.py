age = int(input("Enter your age: "))
remaining_years = 90 - age
# print(remaining_years)
months_remaining = remaining_years * 12
weeks_remaining = remaining_years * 52
days_remaining = remaining_years * 365
print(f"You have {days_remaining} days , {weeks_remaining} weeks and {months_remaining} months left.") 