# Source Code

`src/` là package code dùng chung cho cả nhóm. Mục tiêu là gom phần logic tái sử dụng khỏi notebook để:

- giảm conflict khi nhiều người cùng sửa notebook
- tái sử dụng được giữa train, evaluation và submission
- giúp báo cáo lại quy trình rõ ràng hơn

## Cấu trúc

- `data/`: load dữ liệu và tạo split CV
- `features/`: tiền xử lý text và metadata feature engineering
- `models/`: baseline, hybrid, ensemble
- `evaluation/`: metric, confusion matrix, phân tích lỗi
- `utils/`: path, config, logging helper

## Cách dùng

- Notebook chỉ nên orchestration và visualization.
- Logic nhiều lần dùng lại nên được chuyển vào `src/`.
- Khi thêm module mới, nhớ bổ sung README hoặc docstring ngắn gọn để người khác biết mục đích file đó.
