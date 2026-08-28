so_nguyen = input("Nhập số nguyên dương")

chuoi = [int(x) for x in so_nguyen.split(",")]

chuoi.sort()

print("Danh sách sắp xếp là",chuoi)