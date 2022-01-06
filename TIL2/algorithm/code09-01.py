# 그래프
## 함수
class Graph():
    def __init__(self, size): # 정점의 개수 = size
        self.SIZE=size
        self.graph=[[0 for _ in range(size)] for _ in range(size)]
## 전역
G=None
## 메인
G=Graph(4) # 4X4 이차원 배열
# G.graph[0][1] =1 ;G.graph[0][2] =1 ;G.graph[0][3] =1

for row in range(4):
    for col in range(4):
        if row != col :
            G.graph[row][col]=1
        else:
            G.graph[row][col]=0

        print(G.graph[row][col],end=' ')
    print()