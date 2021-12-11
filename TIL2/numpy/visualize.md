plt.figure(figsize=15,5)  # 그래프 모양 바꾸기



multiple='dodge'  # 그래프가 겹치지 않고 보여줌

multiple = 'stack' # 그래프가 위로 쌓여진 것

multiple = 'fill'  #상대적으로 꽉 채운그래프에서 비율로 나타낸것



- boxplot
  - 탐색적 자료 분석에 사용
  - 4분위수 이용한 시각화
    - 이상치 확인 용도
    - 자료를 4구간으로 나눈 값
    - 1분위수 :자료의 25%
    - 2분위수 :자료의 50%=중앙값
    - 3분위수 :자료의 75%
  - IQR(Inter Quantile Range)
    - IQR+Q3-Q1
    - 최대제한선 = Q3+(IQR*1.5)
    - 최소제한선 = Q1-(IQR*1.5)





```python
sns.scatterplot(data=rawData_without_outlier,x='IDL콜레스테롤',y='트리글리세라이드',hue='흡연상태',size='총콜레스테롤',sizes=(20,400))
```

- size라는 파라미터를 이용해 총콜레스테롤에 따라 크기 차이를 둠.





