# 이진 탐색 트리

## 함수/클래스
class TreeNode() :
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

## 전역
memory = []
root = None
nameAry=['블랙핑크','레드벨벳','마마무','에이핑크','걸스데이','트와이스']

## 메인
node = TreeNode()
node.data=nameAry[0]
root = node #리스트의 헤드와 비슷한 개념
memory.append(node)

for i in nameAry[1:]:
    node = TreeNode()
    node.data = i

    current = root # 항상 커런트를 기준으로 코딩
    while True:
        if i < current.data :
            if current.left == None:
                current.left=node
                break
            current=current.left
        else:
            if current.right == None:
                current.right=node
                break
            current=current.right

    memory.append(node)

print('이진 탐색 트리 완성')

#이진 탐색 트리 활용 (검색)
findName = '바마무'
current = root
while True:
    if findName == current.data :
        print(findName, 'found')
        break
    elif findName <current.data:
        if current.left == None:
            print(findName,' not found')
            break
        current=current.left
    else:
        if current.right == None:
            print(findName,'not found')
            break
        current=current.right
print('종료')