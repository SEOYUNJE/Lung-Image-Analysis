### How to use Rapid Dataset

https://www.kaggle.com/datasets/seoyunje/rapid-cxr-dataset/settings

1. `Kaggle`
   
       df = pd.read_csv('/kaggle/input/rapid-cxr-dataset/metadata.csv')
       tmp = {os.path.basename(x): x for x in glob(os.path.join('/kaggle', 'input', '*','*','*', '*'))}    
     
       df['path'] = df['Image Index'].map(tmp)

3. `Google Colab`

       df = pd.read_csv('/content/rapid-cxr-dataset/metadata.csv')
       tmp = {os.path.basename(x): x for x in glob(os.path.join('/content', '*','*','*', '*'))}    
     
       df['path'] = df['Image Index'].map(tmp)
