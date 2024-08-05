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

Resized Size = `224, 224`
Interpolation = `bilinear`

![](https://www.kaggleusercontent.com/kf/190526475/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..mTC_YwaldO5o4PWZe6vI8g.24zgvITvID73edf6LLUU6Af8ZSuAtODkfnBA8qYGJOabDg_uovWR73lE4ch381-BNRixM5o3WGzT8GePSJgGe8kK_8_KmWG9jXwFXzGvTf8sqoejnC3o9St6SgVqdj8Q6hod_pMffCy_bNTCN6Gkl1qabCRg2UMVuc0u3yaUkc82Ccs6QD5kiZ-4htyoSLv9c88Q0e-2xQjBHfhI695MCCpC0_IoHyNAMy_Rv0AFFH8MuDcqmZOgJtLpfdUliuG3buEDGOd0NnuSmtIjuwgEUKEOzBqYaIyLJzzcErEyHkTS5IZTib_YFOYF-3U4XZRVuODD7NIpb8miYDBDzpkYeni9i3FpS8_BBJuNF3Sbar9eZgMKYH78v6N8lWmk16cvQOxGSz2bsLpyWCZ-Zzwi58-qs6AVrsT3bqz03XglzveDs4j4z4F10alR4c-4ToKi2_t1VdbD2ifUgw-i6_AouMLvYdMcdSriYBxybcLQncbRlAUh0Ufc8r0qqwdOpfTMeRL5xzumNwpfbjQnDySbfwOh2DFsdgQespKXU67v9A97WOfpEuFyB9t3vmhBLCGer_QLdUQhB_HGr_fRCzRARqGkztNcpzgJKWtnFMcH1maITtV-_289FBS08CaY71cpWnOLJnivm6kxs5_DbeWyxl8HVftlh3w7ibifNEHFXGg.8XIxLzGYVSH0WstO5aDi7A/__results___files/__results___41_0.png)



