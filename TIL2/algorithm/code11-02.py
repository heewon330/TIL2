# 선택정렬-1 (두개의 배열 사용)
## 작은 순서대로 나열

import random
## 함수
def findMinIndex(ary):
    minIndex = 0
    for i in range(1, len(ary)):
        if (ary[minIndex]>ary[i]):
            minIndex = i
    return minIndex

## 전역
before=[random.randint(10,99) for _ in range(20)] #20개 랜덤으로 뽑기
after=[]
## 메인

print('정렬 전:', before)

for i in range(len(before)):
    minPos=findMinIndex(before)
    after.append(before[minPos])
    del(before[minPos])

print('정렬 후:', after)