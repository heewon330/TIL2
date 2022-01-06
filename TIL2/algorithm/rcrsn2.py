# 재귀 호출
## 우주선 발사 카운트다운

## 함수
def rocket(num):
    if num ==0:
        print('발사')
    else:
        print(num)
        rocket(num-1)
## 전역

## 메인
rocket(5)