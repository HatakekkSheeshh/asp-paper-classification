# Roadmap plan cho bài tập lớn Data Mining (Kaggle competition)  
**Đề tài:** Phân loại paper nghiên cứu ASP và các lĩnh vực liên quan  
**Mục tiêu:** Tối ưu **Macro F1-score** trên Kaggle đồng thời có quy trình làm việc rõ ràng, có thể giải thích được trong báo cáo/thuyết trình.

---

## 1) Tóm tắt bài toán

Nhóm cần xây dựng mô hình dự đoán `Label` cho từng paper dựa trên dữ liệu metadata và text.  
Theo file thực tế nhóm đang có ở stage 1:

- **Train:** 510 mẫu
- **Test:** 86 mẫu
- **Cột hiện có:** `title, venue, year, authors, doi, Label, id`
- **Lưu ý quan trọng:** file thực tế **không có `abstract`**, nhưng lại có `doi`
- **Thiếu dữ liệu:** `authors` bị thiếu một phần
- **Metric:** **Macro F1-score** → cần quan tâm cân bằng giữa các lớp, không chỉ accuracy

### Nhận định nhanh từ dữ liệu hiện tại
- Số lớp: **5**
- Phân bố label tương đối lệch nhẹ, chưa quá nặng:
  - Label 1: 130
  - Label 2: 103
  - Label 3: 85
  - Label 4: 89
  - Label 5: 103
- `venue` hiện có 2 giá trị chính: `iclp`, `kr`
- Dataset nhỏ → rất phù hợp với:
  - TF-IDF + model tuyến tính / boosting
  - Feature engineering từ metadata
  - Stacking / soft voting
  - Cross-validation cẩn thận để tránh overfit leaderboard

---

## 2) Mục tiêu kỹ thuật của nhóm

### Mục tiêu bắt buộc
1. Có pipeline sạch, reproducible
2. Có ít nhất **3 baseline mạnh**
3. Có **cross-validation chuẩn theo Macro F1**
4. Có **ít nhất 1 mô hình kết hợp text + metadata**
5. Có file submit đúng format
6. Có báo cáo giải thích rõ:
   - chọn feature nào
   - tại sao chọn model đó
   - so sánh các thử nghiệm
   - phân tích lỗi

### Mục tiêu điểm số
- **Ngưỡng an toàn:** baseline chạy ổn, không lỗi, CV hợp lý
- **Ngưỡng tốt:** có tuning + ensemble + error analysis
- **Ngưỡng rất tốt:** có nhiều nhánh mô hình, blending hợp lý, báo cáo chặt chẽ, thuyết trình rõ insight

---

## 3) Chiến lược tổng thể để đạt kết quả tốt nhất

Vì dataset nhỏ và metric là Macro F1, chiến lược nên đi theo hướng:

1. **Làm thật chắc EDA và validation trước**
2. **Xây baseline nhanh** để có mốc so sánh
3. **Tách 3 nhánh feature**
   - Nhánh A: text từ `title`
   - Nhánh B: metadata (`venue`, `year`, `authors`, `doi`)
   - Nhánh C: hybrid = text + metadata
4. **Thử nhiều model cổ điển nhưng mạnh cho text nhỏ**
   - Logistic Regression
   - Linear SVM
   - Naive Bayes
   - Random Forest / XGBoost / LightGBM / CatBoost (nếu encode hợp lý)
5. **Tối ưu Macro F1 bằng cross-validation phân tầng**
6. **Error analysis theo từng lớp**
7. **Ensemble/blending** thay vì phụ thuộc 1 mô hình duy nhất
8. **Giữ log thí nghiệm** để tránh làm lại, tránh “cảm giác model tốt”

---

## 4) Phân chia vai trò cho 4 thành viên

Để tránh chồng chéo, mỗi người có **1 vai trò chính** và **1 vai trò phụ**.

---

### Thành viên 1 — Project Lead + Validation Owner
**Vai trò chính**
- Quản lý tiến độ
- Thiết kế pipeline chung
- Chịu trách nhiệm validation và rule nộp Kaggle

**Nhiệm vụ chính**
- Tạo repo / folder structure
- Quy định cách đặt tên notebook, file submit, file log
- Thiết kế `StratifiedKFold` cho Macro F1
- Kiểm tra data leakage, duplicate, split strategy
- Tổng hợp kết quả từ mọi người
- Chọn final ensemble để submit

**Vai trò phụ**
- Review code và merge branch
- Chuẩn hóa format báo cáo/thuyết trình

