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

3. `Cross Validation`
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

4. `Loss`

     - **tf.keras.losses.CategoricalCrossentropy(label_smoothing=None)**
     - **tf.keras.losses.CategoricalFocalCrossentropy(alpha=None, gamma=None, label_smoothing=None)**
     => alpha: 데이터의 불균형을 해소하고자 모든 라벨 종류에 동일한 가중치를 곱한다(즉, rapid에서s alpha=1로 설정하면 됨)
     => gamma: 쉬운 샘플에 대한 손실 값은 줄이는 변수로 값이 커질수록 어려운 샘플에 초점을 더 둔다(기본값: 2.0)
     - **tf.keras.losses.KLDivergence()**
     => categorial loss들은 실제 값과 예측값의 오차 범위를 측정하는 거라면 kldivergence는 해당 라벨의 확률 값 자체가 아닌
       모든 라벨에 대한 확률 분포를 계산한다.
     => 다만 (1,0,0) 이처럼 1,0으로만 되어 있으면 kldivergene 수식에 의하여 loss값이 너무 커지기 때문에 label smoothing을 진행해야 한다. 이때 따로 kldivergence에는 label_smooting이 없고 One Hot Encoding Part에서 수정해야 한다.
  
     - **F1 Loss(Custom Loss, tf.keras.losses에서 지원하지 않는 함수)**
       
