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
- GradCAM


## 2. Learning Rate
![image](https://github.com/user-attachments/assets/01b06145-0b07-447e-97f4-b6dc3d6ecd6d)
- Best results at Learning Rate Setting of 3e-4
- Metric
![image](https://github.com/user-attachments/assets/f3074b1f-d723-4ff1-9a50-0be98fe9a730)
- Train
![image](https://github.com/user-attachments/assets/8d6b848e-b86b-4d77-81bc-d3a7512e0695)  
- Test
![image](https://github.com/user-attachments/assets/70907634-d232-4989-8d0e-103c66990563)
- GradCAM
![image](https://github.com/user-attachments/assets/133fb62f-7916-4d3a-9461-8f1e44043e88)


## 3. CLAHE
![image](https://github.com/user-attachments/assets/3cdbd0ea-2c60-480d-b1e7-f3ce69629e28)
- No distinct difference according to setting
- [2.0, (4,4)]
