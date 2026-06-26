#find howw long you have left to reach 90 yars
age = int(input("enter your age"))
years_left=90-age
months_left = years_left *12
days_left = years_left*365
print(f"You have {years_left} years, {months_left} months or {days_left} days left.")