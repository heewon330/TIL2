### queue
## 함수

## 전역
SIZE=5
queue = [None for _ in range(SIZE)]
front = rear= -1

## 메인
#enQueue
rear += 1
queue[rear] = '화사'

rear += 1
queue[rear] = '솔라'

rear += 1
queue[rear] = '문별'
print('출구>',queue,'<입구')

#deQueue
front +=1
data=queue[front] #나중에 써먹을 것임
queue[front]=None
print('입장 손님:',data)

front +=1
data=queue[front] #나중에 써먹을 것임
queue[front]=None
print('입장 손님:',data)

front +=1
data=queue[front] #나중에 써먹을 것임
queue[front]=None
print('입장 손님:',data)
print('출구>',queue,'<입구')