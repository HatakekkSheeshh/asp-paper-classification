# Experiments

Thư mục này dùng để ghi lại toàn bộ thí nghiệm và submission của nhóm.

## File hiện có

- `experiment_tracker.csv`: log mọi run đã train hoặc evaluate
- `submission_log.csv`: log mọi file đã submit lên Kaggle

## Quy tắc bắt buộc

- Mỗi run phải có `Run ID` duy nhất
- Phải ghi rõ `owner` và `branch_name`
- Mỗi submission phải map được về đúng run và đúng branch
- Không so branch bằng trí nhớ; luôn nhìn tracker trước

## Cách dùng trong mô hình 4 branch

- Mỗi thành viên vẫn dùng cùng một tracker chung
- Nhưng mọi dòng phải ghi rõ branch để cuối kỳ so branch công bằng
- Nếu một branch có nhiều candidate, đánh dấu candidate mạnh nhất ở cột `notes`
