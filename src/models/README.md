# src.models

Module này gom các constructor model/pipeline để nhóm dễ tái sử dụng.

## File hiện có

- `baselines.py`: model tuyến tính cơ bản cho text hoặc metadata.
- `hybrid.py`: helper tạo preprocessor cho text + categorical + numeric.
- `ensemble.py`: helper tạo soft voting classifier.

## Lưu ý

- Chỉ nên đặt constructor và logic tạo pipeline ở đây.
- Việc tuning, loop CV và visualization nên để notebook hoặc script riêng.
