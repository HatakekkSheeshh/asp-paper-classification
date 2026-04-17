# CV Strategy

## Mục tiêu

Giữ cho cuộc đua giữa các branch là **công bằng** và **so sánh được**.

## Quy ước mặc định

- Dùng `StratifiedKFold`
- `n_splits = 5`
- `shuffle = True`
- `random_state = 42`
- Mọi branch dùng cùng một chiến lược split

## Vì sao phải khóa CV

- Dataset nhỏ nên kết quả dễ dao động
- Nếu mỗi người dùng một split khác nhau thì không thể so CV công bằng
- Dù winner cuối cùng ưu tiên theo Kaggle score, nhóm vẫn cần CV để:
  - kiểm tra branch đó có ổn định không
  - tránh chọn nhầm một pipeline chỉ ăn may trên public leaderboard

## Checklist trước khi báo cáo kết quả

- Đã dùng đúng target column `Label`
- Đã dùng cùng CV split với cả nhóm
- Không có leakage
- Có báo cáo:
  - `CV mean`
  - `CV std`
  - feature set
  - model chính
  - best submission tương ứng

## Nguyên tắc chọn model trong từng branch

Mỗi thành viên có thể chọn candidate cuối theo:

1. CV tốt nhất trên branch của mình
2. Sau đó submit lên Kaggle để kiểm chứng
3. Nếu Public LB tốt hơn baseline cũ thì giữ làm candidate chính

## Nguyên tắc chọn winner toàn nhóm

Ưu tiên:

1. Public LB cao nhất
2. Nếu chênh lệch rất nhỏ, xem thêm:
   - CV mean
   - CV std
   - khả năng tái tạo
   - độ sạch của pipeline

## Kiểm tra leakage nên làm sớm

- Duplicate theo `title`
- Duplicate theo `doi`
- Một paper xuất hiện nhiều biến thể
- Feature vô tình dùng thông tin ngoài train
