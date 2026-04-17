# Experiments

Thư mục này dùng để ghi lại toàn bộ thí nghiệm và submission của nhóm.

## File hiện có

- `experiment_tracker.csv`: log mọi run đã train hoặc evaluate.
- `submission_log.csv`: log mọi file đã submit lên Kaggle.

## Quy tắc bắt buộc

- Không chạy model xong rồi để quên kết quả.
- Mỗi run phải có `Run ID` duy nhất.
- Chỉ dùng tracker để so sánh model, không so sánh bằng trí nhớ.
- Nếu đổi CV strategy hoặc seed, phải ghi rõ ở cột ghi chú.
