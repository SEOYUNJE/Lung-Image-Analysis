### Label Unique

각 Patient ID 당 하나의 Label만 있을수도 있고 여러개의 Label이 존재할 수도 있다 

Label Unique라는 변수는 동일 Patient ID 당 label의 갯수를 의미하는 변수이다. 

    tmp = df.groupby('Patient ID')['Finding Labels'].nunique()
    tmp = tmp.reset_index().rename(columns={'Finding Labels':'label_nunique'})

    df = df.merge(tmp, on='Patient ID', how='left')

![label unique](https://github.com/user-attachments/assets/3acab41d-b5cb-44ff-a88c-deb08205be12)

### No Finding? No Change?

Label Unique가 1에 해당하는 No Finding의 경우는 아무 문제가 없지만

Label Unique가 2이상의 No Finding 중 그전 Follow up에 해당하는 질병에서 No Changed인 경우가 발견되었다.

이에 학습한 이후 실제 Label Unique 1의 No Finding과 Label Unique 2의 No Finding의 Loss 값을 비교하면서
No Changed의 가능성에 대해 확인해보겠다. 

plt.figure(figsize=(12,6))

    tmp = df_loss[df_loss['Finding Labels'] == 'No Finding']
    plt.title('Distribution of Loss for each label_unique in No Finding')
    sns.boxplot(x='label_nunique', y='loss', data=tmp)
    plt.show()

![image](https://github.com/user-attachments/assets/e63be795-a869-44ee-8ad7-99b2f8050963)
