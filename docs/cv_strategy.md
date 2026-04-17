# CV Strategy

## Mục tiêu

Đảm bảo mọi mô hình được so sánh công bằng theo đúng metric `Macro F1-score` của Kaggle.

## Quy ước mặc định

- Dùng `StratifiedKFold`
- `n_splits = 5`
- `shuffle = True`
- `random_state = 42`
- Giữ nguyên cùng một chiến lược split cho toàn bộ baseline, tuning và ensemble

## Vì sao chọn như vậy

- Dataset nhỏ nên cần tận dụng nhiều dữ liệu train hơn hold-out đơn.
- Bài toán có 5 lớp, phân bố hơi lệch nên cần stratify để giữ tỷ lệ nhãn giữa các fold.
- Macro F1 nhạy với lớp yếu, vì vậy phải nhìn cả `mean` và `std`, không chỉ nhìn một fold.

## Checklist trước khi báo cáo điểm CV

- Đã dùng cùng một target column là `Label`.
- Không có leakage từ nhãn hoặc feature hậu kiểm.
- Không thay đổi split seed giữa các run khi chưa ghi log rõ ràng.
- Báo cáo đủ:
  - `CV mean`
  - `CV std`
  - mô tả feature set
  - model và hyperparameter chính

## Nguyên tắc chọn model

Ưu tiên theo thứ tự:

1. Mean Macro F1 tốt
2. Độ ổn định qua folds tốt
3. Pipeline hợp lý và tái tạo được
4. Public leaderboard chỉ dùng để tham khảo

## Kiểm tra leakage nên làm sớm

- Duplicate theo `title`
- Duplicate theo `doi`
- Cùng paper xuất hiện nhiều bản ghi
- Feature được tạo sau khi đã nhìn test hoặc leaderboard
