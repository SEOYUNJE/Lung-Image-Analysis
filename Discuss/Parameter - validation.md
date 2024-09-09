### 전부 다 5 fold로 진행
```python
# Group K-fold (Patient ID)
gkf = GroupKFold(n_splits=5)
for i, (_, valid_index) in enumerate(gkf.split(df_train, df_train['Finding Labels'], groups=df_train['Patient ID'])):
    df_train.loc[valid_index, 'Fold'] = i

# Stratified K-fold
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
for i, (_, valid_index) in enumerate(skf.split(df_train, df_train['Finding Labels'])):
    df_train.loc[valid_index, 'Fold'] = i

#  K-fold
kf = KFold(n_splits=5, shuffle=True, random_state=42)
for i, (_, valid_index) in enumerate(kf.split(df_train)):
    df_train.loc[valid_index, 'Fold'] = i

```

| Experiment | Train Accuracy | Train F1 | Test Accuracy | Test F1 |
|------------|----------------|----------|---------------|---------|
| GKF(Patient ID) | 0.6238 | 0.6340 | ████ 0.6644 | ██ 0.6582 |
| SKF | ███████ 0.6346 | ████████ 0.6440 | ██ 0.6621 | 0.6570 |
| Kfold | ██ 0.6281 | ████ 0.6391 | █ 0.6610 | 0.6570 |

| Experiment | Train Accuracy | Train F1 | Test Accuracy | Test F1 |
|------------|----------------|----------|---------------|---------|
| GSKF(Patient ID) | 0.6238 | 0.6340 | 0.6644 | 0.6582 |
| SKF | 0.634604439 | 0.644030179 | 0.662116041 | 0.656995729 |
| Kfold | 0.628059192 | 0.639052748 | 0.660978385 | 0.656961528 |
