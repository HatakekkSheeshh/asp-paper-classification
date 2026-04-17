# Branching Strategy

## Mục tiêu

Giúp 4 thành viên làm song song mà ít conflict, dễ review và dễ merge.

## Quy ước branch

- `main`: nhánh ổn định, chỉ chứa code đã review nhanh trong nhóm.
- `feature/m1-validation`
- `feature/m2-eda-metadata`
- `feature/m3-text-baselines`
- `feature/m4-hybrid-ensemble`

Nếu có task nhỏ hơn, có thể thêm hậu tố:

- `feature/m2-eda-metadata-title-length`
- `feature/m4-hybrid-ensemble-voting`

## Quy ước commit message

- `docs: update cv strategy`
- `feat: add metadata feature builder`
- `notebook: add text baseline experiments`
- `report: draft eda summary`
- `fix: align submission id order`

## Quy trình đề xuất

1. Pull `main` mới nhất.
2. Làm việc trên branch riêng.
3. Cập nhật tracker thí nghiệm nếu có run mới.
4. Tự kiểm tra notebook/code chạy được.
5. Tạo pull request hoặc gửi diff cho Member 1 review.
6. Merge vào `main` khi không làm hỏng cấu trúc chung.

## Trách nhiệm merge

- Member 1 là người chốt merge cuối ngày hoặc trước mốc deliverable.
- Nếu hai người sửa cùng một notebook, nên tách phần code chung sang `src/` để giảm conflict.
