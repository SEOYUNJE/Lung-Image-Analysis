## Model1. DOLG(Efficient) - CBAM Model

![dolg](https://github.com/user-attachments/assets/a02f999e-8cfd-41fd-94bd-e13889a7cbe8)

## Model2. Hybrid CNN 

![image](https://github.com/user-attachments/assets/2cd6ec7a-b4ae-4401-be2f-98752c154692)

📌 **Experimental Parameters**
    
- `Image Size`: 256X256
    
- `Label Unique`: Label Unique>=2 & No Finding 삭제 
    
- `CLAHE(Contrast Limited Adaptive Histogram Equalization)`: clipLimit: 2.0, tileGridSize: (8,8) 

- `Label Smoothing`: 0.05
    
- `Loss`: BinaryCrossentropy
    
- `Fold`: SKF(n_splits=5) But, Only Traininig Fold1
    
- `Weak Augment`: HFlip, Rotate(limit=5)
    
- `Strong Augment`: CutMix(patch=2), Cutmix size maximum: 256//5
  
- `BackBone Model`: TF EfficientNetB0 Noisy Student
    
- `Freezing Layer`: None
    
- `Batch Size`: 32
    
- `Learning Rate`: 1e-3
    
- `Epoch`: 10
    
- `Optimizer`: Adam

## Model3. Hierarchy Multi Label Classification(HMC)
![image](https://github.com/user-attachments/assets/fb132fad-5885-4bbd-9428-5019ce5b7424)
