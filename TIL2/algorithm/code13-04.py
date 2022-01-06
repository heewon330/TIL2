# 이진 검색
## 정렬이 되어 있는 집합이 전제조건

import random
## 함수
def binSearch(ary,fData):
    pos = -1 # 못찾을때 -1
    start = 0
    end = len(ary)-1
    while start <=end :
        mid = (start + end) // 2
        if fData == ary[mid]:
            return mid
        elif fData > ary[mid]:
            start = mid+1
        else:
            end=mid-1
    return pos

## 전역
dataAry=[random.randint(1,999) for _ in range(10)] #20개 랜덤으로 뽑기
findData=dataAry[random.randint(0,9)]
dataAry.sort() #정렬

## 메인
print('배열 :',dataAry)
position=binSearch(dataAry, findData)
if position == -1: #위치가 없다는 뜻
    print(findData, '없음')
else:
    print(findData, '는', position,'위치에 있음')