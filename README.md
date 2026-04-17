# Kaggle Data Mining Team 4

Repo này là skeleton làm bài tập lớn Data Mining cho đề tài phân loại paper nghiên cứu ASP và các lĩnh vực liên quan. Mục tiêu chính của nhóm là tối ưu `Macro F1-score` trên Kaggle nhưng vẫn giữ được quy trình làm việc rõ ràng, dễ giải thích trong báo cáo và dễ phối hợp giữa 4 thành viên.

## Mục tiêu của repo

- Có cấu trúc thư mục thống nhất để cả nhóm làm song song mà ít đụng nhau.
- Có config, tracker thí nghiệm và guideline validation ngay từ đầu.
- Có module `src/` đủ rõ để Member 2, 3, 4 nhận việc và code tiếp ngay.
- Có notebook khung, report template và nơi lưu submission theo đúng roadmap.

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
5. Ghi log mọi lần chạy vào `experiments/experiment_tracker.csv`.
6. Đọc `docs/cv_strategy.md` trước khi so sánh model.

## Cấu trúc chính

```text
.
├── configs/              # config chung cho path, CV, baseline
├── data/                 # nơi chuẩn hóa dữ liệu raw/interim/processed/submission
├── dataset_stage1/       # dữ liệu gốc hiện có của nhóm
├── docs/                 # roadmap, chiến lược CV, workflow cộng tác
├── experiments/          # tracker thí nghiệm và log submission
├── notebooks/            # notebook khung theo từng giai đoạn
├── reports/              # EDA, error analysis, final report
├── src/                  # code package dùng chung cho cả nhóm
├── .gitignore
├── README.md
└── requirements.txt
```

## Phân chia ownership gợi ý

- Member 1: `configs/`, `docs/`, `experiments/`, validation, final merge.
- Member 2: `src/features/`, `notebooks/01_eda.ipynb`, `notebooks/03_metadata_features.ipynb`, `reports/eda_summary.md`.
- Member 3: `src/features/text.py`, `src/models/baselines.py`, `notebooks/02_text_baseline.ipynb`.
- Member 4: `src/models/hybrid.py`, `src/models/ensemble.py`, `src/evaluation/`, `notebooks/04_hybrid_models.ipynb`, `notebooks/05_ensemble_error_analysis.ipynb`.

## Quy ước làm việc

- Mỗi người làm trên một branch riêng.
- Không so sánh model bằng leaderboard public một cách đơn lẻ.
- Mọi run đều phải có `Run ID` trong tracker.
- Dùng cùng một split CV để so sánh công bằng.
- Submission đặt tên theo mẫu `sub_vX_<short_desc>.csv`.

## Tài liệu nên đọc đầu tiên

- `docs/roadmap_kaggle_data_mining_team4.md`
- `docs/cv_strategy.md`
- `docs/branching_strategy.md`
- `experiments/README.md`

## Gợi ý workflow trong tuần đầu

1. Member 1 khóa config path, CV strategy và tracker.
2. Member 2 chạy EDA, thống kê missing, duplicate và feature hypothesis.
3. Member 3 dựng text baseline TF-IDF + Logistic Regression / Linear SVM.
4. Member 4 chuẩn bị pipeline hybrid, confusion matrix và ensemble skeleton.

## Trạng thái dữ liệu hiện tại

Dữ liệu gốc vẫn được giữ nguyên trong `dataset_stage1/` để tránh làm xáo trộn file nhóm đang dùng. Các module và notebook mặc định đang tham chiếu tới đường dẫn này trong config. Khi nhóm muốn chuẩn hóa lại, có thể copy sang `data/raw/` mà không làm hỏng cấu trúc hiện tại.
