username = "admin"
password = "123456"

user_input_username = input("Nhập tên đăng nhập: ")
user_input_password = input("Nhập mật khẩu: ")

if user_input_username == username and user_input_password == password:
    print("Đăng nhập thành công!")
elif user_input_username != username:
    print("Tên đăng nhập không đúng.")
elif user_input_password != password:
    print("Mật khẩu không đúng.")
else:
    print("Đăng nhập thất bại")
