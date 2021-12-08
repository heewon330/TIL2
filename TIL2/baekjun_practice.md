```python
a=int(input())
b=int(input())
c=int(input())

solve = a * b * c
solve = list(map(int,str(solve)))

ans = [0] * 10

for i in solve:
  ans[i] +=1
print(*ans,sep='\n')
```

나머지

```python
ans= [0] *42
for _ in range(10): # 열 번 반복
  a=int(input())
  i=a % 42
  ans[i] = 1

print(sum(ans))
```



제일큰 숫자의 순서

```python
big=101 # 내 코드
a=[0]*9
for i in range(9):
  n=int(input())
  a[i]=n
  if big==101 or big<n:
        big=n

for i in range(len(a)):
  if a[i]==big:
    b=i+1

print(big,b,sep='\n')
```

```python
max=0 #강사님 코드
maxi=0
for i in range(1,10):
    n =int (input())
    if max < n:
        max=n
        maxi=1
print(max)
print(maxi)
```

바둑판 19 X 19

```
n=int(input())
a=[ [0] *19 for _ in range(19)] ## 19 X 19 행렬로 만들기
for _ in range(n):
  i,j=map(int,input().split())
  a[i-1][j-1]=1


for row in a:
  for col in row:
    print(col, end=' ')
  print() # 행렬 표시
```

