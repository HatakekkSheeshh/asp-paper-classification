# Roadmap plan cho bài tập lớn Data Mining (Kaggle competition)
**Đề tài:** Phân loại paper nghiên cứu ASP và các lĩnh vực liên quan  
**Mục tiêu mới:** Mỗi thành viên tự làm **full pipeline end-to-end trên 1 branch riêng**, sau đó so điểm Kaggle để chọn ra pipeline mạnh nhất làm bài chính của nhóm.

---

## 1) Tóm tắt bài toán

Nhóm cần xây dựng mô hình dự đoán `Label` cho từng paper dựa trên metadata và text.

Theo dữ liệu stage 1 hiện có:

- **Train:** 510 mẫu
- **Test:** 86 mẫu
- **Cột hiện có:** `title, venue, year, authors, doi, Label, id`
- **Lưu ý:** chưa có `abstract`, nhưng có `doi`
- **Thiếu dữ liệu:** `authors` thiếu một phần
- **Metric trên Kaggle:** **Macro F1-score**

### Nhận định nhanh

- Dataset nhỏ
- Feature text hiện tại chủ yếu là `title`
- `venue` chỉ có vài giá trị chính nên metadata không quá phức tạp
- Codebase hiện tại còn ít nên chưa cần chia cứng người này giữ text, người kia giữ metadata

Vì vậy, chiến lược hợp lý hơn ở giai đoạn này là:

1. Khóa luật chơi chung
2. Để mỗi người tự làm một pipeline hoàn chỉnh trên branch riêng
3. So kết quả công bằng
4. Chọn pipeline thắng cuộc để phát triển thành bài nộp chính

---

## 2) Vì sao đổi chiến lược làm việc

Kế hoạch cũ chia nhóm theo module kiểu:

- người A làm validation
- người B làm metadata
- người C làm text
- người D làm ensemble

Cách đó hợp với project lớn hoặc codebase đã đủ dày. Nhưng với dataset và code hiện tại còn gọn, cách chia đó có rủi ro:

- mỗi người chỉ nắm một mảnh nhỏ của pipeline
- phụ thuộc lẫn nhau nhiều nên chờ nhau
- khó biết cách tiếp cận nào thật sự tốt nhất
- dễ bị merge sớm một hướng chưa chắc là mạnh nhất

Kế hoạch mới ưu tiên:

- tốc độ thử nghiệm
- tính độc lập
- cạnh tranh lành mạnh giữa 4 hướng làm
- chọn winner dựa trên kết quả thật trên Kaggle

---

## 3) Luật chơi chung bắt buộc cho cả nhóm

Đây là phần phải **khóa cứng** để việc “đấu đầu” giữa các branch là công bằng.

### Dữ liệu và metric

- Dùng cùng dataset stage 1
- Cùng metric mục tiêu: `Macro F1`
- Cùng format submit: `id,Label`
- Không dùng dữ liệu ngoài nếu cả nhóm chưa thống nhất

### Validation

- Dùng cùng `StratifiedKFold`
- `n_splits = 5`
- `shuffle = True`
- `random_state = 42`
- Báo cáo cả `CV mean` và `CV std`

### Kỷ luật thí nghiệm

- Mỗi run phải ghi vào tracker
- Mỗi submission phải ghi vào submission log
- Ghi rõ `member`, `branch`, `feature set`, `model`, `CV`, `Public LB`
- Không chỉnh tay file submission

### Quy tắc chọn winner

Ưu tiên theo thứ tự:

1. **Public Kaggle score cao nhất**
2. Nếu chênh lệch Public LB quá nhỏ, dùng thêm:
   - CV Macro F1
   - độ ổn định qua folds
   - khả năng chạy lại pipeline
3. Branch nào không tái tạo được hoặc submit sai format thì không được chọn, dù điểm tình cờ cao

---

## 4) Cách tổ chức nhóm mới

### Mô hình làm việc

Mỗi người là **1 mini team độc lập** trên **1 branch riêng**, tự chịu trách nhiệm toàn bộ pipeline:

- đọc dữ liệu
- EDA nhanh
- preprocessing
- feature engineering
- training
- validation
- submission
- ghi chú approach

### Branch gợi ý

- `battle/m1-full-pipeline`
- `battle/m2-full-pipeline`
- `battle/m3-full-pipeline`
- `battle/m4-full-pipeline`

### Vai trò thực tế của từng thành viên

#### Member 1 — Coordinator + Competitor

- Thiết lập repo, tracker, CV rule, naming rule
- Đồng thời vẫn tự làm full pipeline trên branch riêng như mọi người
- Là người tổng hợp kết quả cuối và merge winner vào `main`

#### Member 2 — Competitor

- Tự làm full pipeline branch riêng
- Có thể thiên về metadata, data cleaning, feature thủ công nếu muốn

#### Member 3 — Competitor

- Tự làm full pipeline branch riêng
- Có thể thiên về text baseline mạnh, TF-IDF, linear model nếu muốn

