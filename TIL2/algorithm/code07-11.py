### 원형 큐
## 원형 큐는 한 칸을 못씀 (규칙)
## 오버헤드가 발생하지 않는 것이 장점
## 함수

def isQueueFull():
    global SIZE, queue, front, rear #전역변수
    if (rear +1) % SIZE == front: # !원형큐로 만들어주는 코드!
        return True
    else:
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
    rear = (rear+1) % SIZE # !원형큐의 특징!
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
    return queue[(front+1) % SIZE]


## 전역
SIZE=5
queue = [None for _ in range(SIZE)]
front = rear= 0

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
enQueue('선미')
print('출구>',queue,'<입구')