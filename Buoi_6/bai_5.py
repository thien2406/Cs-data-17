employees = {
    "name": ["An", "Bình", "Chi", "Dũng"],
    "department": ["IT", "IT", "HR", "Finance"],
    "salary": [2000, 3000, 1500, 2500]
}

salary_by_department ={}

for i in range(4):
    department = employees["department"][i]
    salary = employees["salary"][i]

    if department in salary_by_department:
        salary_by_department[department] += salary
    else:
        salary_by_department[department] = salary
print(salary_by_department)
