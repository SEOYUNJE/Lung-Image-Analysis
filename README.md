# Lung-Image-Analysis
📌 classify lung diseases in Chest X-Ray Images

## Overview
The detection and classification of diseases from Chest X-ray (CXR) images is a crucial task in medical diagnostics, enabling timely and accurate identification of various thoracic conditions. This project aims to leverage advanced machine learning and deep learning techniques to detect and classify distinct diseases from CXR images.

## Description
Chest X-ray (CXR) imaging is a fundamental diagnostic tool in medical practice, widely used for the assessment and management of various thoracic conditions. The objective of this project is to harness the power of machine learning and deep learning technologies to detect and classify ten specific diseases from CXR images, Edema, Pneumonia, Tuberculosis, Cardiomegaly, Emphysema, Covid, Effusion, Atelectasis. The successful implementation of this project can significantly aid radiologists by providing a reliable, quick, and accurate diagnostic assistant, thus improving patient care and outcomes.

## Data Description
#### Dataset
- [NIH Chest X-rays](https://www.kaggle.com/datasets/nih-chest-xrays/data

   | Finding Labels       | Count  |
   |----------------------|--------|
   | No Finding           | 60361  |
   | Infiltration         | 9547   |
   | Atelectasis          | 4215   |
   | Effusion             | 3955   |
   | Nodule               | 2705   |  
   | Pneumothorax         | 2194   |
   | Mass                 | 2139   |
   | Consolidation        | 1310   |
   | Pleural Thickening   | 1126   |
   | Cardiomegaly         | 1093   |
   | Emphysema            | 892    |
   | Fibrosis             | 727    |
   | Edema                | 628    |
   | Pneumonia            | 322    |
   | Hernia               | 110    |

#### Citations
- Wang X, Peng Y, Lu L, Lu Z, Bagheri M, Summers RM. ChestX-ray8: Hospital-scale Chest X-ray Database and Benchmarks on Weakly-Supervised Classification and - -Localization of Common Thorax Diseases. IEEE CVPR 2017, ChestX-ray8_Hospital-Scale_Chest_CVPR_2017_paper.pdf

- NIH News release: NIH Clinical Center provides one of the largest publicly available chest x-ray datasets to scientific community
  
- Original source files and documents: https://nihcc.app.box.com/v/ChestXray-NIHCC/folder/36938765345


  
#### Modifications to original data 
=> We have modified the original dataset by selecting only 9 specific lung diseases. This targeted approach allows for a more detailed and accurate classification and detection system.
There are 10classes(9 diseases, and one for "No Findings")


Here is **Modified Dataset** from NIH Dataset(For Speeding up, select only 300 data in each label)

  | Finding Labels       | Count |
  |----------------------|-------|
  | No Finding           | 300   |
  | Cardiomegaly         | 300   |
  | Edema                | 300   |
  | Consolidation        | 300   |
  | Atelectasis          | 300   |
  | Pneumonia            | 300   |
  | Effusion             | 300   |
  | Pneumothorax         | 300   |
  | Pleural Thickening   | 300   |
  | Emphysema            | 300   |


=> The image below is a diagram of hierarchical medical data.

![dataset](https://github.com/user-attachments/assets/f47ed564-a3d2-46c4-b329-e4d1674db36c)