**Deliverables**
- `README.md`
- `configs/`
- `cv_strategy.md`
- bảng tổng hợp experiment
- final submission shortlist

---

### Thành viên 2 — EDA + Data Cleaning + Metadata Features
**Vai trò chính**
- Phân tích dữ liệu
- Xử lý dữ liệu thiếu, chuẩn hóa metadata
- Tạo feature từ `authors`, `venue`, `year`, `doi`

**Nhiệm vụ chính**
- Kiểm tra missing values, duplicates, outliers
- Phân tích phân bố label
- Phân tích title length, số author, năm xuất bản
- Chuẩn hóa `authors`:
  - số lượng tác giả
  - author xuất hiện nhiều
  - first author / last author
- Feature từ `doi`:
  - publisher prefix
  - pattern journal/conference
  - độ dài DOI
- Encode `venue`, `year bin`, `author_count`
- Làm báo cáo EDA có biểu đồ và insight

**Vai trò phụ**
- Hỗ trợ Member 3/4 ghép metadata vào pipeline model

**Deliverables**
- `notebooks/eda.ipynb`
- `src/features_metadata.py`
- `reports/eda_summary.md`

---

### Thành viên 3 — Text Modeling Owner
**Vai trò chính**
- Xử lý text và xây các model baseline / advanced cho `title`

**Nhiệm vụ chính**
- Tiền xử lý `title`
  - lowercase
  - giữ/bỏ punctuation có kiểm chứng
  - stopwords thử nghiệm
  - stemming/lemmatization nếu cần
- Tạo vectorizer:
  - word-level TF-IDF
  - char-level TF-IDF
  - word + char combined
  - n-gram (1,2), (1,3), char 3–5
- Huấn luyện baseline:
  - Multinomial Naive Bayes
  - Logistic Regression
  - Linear SVM
- Tuning:
  - max_features
  - min_df / max_df
  - n-gram range
  - class_weight

**Vai trò phụ**
- Phối hợp với Member 4 để stacking/blending

**Deliverables**
- `notebooks/text_baselines.ipynb`
- `src/text_pipeline.py`
- bảng kết quả CV của từng text model

---

### Thành viên 4 — Advanced Modeling + Ensemble + Reporting Support
**Vai trò chính**
- Xây mô hình nâng cao
- Ensemble / stacking / blending
- Hỗ trợ làm submission cuối

**Nhiệm vụ chính**
- Thử hybrid model:
  - TF-IDF title + metadata
  - FeatureUnion / ColumnTransformer
- Thử tree/boosting nếu hợp lý:
  - LightGBM / XGBoost / CatBoost
- Thử pseudo-labeling **nếu và chỉ nếu** CV ổn định
- Thử ensemble:
  - soft voting
  - weighted voting
  - stacking level-2
- Phân tích confusion matrix
- Tổng hợp feature importance / top n-grams / lỗi theo lớp

**Vai trò phụ**
- Hỗ trợ dựng slide, bảng so sánh final

**Deliverables**
- `notebooks/hybrid_ensemble.ipynb`
- `src/ensemble.py`
- `reports/error_analysis.md`
- 2–3 final submission files

---

## 5) Cách phối hợp giữa 4 thành viên

### Quy tắc chung
- Mỗi người làm trên **1 branch riêng**
- Mọi kết quả đều phải ghi vào **bảng experiment chung**
- Không dùng leaderboard làm tiêu chuẩn duy nhất
- Quyết định cuối dựa trên:
  1. CV Macro F1
  2. độ ổn định qua folds
  3. tính hợp lý của mô hình
  4. leaderboard chỉ dùng để tham khảo

### Bảng log thí nghiệm nên có
| Run ID | Người phụ trách | Feature set | Model | CV Macro F1 | Std | Public LB | Ghi chú |
|---|---|---|---|---:|---:|---:|---|
| exp_001 | M3 | TF-IDF title word(1,2) | Logistic Regression | 0.xxx | 0.xxx | 0.xxx | baseline |
| exp_002 | M2 | metadata only | CatBoost | 0.xxx | 0.xxx | 0.xxx | venue mạnh |
| exp_003 | M4 | title + metadata | Linear SVM | 0.xxx | 0.xxx | 0.xxx | hybrid |

---

## 6) Roadmap chi tiết theo giai đoạn

> Có thể triển khai trong **10 ngày**. Nếu nhóm ít thời gian, có thể nén xuống **7 ngày** bằng cách rút bớt tuning và ensemble.

---

# Giai đoạn 1 — Khởi động dự án (Ngày 1)
## Mục tiêu
- Hiểu dữ liệu
- Chia việc rõ
- Dựng khung dự án

