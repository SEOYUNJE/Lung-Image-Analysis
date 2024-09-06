- sample_num_setting: 500
- epoch_setting: 15 / 10
- label_smoothing_setting: 0.15
- train_batch_setting: 16
- valid_batch_setting: 32
- test_batch_setting: 64
- fold_num_setting: 1(in 5folds)
- LABEL = [['Edema','No Finding', 'Pneumonia', 'Tuberculosis', 'Pneumothorax', 'Emphysema', 'Covid', 'Effusion', 'Atelectasis']

- Preprocess: (CLAHE: None)

- augment: Hflip(p=0.5)
  

<img src="https://github.com/user-attachments/assets/f3965729-22b9-4875-830e-531d715175ad" style="width: 80%; border: 2px solid #999; border-radius: 4px; padding: 4px;" />

<img src="https://github.com/user-attachments/assets/6da3d22b-6d27-42ca-b644-c84efdfd706d" style="width: 80%; border: 2px solid #999; border-radius: 4px; padding: 4px;" />

<img src="https://github.com/user-attachments/assets/63b0413f-55a8-4fbe-bf7c-8e6b3b51ffd4" style="width: 49%; display: inline-block; border: 2px solid #999; border-radius: 4px; padding: 4px;" /><img src="https://github.com/user-attachments/assets/10f56fc0-d669-41c7-8b80-c5a387cb119d" style="width: 49%; display: inline-block; border: 2px solid #999; border-radius: 4px; padding: 4px;" />




### v19
- Best Setting: 3e-4 or 1e-3

| Learning Rate | train_results.accuracy | train_results.f1 | test_results.accuracy | test_results.f1 |
|:-------------:|:----------------------:|:----------------:|:---------------------:|:---------------:|
| 3e-3 | 0.5347 | 0.5161 | 0.5156 | 0.4931 |
| 1e-3 | 0.6833 | 0.6807 | 0.6500 | 0.6594 |
| 3e-4 | 0.6861 | 0.6863 | 0.6500 | 0.6607 |
| 1e-4 | 0.6181 | 0.6128 | 0.6033 | 0.6072 |
| 3e-5 | 0.6069 | 0.6002 | 0.5789 | 0.5805 |
| 1e-5 | 0.5486 | 0.5379 | 0.5278 | 0.5259 |

```
Learning Rate | Train Accuracy        | Test Accuracy         | Train F1              | Test F1
--------------|------------------------|------------------------|------------------------|----------------------
3e-3          |████                53.47%|███▋               51.56%|███▊               51.61%|███▋               49.31%
1e-3          |████████████████▋   68.33%|███████████████    65.00%|████████████████▌   68.07%|███████████████▎   65.94%
3e-4          |████████████████▋   68.61%|███████████████    65.00%|████████████████▋   68.63%|███████████████▎   66.07%
1e-4          |████████████▊       61.81%|██████████████▏    60.33%|████████████▊       61.28%|████████████▌     60.72%
3e-5          |████████████▍       60.69%|███████████▍       57.89%|████████████▏       60.02%|███████████▌      58.05%
1e-5          |████▊               54.86%|████▎               52.78%|████▌               53.79%|████▎              52.59%

Legend: Each █ represents approximately 1%
Base value for all bars: 49.00%
Maximum value: 69.00%
```
