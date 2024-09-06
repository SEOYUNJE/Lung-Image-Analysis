## Version 35 RandomBrightnessContrast
- 최적의 세팅: A.RandomBrightnessContrast(brightness_limit=0.1, contrast_limit=0.2, p=0.5)

#### 실험결과
| Brightness Limit | Contrast Limit | 확률 | 훈련 정확도 | 훈련 F1 점수 | TEST 정확도 |
|------------------|----------------|------|------------|-------------|--------------|
|  (0.0,0.0)  |  (0.0,0.0)  | 0.0 | 0.6750 | 0.6668 | 0.6389 |
|||||||
| (-0.1, 0.1) | (0, 0) | 0.5 | **0.6931** | **0.6876** | **0.6578** |
| (-0.2, 0.2) | (0, 0) | 0.5 | 0.6764 | 0.6733 | **0.6611** |
| (-0.3, 0.3) | (0, 0) | 0.5 | 0.6667 | 0.6593 | 0.6378 |
|||||||
| (0, 0) | (-0.1, 0.1) | 0.5 | 0.6861 | 0.6784 | 0.6311 |
| (0, 0) | (-0.2, 0.2) | 0.5 | 0.6833 | 0.6808 | 0.6478 |
| (0, 0) | (-0.3, 0.3) | 0.5 | 0.6528 | 0.6451 | 0.6500 |
|||||||
| (-0.1, 0.1) | (-0.1, 0.1) | 0.5 | 0.6806 | 0.6764 | **0.6533** |
| (-0.1, 0.1) | (-0.2, 0.2) | 0.5 | **0.7097** | **0.7048** | **0.6533** |
| (-0.1, 0.1) | (-0.3, 0.3) | 0.5 | 0.6833 | 0.6767 | **0.6533** |
|||||||
| (-0.2, 0.2) | (-0.1, 0.1) | 0.5 | 0.6917 | 0.6869 | **0.6644** |
| (-0.2, 0.2) | (-0.2, 0.2) | 0.5 | 0.6708 | 0.6672 | **0.6633** |
| (-0.2, 0.2) | (-0.3, 0.3) | 0.5 | 0.6889 | 0.6870 | **0.6656** |
|||||||
| (-0.3, 0.3) | (-0.1, 0.1) | 0.5 | 0.6764 | 0.6744 | **0.6678** |
| (-0.3, 0.3) | (-0.2, 0.2) | 0.5 | 0.6681 | 0.6606 | 0.6344 |
| (-0.3, 0.3) | (-0.3, 0.3) | 0.5 | 0.6667 | 0.6619 | 0.6389 |



#### 성능 메트릭 비교 (0.63 - 0.71 범위)
```
---------------------------------------------------------------------------------------------
설정 (Brightness, Contrast)     |       훈련 정확도       |       훈련 F1 점수      |       TEST 정확도       |
---------------------------------------------------------------------------------------------
(   NONE  ) (   NONE  ) 0.0     | ██████████████          | ███████████             | ███████                |

(-0.1, 0.1) (0, 0)      0.5     | ███████████████████     | ██████████████████      | ████████████████       |
(-0.2, 0.2) (0, 0)      0.5     | ███████████████         | ██████████████          | ████████████████       |
(-0.3, 0.3) (0, 0)      0.5     | ███████████             | █████████               | ███████                |

(0, 0)     (-0.1, 0.1)  0.5     | ██████████████████      | ███████████████         | █                      |
(0, 0)     (-0.2, 0.2)  0.5     | █████████████████       | ████████████████        | ██████████             |
(0, 0)     (-0.3, 0.3)  0.5     | █                       | █                       | ███████████            |

(-0.1, 0.1) (-0.1, 0.1) 0.5     | █████████████████       | ██████████████          | ████████████           |
(-0.1, 0.1) (-0.2, 0.2) 0.5     | ████████████████████████| ████████████████████████| ████████████           |
(-0.1, 0.1) (-0.3, 0.3) 0.5     | █████████████████       | ███████████████         | ████████████           |

(-0.2, 0.2) (-0.1, 0.1) 0.5     | ██████████████████      | ████████████████        | ██████████████████     |
(-0.2, 0.2) (-0.2, 0.2) 0.5     | ██████████████          | ███████████             | ██████████████████     |
(-0.2, 0.2) (-0.3, 0.3) 0.5     | ██████████████████      | ████████████████        | ███████████████████    |

(-0.3, 0.3) (-0.1, 0.1) 0.5     | ███████████████         | ██████████████          | ███████████████████    |
(-0.3, 0.3) (-0.2, 0.2) 0.5     | ███████████             | █████████               | ██                     |
(-0.3, 0.3) (-0.3, 0.3) 0.5     | ███████████             | ██████████              | ███████                |
---------------------------------------------------------------------------------------------
                                  0.63                    0.65                    0.67                    0.69                    0.71
```

