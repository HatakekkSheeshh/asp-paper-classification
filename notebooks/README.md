# Notebooks

Notebook trong thư mục này được đặt theo thứ tự pipeline để cả nhóm dễ theo dõi.

## Danh sách

- `01_eda.ipynb`: EDA ban đầu và thống kê dữ liệu.
- `02_text_baseline.ipynb`: baseline text với TF-IDF + model tuyến tính.
- `03_metadata_features.ipynb`: xây và đánh giá metadata features.
- `04_hybrid_models.ipynb`: kết hợp text + metadata.
- `05_ensemble_error_analysis.ipynb`: ensemble, confusion matrix, error analysis.

## Quy tắc sử dụng

- Mỗi thành viên có thể dùng bất kỳ notebook nào làm điểm xuất phát cho branch của mình.
- Notebook nên gọi code trong `src/` thay vì viết logic dài trực tiếp trong cell.
- Giữ output cần thiết nhưng tránh commit output quá nặng.
- Khi notebook đã tương đối ổn, chuyển logic tái sử dụng sang `src/`.