## Việc cần làm
### Member 1
- Tạo repo GitHub / Drive folder
- Tạo cấu trúc thư mục
- Tạo template experiment tracker
- Tạo baseline split bằng `StratifiedKFold`

### Member 2
- Chạy EDA ban đầu
- Kiểm tra missing, duplicate, class balance

### Member 3
- Viết notebook baseline đọc data + TF-IDF title

### Member 4
- Chuẩn bị notebook evaluation + confusion matrix + submit generator

## Deliverables cuối ngày
- Repo chạy được
- Cả nhóm đọc được data
- Có EDA sơ bộ
- Có kế hoạch branch và naming

---

# Giai đoạn 2 — Data audit & feature hypotheses (Ngày 2)
## Mục tiêu
Tìm ra các feature đáng thử trước khi model hóa nặng.

## Việc cần làm
### Member 2 lead
- Phân tích:
  - label vs venue
  - label vs year
  - label vs title length
  - label vs author count
  - pattern DOI
- Xem title của từng lớp có từ khóa đặc trưng gì

### Member 1 support
- Kiểm tra duplicate title/doi
- Xác định có cần deduplicate hay giữ nguyên

### Member 3 support
- Xuất top n-grams theo label

### Member 4 support
- Chuẩn hóa hàm đánh giá Macro F1

## Deliverables cuối ngày
- File `eda_summary.md`
- Danh sách feature hypothesis:
  - venue có thể predictive
  - year có thể phản ánh xu hướng
  - authors/doi có tín hiệu phụ
  - title là feature chính

---

# Giai đoạn 3 — Baseline nhanh và chắc (Ngày 3–4)
## Mục tiêu
Có ít nhất 3 baseline tốt, làm mốc để cải tiến.

## Việc cần làm
### Member 3 lead
Chạy các baseline text:
1. TF-IDF word unigram + Logistic Regression
2. TF-IDF word (1,2) + Linear SVM
3. TF-IDF char (3,5) + Logistic Regression
4. TF-IDF word + char combined

### Member 2 lead song song
Chạy baseline metadata:
1. venue + year + author_count
2. venue + year + doi features
3. CatBoost / Logistic Regression / Random Forest cho metadata-only

### Member 1
- Chuẩn hóa cách ghi kết quả CV
- Kiểm tra fold variance
- So sánh fairness giữa các run

### Member 4
- Tạo pipeline feature union
- Chuẩn bị hybrid baseline

## Deliverables cuối ngày 4
- Bảng so sánh baseline đầy đủ
- Chọn ra:
  - best text-only
  - best metadata-only
  - 1 candidate hybrid

---

# Giai đoạn 4 — Hybrid modeling & tuning (Ngày 5–6)
## Mục tiêu
Đẩy điểm số bằng cách kết hợp feature và tuning có kiểm soát.

## Việc cần làm
### Member 4 lead
- Kết hợp:
  - TF-IDF title + OneHot venue + numeric year + author_count + doi stats
- Thử:
  - Logistic Regression
  - Linear SVM
  - LightGBM/CatBoost trên feature phù hợp
- Tuning:
  - regularization
  - class_weight
  - max_features
  - ngram_range

### Member 3
- Tuning vectorizer:
  - min_df
  - max_df
  - analyzer
  - sublinear_tf
- So sánh word vs char vs word+char

### Member 2
- Thêm feature:
  - first author frequency
  - authors hash / rare-author indicator
  - year bucket
  - DOI prefix category

### Member 1
- Theo dõi xem tuning nào có cải thiện thực sự
- Loại bỏ run “ảo” do variance cao

## Deliverables cuối ngày 6
- 2–3 model tốt nhất theo CV
- Bảng tuning có lý do chọn

---

# Giai đoạn 5 — Error analysis & class-focused improvement (Ngày 7)
## Mục tiêu
Tăng Macro F1 bằng cách tập trung vào lớp khó.

## Việc cần làm
### Member 4 lead
- Vẽ confusion matrix
- Xem lớp nào bị nhầm nhiều nhất
- Tính F1 theo từng lớp

### Member 3
- Trích các title bị đoán sai
- Xem mô hình text đang nhầm ở đâu:
  - title quá ngắn
  - từ khóa chồng lấn giữa lớp
  - venue áp đảo dự đoán

### Member 2
- So lại metadata của các mẫu đoán sai
- Kiểm tra missing authors có làm model lệch không

### Member 1
- Tổ chức họp nhóm 30–45 phút chốt hướng cải thiện cuối

