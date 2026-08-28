so_nguyen = input("Nhập số nguyên vào")

chuoi = [int(x) for x in so_nguyen.split(",")]

so_chan = []
so_le = []

for a in chuoi:
    if a % 2 == 0:
        so_chan.append(a)
    else:
        so_le.append(a)
print("Số chẵn là",so_chan)
print("Số lẻ là",so_le)