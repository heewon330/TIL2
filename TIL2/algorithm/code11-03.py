# 선택정렬-2 (한개의 배열 사용)
## 작은 순서대로 나열

import random
## 함수
def selectionSort(ary):
    n=len(ary)
    for i in range(n-1):
        minIndex = i
        for j in range(i+1, n):
            if (ary[minIndex]>ary[j]):
                minIndex = j
        ary[i],ary[minIndex]=ary[minIndex],ary[i]
    return ary

## 전역
dataAry=[random.randint(10,99) for _ in range(20)] #20개 랜덤으로 뽑기

## 메인

print('정렬 전:', dataAry)
dataAry = selectionSort(dataAry)
print('정렬 후:', dataAry)