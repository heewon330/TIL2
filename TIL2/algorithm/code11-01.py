# 정렬
## 최솟값 찾기

import random
## 함수
def findMinIndex(ary):
    minIndex = 0
    for i in range(1, len(ary)):
        if (ary[minIndex]>ary[i]):
            minIndex = i
    return minIndex

## 전역
testAry=[random.randint(1,99) for _ in range(20)] #20개 랜덤으로 뽑기
print(testAry)
## 메인
minPos=findMinIndex(testAry)
print('최솟값 :',testAry[minPos])
