employees = [
    {"name": "Zakir Aliev", "hours": 45, "hourly_rate": 20.0},
    {"name": "Leyla Mammadova", "hours": 38, "hourly_rate": 25.0},
    {"name": "Orkhan Aliyev", "hours": 50, "hourly_rate": 18.5},
    {"name": "Aynur Huseynova", "hours": 40, "hourly_rate": 22.0},
    {"name": "Elmir Gasimov", "hours": 42, "hourly_rate": 30.0},
    {"name": "Nigar Karimova", "hours": 35, "hourly_rate": 28.0},
]

salary_dict = {}

for emp in employees:
    name = emp["name"]
    hours = emp["hours"]
    rate = emp["hourly_rate"]

    if hours > 40:
        overtime_hours = hours - 40
        salary = (40 * rate) + (overtime_hours * rate * 1.5)
        print(f"Overtime alert: {name} worked {hours} hours (overtime).")
    else:
        salary = hours * rate

    salary_dict[name] = salary

print("\nTask 1 Output (Name -> Salary):")
print(salary_dict)