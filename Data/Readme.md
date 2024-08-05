## How to use Kaggle Datasets in google colab? 

To use kaggle datasets in colab you should follow these steps :
1) Click on your profile avatar, from top right corner

2) Go to Settings -> Accounts -> API

3) First click on expired token to expired token(if you use a token already)

4) Now click on Create New Token to download a kaggle.json file.!

![](https://www.googleapis.com/download/storage/v1/b/kaggle-forum-message-attachments/o/inbox%2F13611282%2F522ff946b510cc401b228975b7fb7fdc%2FScreenshot%20from%202024-05-10%2017-08-08.png?generation=1715348599738729&alt=media)

    ! pip install -q opendatasets
    import opendatasets as od
    od.download('https://www.kaggle.com/datasets/zalando-research/fashionmnist')

![](https://www.googleapis.com/download/storage/v1/b/kaggle-forum-message-attachments/o/inbox%2F13611282%2Fe513609c38c047e32ebdcc69676c1766%2FScreenshot%20from%202024-05-10%2017-20-58.png?generation=1715349072557022&alt=media)


![](https://www.googleapis.com/download/storage/v1/b/kaggle-forum-message-attachments/o/inbox%2F13611282%2Fa1f2868c77fce08eef80bdf2294e166b%2FScreenshot%20from%202024-05-10%2017-22-21.png?generation=1715349305203868&alt=media)

## What we will gonna use data in kaggle dataset?

1. https://www.kaggle.com/datasets/jtiptj/chest-xray-pneumoniacovid19tuberculosis
   
=>  Select Only Covid19 Data from this dataset, There are 566images from train,test(not valid)

2. https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia

=> Select Only Pneumonia from this dataset, There are 3875images from train(not test, val)

3., https://www.kaggle.com/datasets/tawsifurrahman/tuberculosis-tb-chest-xray-dataset

=> Select Only Tuberculosis from this dataset, There are 700images

4. https://www.kaggle.com/datasets/nih-chest-xrays/data

=> Select only 8 lung diseases(`Edema`, `Pneumonia`,`Tuberculosis`, `Cardiomegaly`, `Emphysema`, `Covid`, `Effusion`, `Atelectasis`) and No Finding
📌 There are totla 112,000images from this dataset, so it will take 10~20mintues for loading.
