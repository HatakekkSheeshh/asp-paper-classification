# src.data

Module này phụ trách đọc dữ liệu và tạo split validation dùng chung.

## File hiện có

- `loading.py`: đọc train/test từ config.
- `splits.py`: tạo `StratifiedKFold` và fold assignment.

## Ownership gợi ý

- Member 1 phụ trách review vì đây là nền tảng để mọi người dùng chung.
