a = float(input("Nhập số a: "))

if a <0 or a>10:
    print("Điểm không hợp lệ")
elif a>= 9:
    print("Xuất sắc")
elif a>= 8:
    print("Giỏi")
elif a>= 6.5:
    print("Khá")
elif a>= 5:
    print("Trung bình")
elif a<=4:
    print("Yếu")