#### Member 4 — Competitor

- Tự làm full pipeline branch riêng
- Có thể thiên về hybrid, ensemble, boosting nếu muốn

### Điểm quan trọng

Từ giờ, **mọi người đều làm full pipeline**, chỉ khác nhau ở chiến lược mạnh của từng người.

---

## 5) Deliverable bắt buộc của mỗi branch

Mỗi branch cần có tối thiểu:

1. Một pipeline chạy được end-to-end
2. Một notebook hoặc script chính để train/evaluate
3. Ít nhất một submission Kaggle hợp lệ
4. Một file note ngắn giải thích approach
5. Tracker thí nghiệm đã được cập nhật

### Gói bàn giao tối thiểu của mỗi thành viên

- `notebook` hoặc `script` chính
- `best submission`
- `CV summary`
- `Public LB`
- `2-5 ý chính` mô tả approach:
  - dùng feature gì
  - model gì
  - điều gì hiệu quả nhất
  - điểm yếu còn lại là gì

---

## 6) Chiến lược kỹ thuật gợi ý cho từng người

Vì đây là mô hình “đấu branch”, cả nhóm không nên copy nhau hoàn toàn. Nên chủ động tách chiến lược để tối đa hóa khả năng tìm ra winner.

### Hướng A — Text-first

- `title` làm nguồn tín hiệu chính
- TF-IDF word / char
- Logistic Regression / Linear SVM / Naive Bayes

### Hướng B — Metadata-first

- tập trung `venue`, `year`, `authors`, `doi`
- parse `author_count`, `doi_prefix`, `title_length`, `year_bucket`
- Logistic Regression / CatBoost / Random Forest

### Hướng C — Hybrid gọn

- TF-IDF `title` + one-hot / numeric metadata
- `ColumnTransformer`
- Logistic Regression / Linear SVM

### Hướng D — Hybrid mạnh / ensemble

- word TF-IDF + char TF-IDF + metadata
- weighted voting / soft voting / stacking đơn giản

Không bắt buộc mỗi người bám đúng một hướng, nhưng nên khác nhau tương đối để tránh 4 branch na ná nhau.

---

## 7) Roadmap mới theo giai đoạn

> Có thể triển khai trong **7–10 ngày**. Kế hoạch này phù hợp với mô hình “4 người, 4 branch, chọn winner”.

---

### Giai đoạn 1 — Khóa luật chơi chung (Ngày 1)

**Mục tiêu**

- Repo có cấu trúc ổn
- Cả nhóm dùng cùng data path, CV rule, tracker
- Tạo branch riêng cho từng người

**Việc cần làm**

- Chốt `StratifiedKFold + Macro F1`
- Chốt naming branch, file submit, run id
- Tạo 4 branch battle
- Mỗi người pull từ cùng một `main`

**Deliverable cuối ngày**

- 4 branch đã sẵn sàng
- Tracker chung hoạt động
- Cả nhóm hiểu cùng một luật so điểm

---

### Giai đoạn 2 — Baseline full pipeline cho từng người (Ngày 2–3)

**Mục tiêu**

Mỗi thành viên phải có **ít nhất 1 pipeline chạy từ đầu đến cuối**.

**Việc cần làm**

- Đọc train/test
- Chạy EDA nhanh
- Tạo baseline đầu tiên
- Tính CV
- Sinh submission đầu tiên

**Deliverable cuối giai đoạn**

- 4 baseline branch độc lập
- Mỗi người có ít nhất 1 submission hợp lệ
- Tracker đã có các run đầu tiên

---

### Giai đoạn 3 — Tối ưu độc lập trên từng branch (Ngày 4–6)

**Mục tiêu**

Mỗi người cải tiến branch của mình theo triết lý riêng.

**Các hướng nên thử**

- tuning TF-IDF
- thêm char n-gram
- thêm metadata features
- hybrid pipeline
- class weight
- CatBoost / LightGBM / XGBoost
- voting hoặc ensemble nhẹ

**Deliverable cuối giai đoạn**

- mỗi người có 2–5 run đáng chú ý
- mỗi người có best local model tạm thời
- có ít nhất 1 insight rõ ràng về branch của mình

---

### Giai đoạn 4 — Checkpoint giữa kỳ (Ngày 6 hoặc 7)

**Mục tiêu**

So nhanh kết quả để biết branch nào đang dẫn đầu.

**Nội dung họp**

- mỗi người trình bày:
  - best CV
  - best Public LB
  - feature/model đang hiệu quả nhất
  - hướng định cải tiến tiếp

**Lưu ý**

- Không merge branch ở bước này
- Chỉ dùng checkpoint để định hướng sprint cuối

---

### Giai đoạn 5 — Sprint cuối để đẩy điểm (Ngày 7–8)

**Mục tiêu**

Mỗi người tập trung đẩy branch của mình lên mức tốt nhất.

**Việc nên làm**

- sửa lỗi pipeline
- kiểm tra overfit
- làm error analysis nhanh
- thử 1–2 cải tiến cuối cùng có chủ đích
- tạo final candidate submission của từng người

