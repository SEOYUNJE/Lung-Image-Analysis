# Lung-Image-Analysis
📌 classify lung diseases in Chest X-Ray Images

## Overview
The detection and classification of diseases from Chest X-ray (CXR) images is a crucial task in medical diagnostics, enabling timely and accurate identification of various thoracic conditions. This project aims to leverage advanced machine learning and deep learning techniques to detect and classify distinct diseases from CXR images.

## Description
Chest X-ray (CXR) imaging is a fundamental diagnostic tool in medical practice, widely used for the assessment and management of various thoracic conditions. The objective of this project is to harness the power of machine learning and deep learning technologies to detect and classify ten specific diseases from CXR images, Edema, Pneumonia, Tuberculosis, Cardiomegaly, Emphysema, Covid, Effusion, Atelectasis. The successful implementation of this project can significantly aid radiologists by providing a reliable, quick, and accurate diagnostic assistant, thus improving patient care and outcomes.

## Evaluation
The primary evaluation metric will be categorical cross-entropy. This metric is particularly suited for multi-class classification tasks where the goal is to predict the probability distribution over different classes. Categorical cross-entropy is defined as:

![](https://www.googleapis.com/download/storage/v1/b/kaggle-forum-message-attachments/o/inbox%2F16438831%2Fb1e5843855417ef733e697521323b48f%2FCCE.JPG?generation=1722820972412209&alt=media)

## Data Description
#### Citations
- [NIH Chest X-rays](https://www.kaggle.com/datasets/nih-chest-xrays/data)

  📌 Select Edema, No Finding, Pneumonia, Tuberculosis, Cardiomegaly, Emphysema, Covid, Effusion, Atelectasis
- [Chest X-Ray(Pneumonia, Covid-19, Tuberculosis)](https://www.kaggle.com/datasets/jtiptj/chest-xray-pneumoniacovid19tuberculosis)
  
  📌 Select Only Covid-19 
- [Chest X-Ray Images(Pneumonia)](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia)
  
  📌Select Only Pneumonia
- [Tuberculosis(TB) Chest X-ray Database ](https://www.kaggle.com/datasets/tawsifurrahman/tuberculosis-tb-chest-xray-dataset)
  
  📌Select Only Tuberculosis
  
#### Modifications to original data 
- We have modified the original dataset by selecting only 8 specific lung diseases. This targeted approach allows for a more detailed and accurate classification and detection system.
There are 9classes(8 diseases, and one for "No Findings")

- Edema
- No Finding
- Pneumonia
- Tuberculosis
- Cardiomegaly
- Emphysema
- Covid
- Effusion
- Atelectasis

