# Write you code below
hours_worked = int(input("How many hours did you work? "))
hourly_wage = int(input("How much are you paying per hour? "))

if hours_worked <= 40:
    regular_pay = hours_worked * hourly_wage
else: regular_pay = 40 * hourly_wage


if hours_worked > 40:
    overtime_pay =  int((hours_worked - 40) * 1.5 * hourly_wage)
else: overtime_pay = 0


total_pay = regular_pay + overtime_pay
print("Regular pay: ", regular_pay)
print("Overtime pay: ", overtime_pay)
print("Total pay: ", total_pay)
