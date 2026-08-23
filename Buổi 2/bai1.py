age = int(input("Nhập tuổi của bạn: "))

if age <0:
    print("Tuổi không hợp lệ. Vui lòng nhập lại tuổi.")
elif 0 <= age < 18:
    print("Bạn chưa đủ tuổi.")
else:
    print("Bạn đã đủ tuổi.")