from functools import reduce

employees = [
    {"name": "Zakir Aliev", "hours": 45, "hourly_rate": 20.0},
    {"name": "Leyla Mammadova", "hours": 38, "hourly_rate": 25.0},
    {"name": "Orkhan Aliyev", "hours": 50, "hourly_rate": 18.5},
    {"name": "Aynur Huseynova", "hours": 40, "hourly_rate": 22.0},
    {"name": "Elmir Gasimov", "hours": 42, "hourly_rate": 30.0},
    {"name": "Nigar Karimova", "hours": 35, "hourly_rate": 28.0},
]


def salary(employee):
    hours = employee["hours"]
    rate = employee["hourly_rate"]
    if hours > 40:
        return (40 * rate) + ((hours - 40) * rate * 1.5)
    return hours * rate


all_salaries = list(map(salary, employees))
print("All Salaries:", all_salaries)

overtime_employees = list(
    filter(lambda emp: emp["hours"] > 40, employees)
)
print("Overtime Employees:", [e["name"] for e in overtime_employees])

total_payroll = reduce(lambda acc, curr: acc + curr, all_salaries, 0.0)
print(f"Total Payroll: {total_payroll}")