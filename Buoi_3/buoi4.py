so_nguyen = input("Nhập số nguyên dương")

chuoi = [int(x) for x in so_nguyen.split(",")]

for i in range(len(chuoi) -1):
    vi_tri_min = i
    for j in range(i+1,len(chuoi)):
        if chuoi[i] < chuoi[vi_tri_min]:
            vi_tri_min = j

    chuoi[i], chuoi[vi_tri_min] = chuoi[vi_tri_min], chuoi[i]

print("Danh sách sắp xếp là",chuoi)