# 재귀 호출
## 배열 합

import random
## 함수
def arySum(arr,n):
    if n<=0:
        return arr[0]
    return arySum(arr,n-1) + arr[n]

## 전역

## 메인
ary=[random.randint(0,255) for _ in range(10)]
print(ary)
print('배열의 합 :', arySum(ary,len(ary)-1))
