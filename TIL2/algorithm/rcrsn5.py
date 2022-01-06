# 재귀 호출
## n제곱
## 함수
tab=' '
def pow(x, n):
    global tab
    tab += ' '
    if n==0:
        return 1
    print(tab+"%d*%d^(%d-%d)" % (x,x,n,1))
    return x * pow(x,n-1)
## 전역

## 메인
print('2^4')
print('답:', pow(2,4))