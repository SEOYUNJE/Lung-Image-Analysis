## Image Augmentation

![](https://albumentations.ai/docs/images/getting_started/augmenting_images/augmentation_pipeline_visualized.jpg)


### Weak Augmentation

**Flip**
- `HorizontalFlip`: albumentations.HorizontalFlip(p=None)
- `VerticalFlip`: albumentations.VerticalFlip(p=None)

**Rotate**
- `Rotate`: albumentations.Rotate(limit=None, p=None)

**Shear**
- `Shear`: albumentations.Affine(shear=None, p=None)
- `Shift`: albumentations.ShiftScaleRotate(shift_limit=None, scale_limit=None, rotate_limit=None, p=None),

**Cropped**
- `Crop`: albumentations.RandomResizedCrop(height=None, width=None, scale=(None, None), ratio=(None, None))

**Dropout**
- `CoarseDropout`: albumentations.CoarseDropout(max_holes=None, max_height=None, max_width=None, min_holes=None, 
                  min_height=None, min_width=None, fill_value=None, p=None)
- `XYMasking`:
  
  => params = {
           'num_masks_x': None,
           'num_masks_y': None,
           'mask_x_length': None,
           'mask_y_length': None,
           'fill_value': None, 
  }
  
  => albumentations.XYMasking(**params, p=None)
- `Channel Dropout`: albumentations.ChannelDropout(channel_drop_range=(1, 1), p=None)


### Strong Augmentation

`Mixup`:

    def __augment2(self, img_batch, mixup_prob=0.1):
        batch_size, height, width, channels = img_batch.shape

        idx = np.random.permutation(batch_size)
        lam = np.random.beta(2.0, 2.0) 
        
        for i in range(batch_size):
            if np.random.rand() <= mixup_prob:  
                j = idx[i]
            
                img_batch[i] = img_batch[i] * lam + img_batch[j] * (1-lam)
        
        return img_batch


`CutMix`:

     def __augment2(self, img_batch, cutmix_prob=0.5):
        batch_size, height, width, channels = img_batch.shape

        idx = np.random.permutation(batch_size)
        lam = np.random.beta(0.5, 0.5) 
        
        for i in range(batch_size):
            if np.random.rand() <= cutmix_prob:  
                j = idx[i]
    
                cut_width = min(int(width * lam), 50)
                cut_height = min(int(height * lam), 50)
                cut_x = np.random.randint(0, width-cut_width+1)
                cut_y = np.random.randint(0, height-cut_height+1)
            
                img_batch[i,cut_y:cut_y+cut_height,cut_x:cut_x+cut_width,:] = img_batch[j,cut_y:cut_y+cut_height, cut_x:cut_x+cut_width,:]
        
        return img_batch

## Custom Augmentation

`Needle Augmentation`: https://www.kaggle.com/seoyunje/needle-augmentation
