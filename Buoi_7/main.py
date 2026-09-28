import os
import re
import openpyxl

from datetime import datetime


excel_file = "students.xlsx"


if os.path.exists(excel_file):
    workbook = openpyxl.load_workbook(excel_file)
    worksheet = workbook.active
else:
    workbook = openpyxl.Workbook()
    worksheet = workbook.active

    worksheet.title = "Thông tin sinh viên"

    headers = [
        "Mã Sinh Viên",
        "Họ và tên",
        "Lớp",
        "Email",
        "Số điện thoại",
        "Ngày sinh",
        "Tuổi"
    ]

    worksheet.append(headers)


def kiem_tra_email(email):

    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    return re.match(pattern, email) is not None


def kiem_tra_sdt(sdt):

    pattern = r"^0\d{9}$"

    return re.match(pattern, sdt) is not None


def tinh_tuoi(ngay_sinh):

    hom_nay = datetime.now()

    tuoi = hom_nay.year - ngay_sinh.year

    if (hom_nay.month, hom_nay.day) < (
        ngay_sinh.month,
        ngay_sinh.day
    ):

        tuoi -= 1

    return tuoi



while True:

    print("\n===== NHẬP THÔNG TIN SINH VIÊN =====")

    ma_sv = input("Nhập mã sinh viên: ").strip()

    ten = input("Nhập họ và tên: ").strip()

    lop = input("Nhập tên lớp: ").strip()

    while True:

        email = input("Nhập email: ").strip()

        if kiem_tra_email(email):

            break

        print("Email không đúng, vui lòng nhập lại!")


    while True:

        phone = input("Nhập số điện thoại: ").strip()

        if kiem_tra_sdt(phone):

            break

        print("Số điện thoại không hợp lệ, vui lòng nhập lại!")




    while True:

        ngay_sinh_str = input("Nhập ngày sinh (dd/mm/yyyy): ").strip()

        try:

            ngay_sinh = datetime.strptime(ngay_sinh_str,"%d/%m/%Y")

            # Không cho nhập ngày sinh trong tương lai
            if ngay_sinh > datetime.now():
                print("Ngày sinh không được lớn hơn ngày hiện tại!")
                continue
            break
        except ValueError:
            print("Ngày sinh không đúng định dạng!")

            print("Vui lòng nhập theo dạng: dd/mm/yyyy")

    tuoi = tinh_tuoi(ngay_sinh)

    worksheet.append([
        ma_sv,
        ten,
        lop,
        email,
        phone,
        ngay_sinh_str,
        tuoi
    ])

    workbook.save(excel_file)

    print("Đã lưu thông tin sinh viên!")
    print("Tuổi:", tuoi)


    while True:
        tiep_tuc = input("Bạn có muốn nhập tiếp không? (Y/N): ").strip().upper()
        if tiep_tuc == "Y":
            break
        elif tiep_tuc == "N":

            print("Kết thúc chương trình!")

            workbook.save(excel_file)

            exit()

        else:

            print("Vui lòng chỉ nhập Y hoặc N!")