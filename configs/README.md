# Configs

Thư mục này chứa cấu hình dùng chung cho cả nhóm.

## File hiện có

- `experiment_config.yaml`: path dữ liệu, target column, CV strategy, baseline defaults.

## Quy tắc sử dụng

- Member 1 là người chịu trách nhiệm cập nhật file này khi cả nhóm thống nhất thay đổi chung.
- Không sửa path dữ liệu tùy ý trong notebook; ưu tiên đọc từ config để tránh lệch môi trường giữa các thành viên.
- Khi đổi số folds, random seed hoặc cột input, phải ghi lại trong tracker và thông báo cả nhóm.
