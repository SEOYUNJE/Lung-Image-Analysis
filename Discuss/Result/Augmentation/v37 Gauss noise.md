## v37 Gaussian Noise

- 미적용한 걸 실험따로 안했지만 일반적으론 (train acc, test acc)가 보통 (67-68%,63-64%) 정도 나옴
- 최적의 세팅: p=0.5, var=(30.0, 50.0)
- Train 과 Test 의 과적합을 예방할 수 있음. 가능하면 적용하는 게 좋음

| GaussNoise Parameters | train_results.accuracy | train_results.f1 | test_results.accuracy | test_results.f1 |
|:----------------------|:----------------------:|:----------------:|:---------------------:|:---------------:|
| p=0.5, var_limit=(10.0, 30.0) | 0.683333333 | 0.681878225 | 0.646666667 | 0.655314051 |
| p=0.5, var_limit=(10.0, 100.0) | 0.694444444 | 0.690989971 | 0.651111111 | 0.66173726 |
| p=0.5, var_limit=(30.0, 50.0) | 0.686111111 | 0.677750774 | 0.66 | 0.66799589 |
| p=0.5, var_limit=(50.0, 80.0) | 0.647222222 | 0.641397428 | 0.64 | 0.645932098 |
| p=0.8, var_limit=(20.0, 60.0) | 0.661111111 | 0.653778582 | 0.644444444 | 0.648738802 |
| p=0.3, var_limit=(80.0, 120.0) | 0.686111111 | 0.680538383 | 0.655555556 | 0.663676527 |


```
GaussNoise Parameters     | Train Accuracy              | Test Accuracy             | Train F1                  | Test F1
--------------------------|-----------------------------|---------------------------|---------------------------|---------------------
p=0.5, var=(10.0, 30.0)   |█████████████████▋   68.33% |███████████▋       64.67% |█████████████████▍ 68.19% |████████████▋   65.53%
p=0.5, var=(10.0, 100.0)  |██████████████████▉  69.44% |████████████▏      65.11% |██████████████████  69.10% |█████████████▎  66.17%
p=0.5, var=(30.0, 50.0)   |█████████████████▋   68.61% |███████████████     66.00% |████████████████▎  67.78% |██████████████▉  66.80%
p=0.5, var=(50.0, 80.0)   |███████████▉         64.72% |██████████▉        64.00% |███████████▏       64.14% |███████████▋    64.59%
p=0.8, var=(20.0, 60.0)   |█████████████▏       66.11% |███████████▍       64.44% |████████████▍      65.38% |████████████    64.87%
p=0.3, var=(80.0, 120.0)  |█████████████████▋   68.61% |████████████▋      65.56% |█████████████████▏ 68.05% |█████████████▍  66.37%
```

## v40
| Probability| var_limit | train_results.accuracy | train_results.f1 | test_results.accuracy | test_results.f1 | GaussNoise Parameters |
|:---------:|:---------:|:----------------------:|:----------------:|:---------------------:|:---------------:|:----------------------|
|0| No Noise | 0.6889 | 0.6859 | 0.6378 | 0.6480 | Resize only |
|0.5| (10,10) | 0.6556 | 0.6453 | 0.6333 | 0.6371 | p=0.5, var_limit=(10, 10) |
|0.5| (30,30) | 0.6736 | 0.6655 | 0.6489 | 0.6524 | p=0.5, var_limit=(30, 30) |
|0.5| (50,50) | 0.6778 | 0.6765 | 0.6511 | 0.6602 | p=0.5, var_limit=(50, 50) |
|0.5| (70,70) | 0.6722 | 0.6704 | 0.6467 | 0.6563 | p=0.5, var_limit=(70, 70) |
|0.5| (100,100) | 0.6681 | 0.6607 | 0.6511 | 0.6533 | p=0.5, var_limit=(100, 100) |
```
var_limit | Train Accuracy              | Test Accuracy               | Train F1                    | Test F1
----------|------------------------------|------------------------------|------------------------------|-----------------------------
No Noise  |████████████████████████ 68.89% |███████████████ 63.78%        |████████████████████████ 68.59% |███████████████████ 64.80%
10(p=0.5) |████████ 65.56%                |█████████████ 63.33%          |████████ 64.53%                |████████████ 63.71%
30(p=0.5) |███████████████ 67.36%         |██████████████████ 64.89%     |██████████████ 66.55%          |█████████████████ 65.24%
50(p=0.5) |██████████████████ 67.78%      |███████████████████ 65.11%    |██████████████████ 67.65%      |████████████████████ 66.02%
70(p=0.5) |█████████████████ 67.22%       |█████████████████ 64.67%      |█████████████████ 67.04%       |███████████████████ 65.63%
100(p=0.5)|████████████████ 66.81%        |███████████████████ 65.11%    |███████████████ 66.07%         |██████████████████ 65.33%
```

### 결론

```
노이즈를 적용하지 않은 경우(No Noise)가 train accuracy와 train F1에서 가장 높은 성능을 보입니다. 하지만 test 성능은 중간 정도입니다.
var_limit이 50일 때 전반적으로 가장 균형 잡힌 성능을 보입니다. 특히 test accuracy와 test F1에서 높은 성능을 보입니다.
var_limit이 10일 때 모든 메트릭에서 가장 낮은 성능을 보입니다. 이는 너무 작은 노이즈가 오히려 모델의 성능을 저하시킬 수 있음을 시사합니다.
var_limit이 증가함에 따라 test 성능이 대체로 향상되는 경향을 보이지만, 100에서는 약간 감소합니다.
대부분의 GaussNoise 설정에서 train과 test 성능의 차이가 No Noise 경우보다 작습니다. 이는 GaussNoise가 과적합을 어느 정도 방지하는 데 도움이 될 수 있음을 나타냅니다.
```

### 배치 적용 예시
- p=0.5, var_limit=(50.0, 80.0)
![image](https://github.com/user-attachments/assets/60c55a82-ab25-4d25-9511-af9abe60330f)

### edge 검출 시 효과적
![image](https://github.com/user-attachments/assets/a03beb6f-0423-41e7-86a4-22f5aa20038f)
