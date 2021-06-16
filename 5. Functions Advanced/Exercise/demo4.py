import re
# import math

data = input()
# name_date = {}
# name_calories = {}
pattern = r"(#|\|)(?P<food>[a-zA-z\s]+)(\1)(?P<expire_date>[0-9]{2}/[0-9]{2}/[0-9]{2})(\1)(?P<calories>[0-9]+)(\1)"
valid_meal = re.finditer(pattern, data)
total_calories = 0
for meal_data in valid_meal:
    calories = int(meal_data['calories'])
    total_calories += calories

days = total_calories // 2000
print(f"You have food to last you for: {days} days!")

match = re.finditer(pattern, data)
for el in match:
    name = el["food"]
    expire_date = el["expire_date"]
    calories = el["calories"]
    print(f"Item: {name}, Best before: {expire_date}, Nutrition: {calories}")