## Deliverables cuối ngày
- `error_analysis.md`
- Danh sách hành động:
  - tăng trọng số lớp nào?
  - dùng ensemble không?
  - loại feature nào gây nhiễu?

---

# Giai đoạn 6 — Ensemble & final submission (Ngày 8–9)
## Mục tiêu
Tạo submission cuối đủ mạnh và ổn định.

## Việc cần làm
### Member 4 lead
- Ensemble 2–4 model tốt nhất:
  - soft voting
  - weighted voting
  - stacking đơn giản
- So sánh CV trước/sau ensemble

### Member 1
- Chọn final candidates để submit
- Quản lý version submission:
  - `sub_v1_baseline.csv`
  - `sub_v2_hybrid.csv`
  - `sub_v3_ensemble.csv`

### Member 3
- Kiểm tra consistency pipeline train/test
- Tránh mismatch vocabulary

### Member 2
- Kiểm tra format file submit
- Audit lại missing / encoding / id mapping

## Deliverables cuối ngày 9
- 2–3 submission cuối
- Bảng lý do chọn final submission
- File final dùng để nộp Kaggle

---

# Giai đoạn 7 — Báo cáo & thuyết trình (Ngày 10)
## Mục tiêu
Biến quá trình làm thành câu chuyện chặt chẽ, thuyết phục.

## Việc cần làm
### Member 1 lead
- Dàn khung báo cáo
- Phân công ai nói phần nào

### Member 2
- Viết phần dataset understanding + EDA + metadata features

### Member 3
- Viết phần text representation + baseline + tuning

### Member 4
- Viết phần hybrid model + ensemble + error analysis + final result

## Cấu trúc báo cáo gợi ý
1. Giới thiệu bài toán
2. Mô tả dữ liệu
3. EDA và insight
4. Tiền xử lý
5. Feature engineering
6. Mô hình thử nghiệm
7. Validation strategy
8. Kết quả
9. Error analysis
10. Kết luận và hướng cải thiện

## Deliverables cuối cùng
- Báo cáo hoàn chỉnh
- Slide
- Notebook sạch
- Final submission
- Repo có thể chạy lại

---

## 7) Backlog kỹ thuật chi tiết cần ưu tiên

### Mức ưu tiên cao (phải làm)
- [ ] StratifiedKFold + Macro F1 scorer
- [ ] TF-IDF word-level baseline
- [ ] TF-IDF char-level baseline
- [ ] Metadata features cơ bản
- [ ] Hybrid model
- [ ] Confusion matrix
- [ ] File submit đúng format

### Mức ưu tiên trung bình (nên làm)
- [ ] DOI parsing
- [ ] author_count, rare_author features
- [ ] class_weight tuning
- [ ] weighted voting ensemble
- [ ] calibration hoặc threshold check nếu cần

### Mức ưu tiên nâng cao (chỉ làm khi đã ổn)
- [ ] pseudo-labeling
- [ ] stacking level-2
- [ ] pretrained text embedding
- [ ] sentence transformer cho title
- [ ] domain keyword lexicon feature

---

## 8) Đề xuất pipeline mô hình theo thứ tự thử nghiệm

### Baseline 1
- Input: `title`
- Feature: TF-IDF word unigram/bigram
- Model: Logistic Regression
- Mục tiêu: baseline ổn định, nhanh

### Baseline 2
- Input: `title`
- Feature: TF-IDF char 3–5 grams
- Model: Linear SVM
- Mục tiêu: bắt pattern từ thuật ngữ học thuật, acronym, tên phương pháp

### Baseline 3
- Input: `venue`, `year`, `authors`, `doi`
- Feature: one-hot + numeric + handcrafted
- Model: CatBoost / Logistic Regression
- Mục tiêu: đo tín hiệu từ metadata

### Strong candidate 1
- Input: title + metadata
- Feature: ColumnTransformer (TF-IDF + OneHot + numeric)
- Model: Linear SVM / Logistic Regression

### Strong candidate 2
- Input: title + metadata
- Feature: word TF-IDF + char TF-IDF + metadata
- Model: ensemble

### Final candidate
- Blend:
  - best text-only
  - best hybrid
  - best metadata-augmented model

---

## 9) Chuẩn kỹ thuật bắt buộc để tránh mất điểm oan

- Luôn fix `random_state`
- Luôn dùng cùng một CV split để so sánh model
- Không nhìn leaderboard quá nhiều để tránh overfit public LB
- Không đưa `Label` hay biến rò rỉ vào feature
- Khi join feature train/test phải đảm bảo cột khớp
- Kiểm tra submit:
  - đúng số dòng
  - đúng thứ tự `id`
  - cột tên chính xác: `id,Label`
