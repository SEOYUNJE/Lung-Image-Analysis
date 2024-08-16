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

## Label_Unique vs Label_Unique_f 

label_unique가 2이상인 no finding의 위치는 크게 2가지로 분류할 수 있다.

<Case1>: 맨 앞에 No Finding이 있는 경우 
    
![case1](https://github.com/user-attachments/assets/8c6399dc-81b7-4d12-a1c9-a21e8bbf7a33)

<Case2>: 중간 지점에 No Finding이 있는 경우 

![case2](https://github.com/user-attachments/assets/bac1299e-ef42-45b1-95a8-4250987f9815)


=> 이때 Case의 경우 label_unique에다가 f를 붙여서 2_f, 3_f 식으로 표기했다

![label_unique_f](https://github.com/user-attachments/assets/4974c82a-88d5-4395-b730-24c136810a6e)


## Conclusion

아래의 그래프는 최종 Loss graph로써 No Finding 중 No Change에 대한 가능성을 짐작할 수 있다. 

![label_ff](https://github.com/user-attachments/assets/94807359-9a7e-4b75-aa12-b989229fe972)


