so_nguyen = input("Nhập số nguyên vào")

chuoi = [int(x) for x in so_nguyen.split(",")]

value_nguong = 5

gia_tri_lon_hon = []
gia_tri_nho_hon = []

for a in chuoi:
    if a >=value_nguong:
        gia_tri_lon_hon.append(a)
    else:
        gia_tri_nho_hon.append(a)
print("Giá trị lớn hơn ngưỡng là",gia_tri_lon_hon)
#print("Giá trị nhỏ hơn ngưỡng là",gia_tri_nho_hon)