**Deliverable cuối giai đoạn**

- 4 final candidate branch
- mỗi người có 1 submission tự tin nhất

---

### Giai đoạn 6 — Chọn winner branch (Ngày 9)

**Mục tiêu**

Chọn branch mạnh nhất làm bài chính.

**Cách chọn**

1. So `Public Kaggle score`
2. Nếu điểm sát nhau:
   - xem thêm `CV mean/std`
   - xem pipeline có sạch và tái tạo được không
   - xem branch nào dễ trình bày hơn trong báo cáo

**Kết quả cần có**

- chốt 1 branch thắng
- chốt 1 nhánh backup nếu cần

---

### Giai đoạn 7 — Hợp nhất và làm báo cáo (Ngày 10)

**Mục tiêu**

Biến branch thắng thành phiên bản nộp chính thức của nhóm.

**Việc cần làm**

- merge hoặc cherry-pick pipeline winner vào `main`
- chuẩn hóa README/notebook/report cho hướng thắng
- báo cáo không chỉ nói pipeline thắng, mà còn so sánh 4 hướng đã thử

**Deliverable cuối cùng**

- final submission
- repo sạch, chạy lại được
- báo cáo giải thích vì sao branch thắng được chọn
- slide có phần so sánh ngắn giữa 4 hướng

---

## 8) Template so sánh branch cuối cùng

| Member | Branch | Hướng tiếp cận | Best CV Macro F1 | Std | Best Public LB | Trạng thái |
|---|---|---|---:|---:|---:|---|
| M1 | `battle/m1-full-pipeline` | hybrid | 0.xxx | 0.xxx | 0.xxx | contender |
| M2 | `battle/m2-full-pipeline` | metadata-heavy | 0.xxx | 0.xxx | 0.xxx | contender |
| M3 | `battle/m3-full-pipeline` | text-first | 0.xxx | 0.xxx | 0.xxx | contender |
| M4 | `battle/m4-full-pipeline` | ensemble | 0.xxx | 0.xxx | 0.xxx | contender |

---

## 9) Backlog kỹ thuật ưu tiên cho mọi branch

### Bắt buộc

- [ ] Pipeline đọc data/train/predict end-to-end
- [ ] `StratifiedKFold + Macro F1`
- [ ] Ít nhất 1 text baseline
- [ ] Ít nhất 1 submission hợp lệ
- [ ] Ghi log thí nghiệm đầy đủ

### Nên làm

- [ ] char-level TF-IDF
- [ ] metadata features cơ bản
- [ ] hybrid text + metadata
- [ ] confusion matrix
- [ ] error analysis ngắn

### Chỉ làm nếu còn thời gian

- [ ] weighted voting
- [ ] stacking
- [ ] pseudo-labeling
- [ ] pretrained embeddings

---

## 10) Rủi ro chính và cách xử lý

### Rủi ro 1: 4 người làm giống hệt nhau

**Cách xử lý**

- mỗi người chọn một “trục mạnh” khác nhau
- chia hướng từ đầu: text-first, metadata-first, hybrid, ensemble

### Rủi ro 2: Quá phụ thuộc Public LB

**Cách xử lý**

- vẫn phải log CV
- nếu leaderboard chênh rất ít, dùng thêm CV và reproducibility để chốt

### Rủi ro 3: Branch thắng nhưng khó merge

**Cách xử lý**

- mỗi branch phải giữ notebook/script chạy được
- hạn chế sửa lung tung ngoài scope pipeline của mình

### Rủi ro 4: Không ai có pipeline hoàn chỉnh

**Cách xử lý**

- bắt buộc có baseline end-to-end từ rất sớm
- không được chỉ dừng ở EDA hoặc thử từng phần rời rạc

---

## 11) Definition of Done theo chiến lược mới

Nhóm được xem là hoàn thành tốt nếu:

- [ ] cả 4 branch đều có pipeline chạy được
- [ ] cả 4 branch đều có ít nhất 1 submission Kaggle
- [ ] có bảng so sánh đầy đủ giữa các branch
- [ ] chọn được 1 winner branch bằng tiêu chí rõ ràng
- [ ] merge được winner vào `main`
- [ ] có báo cáo giải thích vì sao winner tốt hơn các hướng còn lại

---

## 12) Kết luận chiến lược ngắn gọn

Với dataset nhỏ và codebase còn ít, hướng làm hiệu quả hơn lúc này không phải là chia cứng theo module, mà là:

1. **Khóa luật chơi chung**
2. **Cho mỗi người tự làm full pipeline trên branch riêng**
3. **So điểm Kaggle công bằng**
4. **Chọn winner branch làm bài chính**
5. **Dùng các branch còn lại như phần so sánh trong báo cáo**

Đây là cách vừa nhanh, vừa tạo cạnh tranh tích cực, vừa giúp nhóm tìm ra hướng mạnh nhất trước khi khóa bài nộp cuối.
