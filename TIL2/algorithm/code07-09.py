## 함수

def isQueueFull():
    global SIZE, queue, front, rear #전역변수
    if rear != SIZE-1:
        return False
    elif (rear == SIZE-1) and (front ==-1):
        return True
    else:
        for i in range(front+1,SIZE):
            queue[i-1]=queue[i]
            queue[i]=None
        front -= 1
        rear -=1
        return False

def isQueueNone():
    global SIZE, queue, front, rear #전역변수
    if rear== front:
        return True
    else:
        return False   


def enQueue(data):
    global SIZE, queue, front, rear #전역변수
    if isQueueFull():
        print('queue is full')
        return
    rear+=1
    queue[rear]=data


def deQueue():
    global SIZE, queue, front, rear #전역변수
    if isQueueNone():
        print('queue is empty')
        return None
    front +=1
    data=queue[front]
    queue[front]=None

    return data

def peek(): #그 다음에 나갈 데이터
    global SIZE, queue, front, rear
    if isQueueNone():
        print('queue is empty')
        return None
    return queue[front+1]


## 전역
SIZE=5
queue = [None for _ in range(SIZE)]
front = rear= -1

## 메인
enQueue('화사')
enQueue('솔라')
enQueue('문별')
enQueue('휘인')
enQueue('선미')
print('출구>',queue,'<입구')

print('입장손님 :',deQueue())
print('입장손님 :',deQueue())
print('출구>',queue,'<입구')
enQueue('수영')
print('출구>',queue,'<입구')
enQueue('재현')
print('출구>',queue,'<입구')
enQueue('태용')
print('출구>',queue,'<입구')