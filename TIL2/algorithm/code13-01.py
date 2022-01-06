# 순차 검색
## 정렬되지 않은 집합에서 검색하는 방법, 일일이 비교

import random
## 함수
def seqSearch(ary,fData):
    pos = -1
    for i in range(len(ary)):
        if ary[i] == fData:
            pos=i
            break
    return pos

## 전역
dataAry=[random.randint(10,99) for _ in range(20)] #20개 랜덤으로 뽑기
findData=dataAry[random.randint(0,19)]
# findData=1234

## 메인
print('배열 :',dataAry)
position=seqSearch(dataAry, findData)
if position == -1: #위치가 없다는 뜻
    print(findData, '없음')
else:
    print(findData, '는', position,'위치에 있음')