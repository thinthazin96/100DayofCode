#Exercise 9
print("Exercise 9")
# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = weight / (height * height)

if BMI <= 18.5:
  print(f"Your BMI is {BMI}, you are underweight.")
elif 18.5 < BMI < 25:
  print(f"Your BMI is {BMI}, you have a normal weight.")
elif 25 <= BMI < 30:
  print(f"Your BMI is {BMI}, you are slightly overweight.")
elif 30 <= BMI < 35:
  print(f"Your BMI is {BMI}, you are obese.")
else:
  print(f"Your BMI is {BMI}, you are clinically obese.")


#Exercise 10
print("Exercise 10")
# Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if (year % 100 == 0):
  print("Not leap year")

elif (year % 4 == 0) or (year % 400 == 0):
  print("Leap year")

else:
  print("Not leap year")


