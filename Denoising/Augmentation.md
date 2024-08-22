## Image Augmentation

![](https://albumentations.ai/docs/images/getting_started/augmenting_images/augmentation_pipeline_visualized.jpg)


### Weak Augmentation

**Flip**
- `HorizontalFlip`: albumentations.HorizontalFlip(p=None)
- `VerticalFlip`: albumentations.VerticalFlip(p=None)

**Rotate**
- `Rotate`: albumentations.Rotate(limit=None, p=None)

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

`Mixup`

`CutMix`
