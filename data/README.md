# Data

Thư mục này dùng để chuẩn hóa luồng dữ liệu của project.

## Cấu trúc

- `raw/`: dữ liệu đầu vào sau khi nhóm thống nhất cách đặt tên file.
- `interim/`: dữ liệu sau bước cleaning hoặc feature extraction trung gian.
- `processed/`: dữ liệu sẵn sàng cho model hoặc các artifact đã chuẩn hóa.
- `submissions/`: file nộp Kaggle.

## Lưu ý

- Hiện tại dữ liệu gốc vẫn nằm ở `dataset_stage1/` và đã được map trong config chung.
- Chỉ đưa vào `processed/` những file có thể tái tạo từ code; tránh lưu artifact nặng không cần thiết.
- Nếu cần tạo version chuẩn của train/test, hãy cập nhật README ở `raw/` và config.
