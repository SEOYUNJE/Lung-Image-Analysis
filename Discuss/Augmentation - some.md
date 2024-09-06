#### v33
| Index | train_results.accuracy | train_results.f1 | test_results.accuracy | test_results.f1 | Augmentation | Parameters |
|:-----:|:----------------------:|:----------------:|:---------------------:|:---------------:|:-------------|:-----------|
| 0 | 0.6819 | 0.6739 | 0.6378 | 0.6415 | Resize | p=1.0, height=256, width=256, interpolation=1 |
| 1 | 0.6569 | 0.6510 | 0.6289 | 0.6369 | RandomBrightnessContrast | p=0.7, brightness_limit=(-0.2, 0.2), contrast_limit=(-0.2, 0.2), brightness_by_max=True |
| 2 | 0.6792 | 0.6732 | 0.6544 | 0.6598 | GaussNoise | p=0.5, var_limit=(10.0, 50.0), per_channel=True, mean=0.0, noise_scale_factor=1.0 |
| 3 | 0.6708 | 0.6690 | 0.6378 | 0.6498 | RandomGamma | p=0.6, gamma_limit=(80, 120) |
| 4 | 0.6542 | 0.6470 | 0.6500 | 0.6569 | GaussianBlur | p=0.4, blur_limit=(3, 7), sigma_limit=(0, 0) |
| 5 | 0.6847 | 0.6790 | 0.6256 | 0.6367 | ShiftScaleRotate | p=0.7, shift_limit=(-0.0625, 0.0625), scale_limit=(-0.1, 0.1), rotate_limit=(-15, 15) |
| 6 | 0.6792 | 0.6759 | 0.6567 | 0.6673 | GridDistortion | p=0.5, num_steps=5, distort_limit=(-0.1, 0.1) |
| 7 | 0.6972 | 0.6906 | 0.6356 | 0.6444 | ElasticTransform | p=0.6, alpha=1.0, sigma=50.0 |
| 8 | 0.6625 | 0.6585 | 0.6556 | 0.6599 | RandomShadow | p=0.5, shadow_roi=(0.0, 0.5, 1.0, 1.0), num_shadows_limit=(1, 2), shadow_dimension=5 |
| 9 | 0.6736 | 0.6689 | 0.6289 | 0.6382 | OneOf + ShiftScaleRotate + GaussianBlur | OneOf(p=0.7), ShiftScaleRotate(p=0.5), GaussianBlur(p=0.3) |

Note: All augmentations include Resize(p=1.0, height=256, width=256, interpolation=1). Learning rate is set to 0.0010 for all experiments.

```
Index | Augmentation (Key Params)   | Train Accuracy        | Test Accuracy         | Train F1              | Test F1
------|----------------------------|------------------------|------------------------|------------------------|----------------------
0     | Resize                     |███████████████████████ 68.19% |█████████ 63.78%         |██████████████████████ 67.39% |██████████ 64.15%
1     | RandomBrightnessContrast   |███████████████ 65.69%        |████████ 62.89%          |███████████████ 65.10%        |█████████ 63.69%
      | (p=0.7, limit=±0.2)        |                              |                          |                              |
2     | GaussNoise                 |█████████████████████ 67.92%   |████████████ 65.44%      |█████████████████████ 67.32%  |████████████ 65.98%
      | (p=0.5, var=10-50)         |                              |                          |                              |
3     | RandomGamma                |████████████████████ 67.08%    |█████████ 63.78%         |████████████████████ 66.90%   |███████████ 64.98%
      | (p=0.6, gamma=80-120)      |                              |                          |                              |
4     | GaussianBlur               |██████████████████ 65.42%      |███████████ 65.00%       |██████████████ 64.70%         |███████████ 65.69%
      | (p=0.4, blur=3-7)          |                              |                          |                              |
5     | ShiftScaleRotate           |███████████████████████ 68.47% |███████ 62.56%           |██████████████████████ 67.90% |█████████ 63.67%
      | (p=0.7, rotate=±15°)       |                              |                          |                              |
6     | GridDistortion             |█████████████████████ 67.92%   |████████████ 65.67%      |█████████████████████ 67.59%  |█████████████ 66.73%
      | (p=0.5, limit=±0.1)        |                              |                          |                              |
7     | ElasticTransform           |████████████████████████ 69.72%|████████ 63.56%          |███████████████████████ 69.06%|██████████ 64.44%
      | (p=0.6, sigma=50)          |                              |                          |                              |
8     | RandomShadow               |███████████████████ 66.25%     |████████████ 65.56%      |███████████████ 65.85%        |███████████ 65.99%
      | (p=0.5, num=1-2)           |                              |                          |                              |
9     | OneOf + ShiftScaleRotate   |████████████████████ 67.36%    |████████ 62.89%          |████████████████████ 66.89%   |█████████ 63.82%
      | + GaussianBlur             |                              |                          |                              |

Legend: Each █ represents approximately 0.5%
Base value for all bars: 60.00%
Maximum value: 75.00%
```


- ElasticTransform(인덱스 7, p=0.6, sigma=50)이 train accuracy와 train F1에서 가장 높은 성능을 보이지만, test 성능은 상대적으로 낮습니다. 이는 과적합의 징후일 수 있습니다.
- GridDistortion(인덱스 6, p=0.5, limit=±0.1)이 test accuracy와 test F1에서 가장 높은 성능을 보입니다. 또한 train과 test 성능 간의 차이가 작아 좋은 균형을 보입니다.
- GaussNoise(인덱스 2, p=0.5, var=10-50)도 전반적으로 좋은 성능을 보이며, train과 test 성능 간의 균형이 좋습니다.
- ShiftScaleRotate(인덱스 5, p=0.7, rotate=±15°)는 높은 train 성능에 비해 낮은 test 성능을 보입니다. 이 역시 과적합의 징후일 수 있습니다.
- 복합적인 증강 기법(인덱스 9)은 예상보다 좋은 성능을 보이지 않습니다. 이는 너무 많은 증강이 오히려 모델의 학습을 방해할 수 있음을 시사합니다.
- 단순한 Resize만 적용한 경우(인덱스 0)도 상대적으로 좋은 성능을 보입니다. 이는 기본 모델이 이미 어느 정도 강건함을 나타냅니다.
