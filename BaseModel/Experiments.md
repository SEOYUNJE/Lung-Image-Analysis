1. `Image Size`

   - 224 X 224
   - 256 X 256
   - 386 X 386
   - 512 X 512
   - 786 X 786
   - 1024 X 1024
  
     ![imgsi](https://github.com/user-attachments/assets/935a9d6f-66a6-41e4-9787-a19c67e02dbd)

2. `Label Smoothing`
   
    loss = losses.CategoricalCrossentropy(`label_smoothing`=0.2)
    
    - 현재 값: 0.2
      => 0.8, 0.2/8, 0.2/8, 0.2/8, 0.2/8, 0.2/8, 0.2/8, 0.2/8, 0.2/8

     - 0.01
     - 0.05
     - 0.1
     - 0.2

3. 'Cross Validation`
     - 현재 cross validation: SKF
       
        skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
        for i, (_, valid_index) in enumerate(skf.split(df_train, df_train['Finding Labels'])):
           df_train.loc[valid_index, 'Fold'] = i

      - GroupKFold
        
         gkf = GroupKFold(n_splits=5)
         for i, (_, valid_index) in enumerate(gkf.split(df_train, df_train['Finding Labels'], groups=df_train['Patient ID'])):
            df_train.loc[valid_index, 'Fold'] = i

      - StratifiedKFold
   
          from sklearn.model_selection import StratifiedGroupKFold    

          sgkf = StratifiedGroupKFold(n_splits=5, shuffle=True, random_state=42)
          for i, (_, valid_index) in enumerate(sgkf.split(df_train, df_train['Finding Labels'], groups=df_train['Patient ID'])):
             df_train.loc[valid_index, 'Fold'] = i

   
