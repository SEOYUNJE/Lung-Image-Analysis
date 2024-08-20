### CLAHE
![train f1](https://github.com/user-attachments/assets/614be174-37fe-4032-8a5f-5ba4a52f1ad3)

![test f1](https://github.com/user-attachments/assets/b5981b66-54a8-4788-8f83-2a6679ce89e4)

📌 Best CLAHE parameter: `clipLimit(2) & tileGridSize(8,8)`

### CLAHE-HE
1Step: `Clahe[cliplimit:2, tilegridsize: (8,8)]`

2Step: `Histogram Equalization`

![clahe-he](https://github.com/user-attachments/assets/c3f8fa4a-1da8-439d-adef-b121488291c7)


### HE-CLAHE
1Step. `Histogram Equalization`

2Step. `Clahe[cliplimit:2, tilegridsize: (8,8)]`

![he-clahe](https://github.com/user-attachments/assets/2a517a9a-3415-4b89-9e97-a37bc85f8d90)


### CLAHE-Unsharp Masking
