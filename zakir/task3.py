employees = [
    {"name": "Zakir Aliev", "hours": 45, "hourly_rate": 20.0},
    {"name": "Leyla Mammadova", "hours": 38, "hourly_rate": 25.0},
    {"name": "Orkhan Aliyev", "hours": 50, "hourly_rate": 18.5},
    {"name": "Aynur Huseynova", "hours": 40, "hourly_rate": 22.0},
    {"name": "Elmir Gasimov", "hours": 42, "hourly_rate": 30.0},
    {"name": "Nigar Karimova", "hours": 35, "hourly_rate": 28.0},
]

def select(items, predicate):
    result = []
    for item in items:
        if predicate(item):
            result.append(item)
    return result


def is_high_paid(employee):
    hours = employee["hours"]
    rate = employee["hourly_rate"]
    total = (
        (40 * rate) + ((hours - 40) * rate * 1.5)
        if hours > 40
        else hours * rate
    )
    return total > 1000

overtime_workers = select(employees, lambda emp: emp["hours"] > 40)
print("Employees with > 40 hours (via Lambda):", [e["name"] for e in overtime_workers])

high_paid_workers = select(employees, is_high_paid)
print("High Paid Employees (via is_high_paid):", [e["name"] for e in high_paid_workers])