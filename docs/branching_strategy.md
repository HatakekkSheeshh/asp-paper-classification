# Branching Strategy

## Mục tiêu

Hỗ trợ mô hình làm việc mới: **4 thành viên, 4 branch độc lập, 4 pipeline hoàn chỉnh**, sau đó chọn branch mạnh nhất để merge vào `main`.

## Quy ước branch

- `main`: nhánh ổn định, chỉ chứa cấu trúc chung và pipeline đã được chọn cuối cùng
- `battle/m1-full-pipeline`
- `battle/m2-full-pipeline`
- `battle/m3-full-pipeline`
- `battle/m4-full-pipeline`

Trong giai đoạn “đấu branch”, mỗi người chủ yếu làm trên nhánh của mình, hạn chế merge chéo để tránh vô tình biến 4 hướng thành 1 hướng giống nhau.

## Quy ước commit message

- `feat: add text baseline pipeline`
- `feat: add metadata features and catboost`
- `tune: improve svm with char tfidf`
- `report: summarize branch results`
- `fix: align submission format`

## Workflow đề xuất

1. Pull `main` mới nhất.
2. Checkout branch battle của mình.
3. Tự phát triển full pipeline trên branch đó.
4. Ghi run vào tracker, kèm `member` và `branch`.
5. Tạo submission và ghi vào submission log.
6. Chỉ review chéo ở mức góp ý, không merge lẫn nhau trong lúc đang thi nội bộ.
7. Cuối kỳ, chọn winner branch rồi mới merge hoặc cherry-pick vào `main`.

## Quy tắc merge

- Không merge toàn bộ 4 branch vào `main`.
- Chỉ merge:
  - branch thắng cuộc
  - hoặc một phần rất cụ thể từ branch khác nếu cả nhóm thống nhất lấy thêm ý tưởng
- Nếu lấy ý tưởng từ branch thua, nên cherry-pick có chọn lọc thay vì trộn toàn bộ.

## Tiêu chí chọn branch thắng

Ưu tiên:

1. Public Kaggle score
2. CV Macro F1 và độ ổn định
3. Pipeline có chạy lại được không
4. Dễ trình bày trong báo cáo hay không

## Trách nhiệm cuối kỳ

- Member 1 hoặc người được nhóm giao sẽ:
  - tổng hợp bảng kết quả
  - xác nhận branch thắng
  - merge vào `main`
  - chuẩn hóa lại tài liệu nếu cần
