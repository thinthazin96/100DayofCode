print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill?\n"))
num_of_people = int(input("How many people to split the bill?\n"))
tip_percentage = int(input("What percentage tip would you like to give? 15, 18 or 20?\n"))

if tip_percentage == 15:
  each_person_cost = (total_bill/num_of_people) * 1.15
  print("Each person should pay: " + str(each_person_cost))
elif tip_percentage == 18:
  each_person_cost = (total_bill/num_of_people) * 1.18
  print("Each person should pay: " + str(each_person_cost))
elif tip_percentage == 20:
  each_person_cost = (total_bill/num_of_people) * 1.20
  print("Each person should pay: " + str(each_person_cost))
else:
  print("You can only tip; 15%, 18% or 20%")