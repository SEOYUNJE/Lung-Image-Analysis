## PC v5 (24.10.10)


| optimizer_setting                                                        | train_results_avg_f1_score | train_results_avg_auc | test_results_avg_f1_score | test_results_avg_auc | sample_number_setting | epoch_setting | label_smooth_setting | learning_rate_setting | train_batch_setting | valid_batch_setting | test_batch_setting | fold_num_setting | clahe_setting | base_model |  |
|--------------------------------------------------------------------------|----------------------------|-----------------------|---------------------------|----------------------|-----------------------|---------------|----------------------|-----------------------|---------------------|---------------------|--------------------|------------------|---------------|------------|--|
| optimizers.Adadelta(learning_rate=learning_rate_setting, rho=0.95)       |         0.0762463807782193 |    0.7061301183898986 |       0.08188296306626067 |   0.7012937568907734 |                   500 |            10 |                 0.15 |                0.0003 |                  16 |                  32 |                 64 |                1 | [2.0, (4, 4)] | resnet18   |  |
| optimizers.Adagrad(learning_rate=learning_rate_setting)                  |         0.4316500634625954 |    0.8442836025375243 |       0.39228587223424966 |   0.8227320383147004 |                   500 |            10 |                 0.15 |                0.0003 |                  16 |                  32 |                 64 |                1 | [2.0, (4, 4)] | resnet18   |  |
| optimizers.Adam(learning_rate=learning_rate_setting)                     |          0.437311897248032 |    0.8383502524173391 |        0.4234829637664392 |    0.841862907718958 |                   500 |            10 |                 0.15 |                0.0003 |                  16 |                  32 |                 64 |                1 | [2.0, (4, 4)] | resnet18   |  |
| optimizers.Adamax(learning_rate=learning_rate_setting)                   |        0.02024566219688171 |    0.5727142159655805 |      0.020144557535444453 |   0.5668585073873267 |                   500 |            10 |                 0.15 |                0.0003 |                  16 |                  32 |                 64 |                1 | [2.0, (4, 4)] | resnet18   |  |
| optimizers.AdamW(learning_rate=learning_rate_setting, weight_decay=0.01) |        0.13124056064854758 |   0.45747833018238976 |       0.13093961460193917 |   0.4617022615750094 |                   500 |            10 |                 0.15 |                0.0003 |                  16 |                  32 |                 64 |                1 | [2.0, (4, 4)] | resnet18   |  |
| optimizers.Ftrl(learning_rate=learning_rate_setting)                     |        0.40136027327999957 |    0.8223614117778311 |       0.35552361243570224 |   0.7971281393916831 |                   500 |            10 |                 0.15 |                0.0003 |                  16 |                  32 |                 64 |                1 | [2.0, (4, 4)] | resnet18   |  |
| optimizers.Nadam(learning_rate=learning_rate_setting)                    |         0.4676276185034326 |     0.846005186669621 |       0.45283893421191557 |   0.8285264471164409 |                   500 |            10 |                 0.15 |                0.0003 |                  16 |                  32 |                 64 |                1 | [2.0, (4, 4)] | resnet18   |  |
| optimizers.RMSprop(learning_rate=learning_rate_setting, rho=0.9)         |        0.18054453049852986 |                   0.5 |       0.18030570351009131 |                  0.5 |                   500 |            10 |                 0.15 |                0.0003 |                  16 |                  32 |                 64 |                1 | [2.0, (4, 4)] | resnet18   |  |
| optimizers.SGD(learning_rate=learning_rate_setting, momentum=0.9)        |         0.4027772552077421 |    0.8422722902694948 |        0.3964201152204996 |   0.8346099659333757 |                   500 |            10 |                 0.15 |                0.0003 |                  16 |                  32 |                 64 |                1 | [2.0, (4, 4)] | resnet18   |  |


```
for opt_set in optimizer_settings:
    configurations.append(
        {
            'sample_number_setting':sample_num_setting,
            'epoch_setting': 10,
            'label_smooth_setting': 0.15,
            'learning_rate_setting': 3e-4,
            'train_batch_setting': 16,
            'valid_batch_setting': 32,
            'test_batch_setting': 64,
            'fold_num_setting': 1,
            'clahe_setting': [2.0, (4, 4)],
            'train_augs': [A.Resize(256, 256, always_apply=True)],
            'train_batch_augmentation_params': {},
            'valid_augs': [A.Resize(256, 256, always_apply=True)],
            'valid_batch_augmentation_params': {},
            'base_model': 'resnet18',
            'optimizer_setting': opt_set,
        }
    )
```
** No augmentation applied