- Ghi lại mọi thí nghiệm vào bảng log
- Notebook final phải chạy từ đầu đến cuối

---

## 10) Rủi ro chính và cách xử lý

### Rủi ro 1: Dataset nhỏ → kết quả dao động
**Cách xử lý**
- Dùng Stratified K-Fold
- Báo cáo mean + std
- Không kết luận chỉ từ 1 split

### Rủi ro 2: Overfit leaderboard
**Cách xử lý**
- Chọn model theo CV
- Chỉ submit các candidate thực sự khác nhau

### Rủi ro 3: Chồng chéo công việc nhóm
**Cách xử lý**
- Mỗi người có deliverable rõ
- Có experiment sheet chung
- Họp ngắn mỗi ngày 10–15 phút

### Rủi ro 4: Code không ghép được
**Cách xử lý**
- Thống nhất path, naming, environment từ ngày đầu
- Dùng `requirements.txt`

### Rủi ro 5: Metadata gây nhiễu
**Cách xử lý**
- Luôn so sánh với text-only baseline
- Chỉ giữ feature nào cải thiện CV

---

## 11) Lịch họp nhóm đề xuất

### Họp 1 — Kickoff (Ngày 1)
- Chốt vai trò
- Chốt cấu trúc repo
- Chốt metric + validation

### Họp 2 — Sau baseline (Ngày 4)
- Xem baseline nào mạnh
- Quyết định hướng tuning

### Họp 3 — Sau error analysis (Ngày 7)
- Chốt final model strategy
- Chia việc làm báo cáo

### Họp 4 — Trước khi nộp (Ngày 10)
- Review submit
- Review slide/báo cáo
- Kiểm tra lần cuối format

---

## 12) Cấu trúc thư mục đề xuất

```text
project/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── submissions/
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_text_baseline.ipynb
│   ├── 03_metadata_features.ipynb
│   ├── 04_hybrid_models.ipynb
│   └── 05_ensemble_error_analysis.ipynb
│
├── src/
│   ├── utils.py
│   ├── metrics.py
│   ├── preprocess.py
│   ├── features_metadata.py
│   ├── text_pipeline.py
│   └── ensemble.py
│
├── reports/
│   ├── eda_summary.md
│   ├── error_analysis.md
│   └── final_report.md
│
├── configs/
│   └── experiment_config.yaml
│
├── requirements.txt
└── README.md
```

---

## 13) Definition of Done

Nhóm được xem là hoàn thành tốt nếu đạt đủ các điều kiện sau:

- [ ] Có EDA và insight rõ ràng
- [ ] Có ít nhất 3 baseline được so sánh công bằng
- [ ] Có validation chuẩn bằng Macro F1
- [ ] Có ít nhất 1 mô hình hybrid
- [ ] Có error analysis theo lớp
- [ ] Có ensemble hoặc lý do rõ vì sao không ensemble
- [ ] Có submission cuối đúng format
- [ ] Có báo cáo giải thích logic, không chỉ đưa điểm số

---

## 14) Kết luận chiến lược ngắn gọn

Để đạt kết quả tốt nhất, nhóm nên đi theo hướng:

1. **Làm chắc validation**
2. **Xây baseline text thật mạnh**
3. **Khai thác metadata thông minh nhưng không lạm dụng**
4. **Dùng hybrid model**
5. **Phân tích lỗi để cải thiện Macro F1**
6. **Dùng ensemble ở giai đoạn cuối**
7. **Ghi log đầy đủ để báo cáo/thuyết trình thuyết phục**

---

## 15) Phân công ngắn gọn để bắt đầu ngay hôm nay

### Member 1
- Setup repo, CV strategy, experiment tracker, merge kết quả

### Member 2
- EDA, data cleaning, metadata features, insight report

### Member 3
- TF-IDF + text baselines + tuning

### Member 4
- Hybrid models, ensemble, error analysis, final submission support

---

**Khuyến nghị cuối:**  
Nếu thời gian có hạn, hãy ưu tiên theo thứ tự:
1. text baseline  
2. hybrid text + metadata  
3. error analysis  
4. ensemble  
5. báo cáo sạch và có lý do rõ ràng  

Với dataset nhỏ như stage 1, một pipeline **TF-IDF tốt + Linear model tốt + metadata vừa đủ + ensemble gọn** thường sẽ là hướng có tỷ lệ hiệu quả / công sức rất cao.
