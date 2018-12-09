## GridSearch for randomforest, gradientboost
```
ember: we trained a gradientboosed decision tree (GBDT) model using LightGBM with default parameters (100 trees, 31 leaves per tree)
reference: https://arxiv.org/pdf/1804.04637.pdf
```
  
n_estimators: 트리의 수
max_depth: 트리의 깊이
    
# GridSearch randomforest 실험 결과
```
특성: test6사용
실험환경 i7-8700, 16GB Ram
```
    
### default parameter(not used GridSearch)
```
93.746873 %
```
    
### case 1
```
params = {
    'n_estimators': [1,2,3,4,5],    
    'max_depth': [100, 150, 200],
}

{'max_depth': 200, 'n_estimators': 5}
0.9250688016012009
```
    
### case 2

```
params = {
    'n_estimators': [1000, 1500, 2000, 2500],    
    'max_depth': [200, 230, 240],
}

{'max_depth': 230, 'n_estimators': 1500}
0.9321991493620215
94.197099 %
              precision    recall  f1-score   support

           0       0.86      0.94      0.90       540
           1       0.98      0.94      0.96      1459

   micro avg       0.94      0.94      0.94      1999
   macro avg       0.92      0.94      0.93      1999
weighted avg       0.95      0.94      0.94      1999
```
    
# 결과
case1는 i7-8700기준으로 약 2분정도 시간 소요
case2는 i7-8700기준으로 약 5분정도 시간 소요
```
n_estimators(트리의 수)가 많을 수록 시간이 엄청 오래 걸림
n_estimators, max_depth와 적절히 섞으면 좋은 효율이 나옴
```
    
# TO do 
K-fold 교차검증    

# reference
PE Format 공식 문서: https://docs.microsoft.com/en-us/windows/desktop/debug/pe-format#file-headers  
pestudio: https://www.winitor.com/  
ember논문: reference: https://arxiv.org/pdf/1804.04637.pdf  