### 오버피팅 개선 외 큰 효과 없음

| Train Accuracy | Train F1 | Test Accuracy | Test F1 | Augmentation Parameters |
|----------------|----------|---------------|---------|-------------------------|
| 0.6861         | 0.6845   | 0.6567        | 0.6641  | Baseline (No augmentation) |
||||||
| 0.7014         | 0.6981   | 0.6644        | 0.6725  | blur_limit=(3, 3), sigma_limit=(0.1, 2.0), p=0.1 |
| 0.7069         | 0.7066   | 0.6622        | 0.6720  | blur_limit=(3, 3), sigma_limit=(0.1, 3.0), p=0.1 |
| 0.6875         | 0.6852   | 0.6522        | 0.6631  | blur_limit=(5, 5), sigma_limit=(0.1, 2.0), p=0.1 |
| 0.6958         | 0.6944   | 0.6489        | 0.6567  | blur_limit=(5, 5), sigma_limit=(0.1, 3.0), p=0.1 |
| 0.6917         | 0.6903   | 0.6433        | 0.6518  | blur_limit=(7, 7), sigma_limit=(0.1, 2.0), p=0.1 |
| 0.6903         | 0.6855   | 0.6567        | 0.6657  | blur_limit=(7, 7), sigma_limit=(0.1, 3.0), p=0.1 |
||||||
| 0.7000         | 0.6969   | 0.6611        | 0.6700  | blur_limit=(3, 7), sigma_limit=(0.1, 2.0), p=0.1 |

| Augmentation Parameters | Train Accuracy | Train F1 | Test Accuracy | Test F1 |
|-------------------------|----------------|----------|---------------|---------|
| Baseline (No augmentation) | ███████ 0.6861 | ███████ 0.6845 | ████████████ 0.6567 | ████████ 0.6641 |
||||||
| blur=(3, 3), sigma=(0.1, 2.0), p=0.1 | ███████████ 0.7014 | ███████████ 0.6981 | ████████████ 0.6644 | ████████████ 0.6725 |
| blur=(3, 3), sigma=(0.1, 3.0), p=0.1 | ████████████ 0.7069 | ████████████ 0.7066 | ███████████ 0.6622 | ████████████ 0.6720 |
| blur=(5, 5), sigma=(0.1, 2.0), p=0.1 | ███████ 0.6875 | ███████ 0.6852 | ████████ 0.6522 | ███████ 0.6631 |
| blur=(5, 5), sigma=(0.1, 3.0), p=0.1 | █████████ 0.6958 | ████████ 0.6944 | ███████ 0.6489 | █████ 0.6567 |
| blur=(7, 7), sigma=(0.1, 2.0), p=0.1 | ████████ 0.6917 | ████████ 0.6903 | █████ 0.6433 | ███ 0.6518 |
| blur=(7, 7), sigma=(0.1, 3.0), p=0.1 | ████████ 0.6903 | ███████ 0.6855 | ████████████ 0.6567 | █████████ 0.6657 |
||||||
| blur=(3, 7), sigma=(0.1, 2.0), p=0.1 | ██████████ 0.7000 | ██████████ 0.6969 | ██████████ 0.6611 | ██████████ 0.6700 |
