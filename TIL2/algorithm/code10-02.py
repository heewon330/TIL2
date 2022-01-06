# 재귀 호출
## 횟수 제한

## 함수
def openBox(): # 무한루프 돌게 됨
    global count
    print('상자 열기')
    count -= 1
    if count == 0 :
        print('## 반지 넣기 ##')
        return # 돌아가기
    openBox()
    print('상자 닫기')
    return
## 전역

## 메인
count=10
openBox()