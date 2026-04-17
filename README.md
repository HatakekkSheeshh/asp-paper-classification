# Kaggle Data Mining Team 4

Repo này là skeleton làm bài tập lớn Data Mining cho đề tài phân loại paper nghiên cứu ASP và các lĩnh vực liên quan. Cách làm hiện tại của nhóm là **4 thành viên tự làm full pipeline trên 4 branch riêng**, sau đó so điểm Kaggle để chọn ra branch mạnh nhất làm bài chính.

## Mục tiêu của repo

- Có cấu trúc thư mục chung để mọi branch bắt đầu từ cùng một nền.
- Có config, tracker thí nghiệm và luật validation thống nhất.
- Cho phép mỗi thành viên phát triển một pipeline độc lập, end-to-end.
- Dễ tổng hợp kết quả để chọn winner branch và merge về `main`.

## Bắt đầu nhanh

1. Tạo môi trường Python 3.10+.
2. Cài thư viện:

```bash
pip install -r requirements.txt
```

3. Kiểm tra dữ liệu stage 1 đang nằm ở:
   - `dataset_stage1/Stage_1_publcitrain.csv`
   - `dataset_stage1/test (2).csv`
4. Xem config chung tại `configs/experiment_config.yaml`.
5. Đọc `docs/cv_strategy.md` và `docs/branching_strategy.md` trước khi bắt đầu branch riêng.
6. Ghi log mọi lần chạy vào `experiments/experiment_tracker.csv`.

## Cấu trúc chính

```text
.
├── configs/              # config chung cho data path, CV, baseline defaults
├── data/                 # nơi chứa raw/interim/processed/submissions
├── dataset_stage1/       # dữ liệu gốc hiện có của nhóm
├── docs/                 # roadmap, CV strategy, branch battle strategy
├── experiments/          # tracker thí nghiệm và log submission
├── notebooks/            # notebook khung
├── reports/              # report template và error analysis
├── src/                  # code package dùng chung làm điểm xuất phát
├── .gitignore
├── README.md
└── requirements.txt
```

## Cách nhóm đang làm việc

### Shared core

Cả nhóm dùng chung:

- cùng dataset
- cùng metric `Macro F1`
- cùng `StratifiedKFold`
- cùng tracker/log
- cùng format submission

### Battle branches

Mỗi người tạo và phát triển một branch riêng:

- `battle/m1-full-pipeline`
- `battle/m2-full-pipeline`
- `battle/m3-full-pipeline`
- `battle/m4-full-pipeline`

Trên branch của mình, mỗi thành viên tự làm:

- EDA nhanh
- preprocessing
- feature engineering
- model training
- CV evaluation
- Kaggle submission

## Quy tắc chọn hướng chính

Ưu tiên:

1. Public Kaggle score cao nhất
2. Nếu điểm sát nhau, xem thêm CV mean/std và khả năng chạy lại pipeline

## Tài liệu nên đọc đầu tiên

- `docs/roadmap_kaggle_data_mining_team4.md`
- `docs/cv_strategy.md`
- `docs/branching_strategy.md`
- `experiments/README.md`

## Trạng thái dữ liệu hiện tại

Dữ liệu gốc vẫn được giữ nguyên trong `dataset_stage1/` để tránh làm xáo trộn file nhóm đang dùng. Các module và notebook mặc định đang tham chiếu tới đường dẫn này trong config. Khi nhóm muốn chuẩn hóa lại, có thể copy sang `data/raw/` mà không làm hỏng cấu trúc hiện tại.
