# src.evaluation

Module này phục vụ đánh giá model và phân tích lỗi.

## File hiện có

- `metrics.py`: `macro_f1` và scorer cho scikit-learn
- `error_analysis.py`: confusion matrix và per-class F1

## Cách dùng trong mô hình 4 branch

- Metric và helper đánh giá ở đây là baseline dùng chung.
- Mỗi branch có thể thêm hàm phân tích lỗi riêng, miễn vẫn giữ được khả năng so sánh công bằng.
