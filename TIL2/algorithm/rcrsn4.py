# 재귀 호출
## 구구단
## 함수
def gugudan(n1, n2):
    print("%d X %d = %d" % (n1, n2, n1*n2))
    if n2<9:
        gugudan(n1, n2+1)

## 전역

## 메인
for n1 in range(2,10):
    print("## %d단 ##" %n1)
    gugudan(n1,1)