#### train 배치 예시
- (-0.1, 0.1) (-0.2, 0.2) 0.5
![image](https://github.com/user-attachments/assets/b4a92361-4f6d-4d72-a772-3afd53c0d8b9)
- (-0.3, 0.3) (-0.3, 0.3) 0.5
![image](https://github.com/user-attachments/assets/a36c45ab-8d3c-48b3-871e-f15b7e4bce0a)



#### 코드
```python
class AugmentationPipeline:
    def __init__(self, albumentation_augs=None):
        self.albumentation_augs = A.Compose(albumentation_augs) if albumentation_augs else None

    def apply(self, images):
        if self.albumentation_augs:
            if len(images.shape) == 4:  # 배치 처리
                return np.array([self.albumentation_augs(image=img)['image'] for img in images])
            elif len(images.shape) == 3:  # 단일 이미지 처리
                return self.albumentation_augs(image=images)['image']
            else:
                raise ValueError("Unexpected input shape. Expected 3D or 4D array.")
        return images

class BatchAugmentation:
    def __init__(self, augmentation_params):
    def apply(self, X, y):
    def _apply_mixup(self, X, y):
    def _apply_cutmix(self, X, y):
    def _apply_edge_mixup(self, X, y):

class DataGenerator(tf.keras.utils.Sequence):
    def __init__(self, data, batch_size=16, shuffle=False, preprocess=None, augmentation_pipeline=None, batch_augmentation=None):
        self.data = data
        self.batch_size = batch_size
        self.shuffle = shuffle
        self.preprocess = preprocess
        self.augmentation_pipeline = augmentation_pipeline
        self.batch_augmentation = batch_augmentation
        self.on_epoch_end()
        self.clahe = cv2.createCLAHE(clipLimit=clahe_setting[0], tileGridSize=clahe_setting[1])

    def __len__(self):
        return int(np.ceil(len(self.data) / self.batch_size))

    def __getitem__(self, index):
        indexes = self.indexes[index*self.batch_size:(index+1)*self.batch_size]
        X, y = self.__data_generation(indexes)
        if self.preprocess:X = self.preprocess(X)
        if self.augmentation_pipeline:
            X_uint8 = X.clip(0, 255).astype(np.uint8)
            X_augmented = self.augmentation_pipeline.apply(X_uint8)
            X = X_augmented.astype(np.float32)
        
        if self.batch_augmentation:X, y = self.batch_augmentation.apply(X, y)
        return X, y

    def on_epoch_end(self):
    def __data_generation(self, indexes):
```

```
# 적용 예시
'train_augs': [
    A.GaussNoise(var_limit=(10.0, 100.0), mean=0, p=0.5),
    A.Resize(256, 256, always_apply=True)
],
'train_batch_augmentation_params': {
    'edge_mixup': [0.0, 0.2, 40]  # Probability, alpha, edge width
},
'valid_augs': [A.Resize(256, 256, always_apply=True)],
'valid_batch_augmentation_params': {}


train_aug_pipeline = AugmentationPipeline(albumentation_augs=train_augs)
train_batch_aug = BatchAugmentation(train_batch_augmentation_params)

valid_aug_pipeline = AugmentationPipeline(albumentation_augs=valid_augs)
valid_batch_aug = BatchAugmentation(valid_batch_augmentation_params)

train_gen = DataGenerator(df_train,
                          batch_size=train_batch_setting, shuffle=True,
                          augmentation_pipeline=train_aug_pipeline,
                          batch_augmentation=train_batch_aug,
                          preprocess=preprocess_input)
```
