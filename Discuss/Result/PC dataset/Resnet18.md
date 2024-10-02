# PC dataset v4

## Label Smooth
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
## Learning Rate

## CLAHE
