so_nguyen = input("Nhập một số nguyên: ")

chuoi = [int(x) for x in so_nguyen.split(",")]
# 1,3,4,5,6
lon_nhat = chuoi[0]
lon_thu_hai = None
for a in chuoi:
    if a > lon_nhat:
        lon_thu_hai = lon_nhat
        lon_nhat = a
    elif a < lon_nhat and (lon_thu_hai is None or a > lon_thu_hai):
        lon_thu_hai = a
if lon_thu_hai is not None:
    print("Số lớn thứ 2 là", lon_thu_hai)