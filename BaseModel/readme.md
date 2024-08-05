## Pretrained Model
   I did use TensorFlow Implementation of `ResNet` & `EfficiententB0` & `Vision Transformer`

   For Speeding Up, I choose model which has smallest parameters like `resnet18`

   📌 In this [qubvel/classification_models](https://github.com/qubvel/classification_models)

   -> We can choose not only `resnet` But also `mobilenet`, `densenet`, `seresnet`, `VGG` etc.

   ![QUAVEL](https://github.com/user-attachments/assets/ef8f3ac6-5c43-499d-b4d4-83fe258fc552)

   📌 In this [qubvel/efficientnet](https://github.com/qubvel/efficientnet)

   -> We can choose below models(imagenet or noisy student) and `b0~b7`
   
   ![ns](https://github.com/user-attachments/assets/b62a30a8-c0ef-4dd0-92e8-fb4f2edbf5b1)

   📌 In this [vit_keras](https://github.com/faustomorales/vit-keras)
   
   We can choose `224X224`, `384X384` Image sizes, and then `vit_b16`, `vit_b32`, `vit_l16`, `vit_l32`
   
## Cross Validation
#### Using StratifiedKFold for Imbalanced Datasets
Given that you initially chose 500 images for each label to avoid imbalance but now need more data, which will reintroduce imbalance, using StratifiedKFold is a good option. StratifiedKFold ensures that each fold has the same proportion of each class as the original dataset.

#### Using GroupKFold By Patient ID
In medical datasets, it is often essential to use GroupKFold for cross-validation, particularly when you have multiple records for the same patient. Using patient IDs to define the groups ensures that the data related to each patient is not split between the training and validation sets. This approach helps in preventing data leakage and ensures that the model's performance evaluation is more realistic and reliable.

## Metric
=> `Accuracy` & `Macro F1 Loss`

     def f1_score(y_true, y_pred):
      # Calculate the F1 score for each class
        f1_scores = []
        num_classes = K.int_shape(y_pred)[-1]  # (batch_size, output_dims = num_classes)
    
     # Get the true and predicted class indices
        y_true = K.argmax(y_true, axis=-1)
        y_pred = K.argmax(y_pred, axis=-1) # For Label Smoothing(in CCE)

        for i in range(num_classes):
            true_positives = K.sum(K.cast(tf.logical_and(K.equal(y_true, i), K.equal(y_pred, i)), dtype=tf.float32))
            possible_positives = K.sum(K.cast(K.equal(y_true, i), dtype=tf.float32))
            predicted_positives = K.sum(K.cast(K.equal(y_pred, i), dtype=tf.float32))

            recall = true_positives / (possible_positives + K.epsilon())
            precision = true_positives / (predicted_positives + K.epsilon())
        
            f1_score = 2 * ((precision * recall) / (precision + recall + K.epsilon()))
            f1_scores.append(f1_score)
    
        # Calculate the macro-average F1 score
       macro_f1_score = K.mean(tf.stack(f1_scores))
       return macro_f1_score

## Loss 
We can choose 4 Types of Loss Function or we can combine two loss function for improving model's performance 

1) `CategoricalCrossEntropy()`
2) `CategoricalFocalCrossEntropy()`
3) `Macro F1 Loss()`
4) `Kullback–Leibler divergence()`
