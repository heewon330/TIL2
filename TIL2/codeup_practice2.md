```python
# 한 라인씩 입력을 처리하는 함수
# 줄을 바꿔서 입력이 주어짐
# 매 라인마다 반복적으로 입력 처리
# input은 모든 입력을 문자열 형태로 변환

# 한 번에 처리할 필요 없음
# 각각의 입력을 별도의 케이스로 보고 그때그때 처리함
while True:
  line=input()
  print(line)
```

- input은 문자열만 받음
- 즉, 숫자열을 받고 싶다면 설정을 해줘야함. (int float 등)
- input은 뉴라인(라인의 끝,LF)이 될 때까지 값을 받음. 엔터 칠때까지~





72번

```python
n=int(input())

for i in range (n,0,-1):
	print(i)
```

74번

```python
n=ord(input()) # 문자를 아스키코드(숫자)로 변경
print(chr(n)) # 아스키코드에 해당되는 문자로 출력
```

```python
n=ord(input())
t=ord('a')

for ch in range(t,n+1):
    print(chr(ch),end=" ")
```

77번

```python
n=int(input())
total = 0
for i in range(0,n+1,2): # 짝수만 출력
	total +=i
	
print(total)
```

81번

```python
n=int(input(),base=16) #16진수
for i in range (1,16):
    print(f'{n:X}*{i:X}={n*i:X}') # X는 16진수로 변환해주는 것, f string
```



별찍기

```python
n=int(input())
for i in range(n):
    for j in range(i+1):
        print('*',end='')
    print()
```

```python
n=int(input())
for i in range(n):
  for k in range(n-i):
    print(" ",end='')

  for j in range(i+1):
    print('*',end='')
  print()
```

```python
n=int(input())
for i in range(n):
   for j in range(n-i):
    print('*',end="")
   print()
```

```python
n=int(input())
for i in range(n):
  for k in range(i):
    print(" ",end="")
  for j in range(n-i):
    print("*",end="")

  print()
```

```python
n=int(input())
for i in range(n):
  for k in range(n-i-1):
    print(" ",end='')

  for j in range(2*i+1):
    print('*',end='')

  print()
```

출석부 -리스트 이용하여 수 세기

```
n=int(input())
a=list(map(int, input().split()))

check = [0] *24

for i in range(n):
   check[a[i]] += 1

for i in range(1, len(check)):
    print(check[i], end=' ')

```

거꾸로

```python
n=int(input())
a=list(map(int,input().split()))

check=[0]*n # 내가 작성한 코드

for i in range(n):
    check[i]=a[n-i-1]
    
print(*check,sep=' ')
```

```python
n=int(input())
a=list(map(int,input().split()))

for i in a[::-1]: # 강사님 코드
    print(i,end=' ')
```

```python
n=int(input())
a=list(map(int,input().split()))
a.reverse()
print(*a,sep=" ")
```

최소값

```python
n=int(input())
a=list(map(int,input().split()))
b=99999999999999999999
for i in a:
    if i<b:
        b=i
print(b)  
    
```

```python
n=int(input())
a=list(map(int,input().split()))
mini=-1


for i in a:
    if mini==-1 or mini >i:
        mini=i
print(mini)  
```

최대최소

```python
n=int(input())
a=list(map(int,input().split()))
big=1000001
mini=-1000001
for i in a :
    if big==1000001 or big<i:
        big=i
for i in a:
    if mini==-1000001 or mini >i:
        mini=i

        
print(mini, big)
```

바둑알 십자

```
x, y = 10, 10

for j in range(19):
  if j != y-1: 
    if a[x-1][j] == 1: a[x-1][j] = 0
    elif a[x-1][j] == 0: a[x-1][j] = 1
    
for i in range(19):
  if i != x-1: 
    if a[i][y-1] == 1: a[i][y-1] = 0
    elif a[i][y-1] == 0: a[i][y-1] = 1

print(a)
```

```python
# 19 x 19의 리스트를 입력
a = [ list(map(int, input().split())) for _ in range(19) ]
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    
    for j in range(19):
      if j != y-1: 
        if a[x-1][j] == 1: a[x-1][j] = 0
        elif a[x-1][j] == 0: a[x-1][j] = 1
        
    for i in range(19):
      if i != x-1: 
        if a[i][y-1] == 1: a[i][y-1] = 0
        elif a[i][y-1] == 0: a[i][y-1] = 1
        
for i in range(19):
  for j in range(19):
    print( a[i][j], end= ' ' )
  print()
```



- 다차원 리스트 입력 받기

```python
a=[list(map(int, input().split())) for _ in range(19)]

# 19열 리스트 받기
```

- 리스트에 별 넣기

```python
n=5
a=[ [''] * 5 for _ in range(5)]

for i in range(5):
    for j in range(i+1):
        a[i][j]="*"
        
for i in range(5):
    for j in range(5):
        print(a[i][j],end='')
    print()
```

 
