## Model1. Hybrid SeResNet with Vit 

![hybr](https://github.com/user-attachments/assets/cfab5ebe-366a-426c-921a-3073319405f5)

- Backbone: `SeResNet18`, `Vit b16`
- SeResNet18's Input Size: `512X512`
- Vit's Input Size: `224X224` (Learning to resize Mechanism)
- Image Interpolation: `LANCZOS`
- Training for 10 epochs
- split: StratifiedKFold(n=5)
(But for Speeding Up, train only fold1)
- augment: HorizontalFlip(p=0.5)
- Batch: `16`
- LR: `1e-3`
- LabelSmoothing: `0.2`
- Loss: `CategoricalCrossentropy`
- Dropout: None
- Optimizer: `Adam`

## Model2. DOLG(Efficient) - CBAM Model

![dolg](https://github.com/user-attachments/assets/a02f999e-8cfd-41fd-94bd-e13889a7cbe8)


- Backbone: `EfficientnetB0_Ns`
- Input Size: `256X256`
- Image Interpolation: `LANCZOS`
- Training for 10 epochs
- split: StratifiedKFold(n=5)
(But for Speeding Up, train only fold1)
- augment: HorizontalFlip(p=0.5)
- Batch: `16`
- LR: `1e-3`
- LabelSmoothing: `0.2`
- Loss: `CategoricalCrossentropy`
- Dropout: None
- Optimizer: `Adam`

## Model3. Hierarchy Multi Label Classification(HMC)

![hmc1](https://github.com/user-attachments/assets/164a65de-6594-42fb-bf2f-67d715fb088f)

