salary = 15_000_000
sale = float(input("Nhập doanh thu thực tế "))

if sale > 100_000_000:
    salary = salary * 1.10
    print("Lương thực nhận:", salary)

elif 80_000_000 <= sale <= 100_000_000:
    print("Lương thực nhận:", salary)

elif 10_000_000 <= sale < 80_000_000:
    salary = salary * 0.90
    print("Lương thực nhận:", salary)

else:
    print("Cần xử lý theo quy định doanh nghiệp")