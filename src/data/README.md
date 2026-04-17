# src.data

Module này phụ trách đọc dữ liệu và tạo split validation dùng chung.

## File hiện có

- `loading.py`: đọc train/test từ config.
- `splits.py`: tạo `StratifiedKFold` và fold assignment.

## Cách dùng trong mô hình 4 branch

- Đây là phần dùng chung cho tất cả branch.
- Mỗi thành viên có thể giữ nguyên module này hoặc mở rộng trên branch của mình nếu cần.
