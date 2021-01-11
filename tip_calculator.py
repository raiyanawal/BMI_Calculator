print("Welcome to the tip calculator!")
total_bill = int(input("What is the total bill?"))
tip =  int(input("What percentage tip would you like to give?"))
tip_percentage = tip/100
total_tip = total_bill * tip_percentage
total_bill_tip = total_bill + total_tip
num_of_people = int(input("How many people"))
per_person_bill = total_bill_tip / num_of_people
final_amount = round(per_person_bill, 2)
print (f"Per person bill is {final_amount}")

