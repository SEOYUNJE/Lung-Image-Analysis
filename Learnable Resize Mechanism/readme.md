# Learning to Resize Images for Vision Transformer 

Usually Transformer based models with high resolution may not fit into GPU, In such cases, we can adopt a **Trainable Resizer** mechansim as a backbone of the transformer models and performas joint learning of the image resizer and recognition models simultaneously.  
![](https://user-images.githubusercontent.com/17668390/138256285-c24f98db-ce35-4877-8741-221fd57d895e.jpg)

## Citations 
[Learning to Reisze in Computer Vision](https://keras.io/examples/vision/learnable_resizer/)
=> Description: How to optimally learn representations of images for a given resolution

## Impelmentation of Learning to Resize Mechanism
Our proposed resizer architecture is shown in below figure. 

(1) The bilinear feature resizing

(2) The skip connection that accommodates combining the bilinearly reisze image and the CNN features.

![](https://user-images.githubusercontent.com/17668390/138250657-29995830-b903-447f-8729-09b72b90ab3c.png)

## Examples in Chest X-Ray Images

#### Example 1
![ressize1](https://github.com/user-attachments/assets/05c213ab-44b1-4ae7-93bb-c07964177f80)

___ 
#### Example 2
![resize2](https://github.com/user-attachments/assets/ff149c2c-c008-452d-8465-08db24e4144b)



