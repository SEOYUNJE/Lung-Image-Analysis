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
3. `Custom Augmentation`:

   **Needle Augmentation**
   kaggle 주소: https://www.kaggle.com/code/seoyunje/needle-augmentation/input

   => od.download('https://www.kaggle.com/code/seoyunje/needle-augmentation/input')

   **Numerous CutMix**
   => num_patches=1이면 cutmix 한번 적용된 걸로 기본 cutmix랑 동일
   => 단, num_patches의 값을 1이 아닌 2~4로 하게 될 경우 여러 개의 cutmix가 적용됨
   
        def __augment2(self, img_batch, mask_batch, cutmix_prob=0.5, num_patches=4):
             batch_size, height, width, channels = img_batch.shape

             for i in range(batch_size):
                  if np.random.rand() <= cutmix_prob:  
                  for _ in range(num_patches):  # 여러 개의 패치를 적용하기 위해 반복문 추가
                       idx = np.random.randint(batch_size)
                       lam = np.random.beta(0.5, 0.5)
                
                       cut_width = min(int(width * lam), 50)
                       cut_height = min(int(height * lam), 50)
                       cut_x = np.random.randint(0, width - cut_width + 1)
                       cut_y = np.random.randint(0, height - cut_height + 1)

                       img_batch[i, cut_y:cut_y + cut_height, cut_x:cut_x + cut_width, :] = img_batch[idx, cut_y:cut_y + cut_height, cut_x:cut_x + cut_width, :]
                       mask_batch[i, cut_y:cut_y + cut_height, cut_x:cut_x + cut_width, :] = mask_batch[idx, cut_y:cut_y + cut_height, cut_x:cut_x + cut_width, :]

            return img_batch, mask_batch

5. `Cross Validation`
     - 현재 cross validation: SKF
       
        skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
        for i, (_, valid_index) in enumerate(skf.split(df_train, df_train['Finding Labels'])):
           df_train.loc[valid_index, 'Fold'] = i

      - GroupKFold
        
         gkf = GroupKFold(n_splits=5)
         for i, (_, valid_index) in enumerate(gkf.split(df_train, df_train['Finding Labels'], groups=df_train['Patient ID'])):
            df_train.loc[valid_index, 'Fold'] = i

      - StratifiedGroupKFold
   
          from sklearn.model_selection import StratifiedGroupKFold    

          sgkf = StratifiedGroupKFold(n_splits=5, shuffle=True, random_state=42)
          for i, (_, valid_index) in enumerate(sgkf.split(df_train, df_train['Finding Labels'], groups=df_train['Patient ID'])):
             df_train.loc[valid_index, 'Fold'] = i

6. `Best Loss Function for Macro F1-Score Metric`

     - **tf.keras.losses.CategoricalCrossentropy(label_smoothing=None)**
     - **tf.keras.losses.CategoricalFocalCrossentropy(alpha=None, gamma=None, label_smoothing=None)**
     => alpha: 데이터의 불균형을 해소하고자 모든 라벨 종류에 동일한 가중치를 곱한다(즉, rapid에서s alpha=1로 설정하면 됨)
     => gamma: 쉬운 샘플에 대한 손실 값은 줄이는 변수로 값이 커질수록 어려운 샘플에 초점을 더 둔다(기본값: 2.0)
     - **tf.keras.losses.KLDivergence()**
     => categorial loss들은 실제 값과 예측값의 오차 범위를 측정하는 거라면 kldivergence는 해당 라벨의 확률 값 자체가 아닌
       모든 라벨에 대한 확률 분포를 계산한다.
     => 다만 (1,0,0) 이처럼 1,0으로만 되어 있으면 kldivergene 수식에 의하여 loss값이 너무 커지기 때문에 label smoothing을 진행해야 한다. 이때 따로 kldivergence에는 label_smooting이 없고 One Hot Encoding Part에서 수정해야 한다.
  
     - **F1 Loss(Custom Loss, tf.keras.losses에서 지원하지 않는 함수)**
  
   <Correlation with Macro F1 Score Metric & Loss Function>
   
        cce = tf.keras.losses.categorical_crossentropy(all_true, all_oof)
        macro_f1 = f1(all_true, all_oof)

        plt.figure(figsize=(12,6))

        plt.scatter(cce,macro_f1)
        plt.xlabel('CCE Loss')
        plt.ylabel('Macro F1-Score')
        plt.show()
   ![](https://www.kaggleusercontent.com/kf/6633544/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..D5KoCQhi8-w3e_8BTQkUkA.chRhxjql1202i3rAizObtWKRothpvDJbBSzZdeTJy2bcB_qIYo-AZUdMWbCSp_CFVKWiaoSJU47kEopsPbpkaE4vFUKNPrhB8CGL8KKgtybgHdLGm_C68zW27fP-Qx2Mq7fiBisLax-Ka-a94O4QrHMwJGG0XdOZ31SoM9jIaDKk5jAseidHYfgKy2pUnzNMQGpLNb8UHTFDVEhq5k4SYCt7FikN-xMp6q1OrJFaKvyWyEpDRu5r_ydtIY3aoi1JNOkHFdJgfNGJGpHWaOxQrG0Dw1FI9vyczMAv5WEi-77en1L3JpNHD6o1nWRnr6mzuoeLiVsaV4HqRtbgmjelS9g0JlYowi9o7ri4TyIoFxTQB09_dQDvg78WIZNcvCNApZ5PKbVp1x_zcOXAv2Bi07VLnLcVOvSttWSqqoPw1kcdRNr5HuQrVFa3-mFL8m_KTJIrjGZJWRsMlLOMZeMJU45oPmtLiHuu18C1yB3oLOZSgwtwekjOTe3Zf1n1kYoNCT-HrgcCIDVNKeLpRUo9V5MpVBmEfBPmA8vrTpf7Wuy4cEWcg2l-23jAMGmiU2wRP6oY_fnlVCVbRzcQABlncbk7U8Gf-ahY1vg8bUoeRSIRfteCMyNoOZwYrSM6UOjR3qpww7rhiCxuQXswcbSe3W0wzDs4fsYiVL6GbjEzi80.nSZgn_ylEhxCKkxH3GZCAQ/__results___files/__results___14_0.png)
       
