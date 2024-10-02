# PC dataset v4

## 1. Label Smooth
![image](https://github.com/user-attachments/assets/4740eb52-5598-49f0-9902-0285e4d73008)
- Best results at Label Smooth Setting of 0.15
---
- sample_number_setting: 500
- epoch_setting: 10
- label_smooth_setting: ######
- learning_rate_setting: 0.0001
- train_batch_setting: 16
- valid_batch_setting: 32
- test_batch_setting: 64
- fold_num_setting: 1
- clahe_setting: [2.0, (4, 4)]
- train_augs: None
- train_batch_augmentation_params: {}
- valid_augs: None
- valid_batch_augmentation_params: {}
- base_model: resnet18
- optimizer_setting: optimizers.Adam(learning_rate=learning_rate_setting)
---
- Metric
![image](https://github.com/user-attachments/assets/5d35c753-72d7-49fb-a187-4c28920b2c9f)
- Train
![image](https://github.com/user-attachments/assets/48243f5d-2f13-4f72-a0e2-572b3213a5ba)
- Test
![image](https://github.com/user-attachments/assets/56da8d3d-6306-4bde-af9c-1f911a44159f)

## 2. Learning Rate

## 3. CLAHE
