## Model1. Hybrid SeResNet with Vit 

![hybrid seresnet](https://github.com/user-attachments/assets/f6bf0c1b-2651-4107-96fc-878d0aec0ce5)

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

## Model2. EfficientNet - CBAM Model

- Backbone: `EfficientnetB0_Ns`
- SeResNet18's Input Size: `256X256`
- Image Interpolation: `LANCZOS`
- Training for 10 epochs
- split: GroupKFold(n=5)
(But for Speeding Up, train only fold1)
- augment: HorizontalFlip(p=0.5)
- Batch: `16`
- LR: `1e-3`
- LabelSmoothing: `0.2`
- Loss: `CategoricalCrossentropy`
- Dropout: None
- Optimizer: `Adam`
