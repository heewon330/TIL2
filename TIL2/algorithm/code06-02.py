# 함수
def isStackFull(): #스택이 꽉 차있는지 확인
    global SIZE, stack, top
    if (top >= SIZE-1):
        return True
    else:
        return False

def push(data):
    global SIZE, stack, top
    if (isStackFull()):
        print('stack full')
        return
    top +=1
    stack[top] = data


def isStackEmpty(): #스택이 꽉 차있는지 확인
    global SIZE, stack, top
    if (top <= -1):
        return True
    else:
        return False

def pop():
    global SIZE, stack, top
    if (isStackEmpty()):
        print('stack empty')
        return None
    data = stack[top]
    stack[top]=None
    top -=1
    return data

def peek():
    global SIZE, stack, top
    if (isStackEmpty()):
        print('stack empty')
        return None
    return stack[top]

# 전역
SIZE=5
stack = [None for _ in range(SIZE)]
top = -1

# 메인

stack = ['커피', None, None,None]
top=0
# push('보리차')
# print(stack)
# push('사이다')
# print(stack)

print('다음 나올 예정: ', peek())
print(pop())
print(pop())
