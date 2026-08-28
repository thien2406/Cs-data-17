so_nguyen = input("Nhập danh sách số nguyên là")

chuoi= [int(x) for x in so_nguyen.split(",")]

so_can_tim = int(input("Số cần tìm là"))

vitri = []

for i in range(len(chuoi)):
    if chuoi[i] == so_can_tim:
        vitri.append(i)
if len(vitri)>0:
    print("Số", so_can_tim,"Vị trí hiện tại vị trí là",vitri)
else:
    print("Không tin thấy số",so_can_tim)


