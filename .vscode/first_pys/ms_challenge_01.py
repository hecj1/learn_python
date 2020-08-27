# This program is to complete the first challenge for Create your first Python program
# the output will be similar to the following sample output:
# Today's date?
# Thursday
# Breakfast calories?
# 100
# Lunch calories?
# 200
# Dinner calories?
# 300
# Snack calories?
# 400
# Calorie content for Thursday: 1000
#Start

# this will ask the user what is today's date
print("What is today's date? ")
date_today = input()
# this will ask the user for the number of calories consumed for breakfast
print("Number of calories for breakfast? ")
breakfast_cal = int(input())
# this will ask the user for the number of calories consumed for breakfast
print("Number of calories for lunch? ")
lunch_cal = int(input())
# this will ask the user for the number of calories consumed for breakfast
print("Number of calories for dinner? ")
dinner_cal = int(input())
# sum the total calories
total_day = breakfast_cal + lunch_cal + dinner_cal
print("Calorie to total for " + date_today + ": " + str(total_day))
