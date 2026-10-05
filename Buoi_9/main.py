from cover_letter_processor import CoverLetterProcessor


# Tạo đối tượng xử lý hồ sơ
processor = CoverLetterProcessor(
    folder_path="cover_letters",
    excel_file="so_yeu_ly_lich.xlsx"
)


# Bắt đầu xử lý
processor.process_documents()