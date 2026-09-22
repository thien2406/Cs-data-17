employees = { 
    "name": ["An", "Bình", "Chi", "Dũng"], 
    "department": ["IT", "IT", "HR", "Finance"], 
    "salary": [2000, 3000, 1500, 2500] 
}

for i in range(len(employees["name"])):
    print(
        employees["name"][i],"-",
        employees["department"][i],"-",
        employees["salary"][i],
    )