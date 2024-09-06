| Brightness Limit | Contrast Limit | 확률 | 훈련 정확도 | 훈련 F1 점수 | 테스트 정확도 |
|------------------|----------------|------|------------|-------------|--------------|
| (-0.2, 0.2) | (-0.2, 0.2) | 0.0 | 0.6750 | 0.6668 | 0.6389 |
| (-0.1, 0.1) | (0, 0) | 0.5 | 0.6931 | 0.6876 | 0.6578 |
| (-0.2, 0.2) | (0, 0) | 0.5 | 0.6764 | 0.6733 | 0.6611 |
| (-0.3, 0.3) | (0, 0) | 0.5 | 0.6667 | 0.6593 | 0.6378 |
| (0, 0) | (-0.1, 0.1) | 0.5 | 0.6861 | 0.6784 | 0.6311 |
| (0, 0) | (-0.2, 0.2) | 0.5 | 0.6833 | 0.6808 | 0.6478 |
| (0, 0) | (-0.3, 0.3) | 0.5 | 0.6528 | 0.6451 | 0.6500 |
| (-0.1, 0.1) | (-0.1, 0.1) | 0.5 | 0.6806 | 0.6764 | 0.6533 |
| (-0.1, 0.1) | (-0.2, 0.2) | 0.5 | 0.7097 | 0.7048 | 0.6533 |
| (-0.1, 0.1) | (-0.3, 0.3) | 0.5 | 0.6833 | 0.6767 | 0.6533 |
| (-0.2, 0.2) | (-0.1, 0.1) | 0.5 | 0.6917 | 0.6869 | 0.6644 |
| (-0.2, 0.2) | (-0.2, 0.2) | 0.5 | 0.6708 | 0.6672 | 0.6633 |
| (-0.2, 0.2) | (-0.3, 0.3) | 0.5 | 0.6889 | 0.6870 | 0.6656 |
| (-0.3, 0.3) | (-0.1, 0.1) | 0.5 | 0.6764 | 0.6744 | 0.6678 |
| (-0.3, 0.3) | (-0.2, 0.2) | 0.5 | 0.6681 | 0.6606 | 0.6344 |
| (-0.3, 0.3) | (-0.3, 0.3) | 0.5 | 0.6667 | 0.6619 | 0.6389 |


```jsx
import React from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const data = [
  { name: '(-0.2, 0.2), (-0.2, 0.2), 0.0', train_acc: 0.6750, train_f1: 0.6668, test_acc: 0.6389 },
  { name: '(-0.1, 0.1), (0, 0), 0.5', train_acc: 0.6931, train_f1: 0.6876, test_acc: 0.6578 },
  { name: '(-0.2, 0.2), (0, 0), 0.5', train_acc: 0.6764, train_f1: 0.6733, test_acc: 0.6611 },
  { name: '(-0.3, 0.3), (0, 0), 0.5', train_acc: 0.6667, train_f1: 0.6593, test_acc: 0.6378 },
  { name: '(0, 0), (-0.1, 0.1), 0.5', train_acc: 0.6861, train_f1: 0.6784, test_acc: 0.6311 },
  { name: '(0, 0), (-0.2, 0.2), 0.5', train_acc: 0.6833, train_f1: 0.6808, test_acc: 0.6478 },
  { name: '(0, 0), (-0.3, 0.3), 0.5', train_acc: 0.6528, train_f1: 0.6451, test_acc: 0.6500 },
  { name: '(-0.1, 0.1), (-0.1, 0.1), 0.5', train_acc: 0.6806, train_f1: 0.6764, test_acc: 0.6533 },
  { name: '(-0.1, 0.1), (-0.2, 0.2), 0.5', train_acc: 0.7097, train_f1: 0.7048, test_acc: 0.6533 },
  { name: '(-0.1, 0.1), (-0.3, 0.3), 0.5', train_acc: 0.6833, train_f1: 0.6767, test_acc: 0.6533 },
  { name: '(-0.2, 0.2), (-0.1, 0.1), 0.5', train_acc: 0.6917, train_f1: 0.6869, test_acc: 0.6644 },
  { name: '(-0.2, 0.2), (-0.2, 0.2), 0.5', train_acc: 0.6708, train_f1: 0.6672, test_acc: 0.6633 },
  { name: '(-0.2, 0.2), (-0.3, 0.3), 0.5', train_acc: 0.6889, train_f1: 0.6870, test_acc: 0.6656 },
  { name: '(-0.3, 0.3), (-0.1, 0.1), 0.5', train_acc: 0.6764, train_f1: 0.6744, test_acc: 0.6678 },
  { name: '(-0.3, 0.3), (-0.2, 0.2), 0.5', train_acc: 0.6681, train_f1: 0.6606, test_acc: 0.6344 },
  { name: '(-0.3, 0.3), (-0.3, 0.3), 0.5', train_acc: 0.6667, train_f1: 0.6619, test_acc: 0.6389 },
];

const PerformanceGraph = () => (
  <ResponsiveContainer width="100%" height={400}>
    <BarChart
      data={data}
      margin={{
        top: 20,
        right: 30,
        left: 20,
        bottom: 5,
      }}
    >
      <CartesianGrid strokeDasharray="3 3" />
      <XAxis dataKey="name" angle={-45} textAnchor="end" interval={0} height={100} />
      <YAxis />
      <Tooltip />
      <Legend />
      <Bar dataKey="train_acc" fill="#8884d8" name="훈련 정확도" />
      <Bar dataKey="train_f1" fill="#82ca9d" name="훈련 F1 점수" />
      <Bar dataKey="test_acc" fill="#ffc658" name="테스트 정확도" />
    </BarChart>
  </ResponsiveContainer>
);

export default PerformanceGraph;
```
