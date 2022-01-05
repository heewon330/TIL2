#  연결 리스트

## 함수
class Node() :
    def __init__(self):
        self.data = None
        self.link = None

    
def printNodes(start):
    current = start
    print(current.data, end= ' ')
    while current.link != None :
        current = current.link
        print(current.data, end=' ')
    print()

def insertNode(findData, insertData) : # findData 앞에 insertData 삽입하려면?
    global memory, head, current, pre
    if head.data==findData :
        node = Node()
        node.data=insertData
        node.link=head
        head = node
        return
    # 중간 노드 앞에 삽입
    current = head
    while current.link != None:
        pre = current # 프리가 일단 커런트 붙잡고 있게 함
        current = current.link #옆 노드로 움직임
        if current.data == findData :
            node=Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return

        #findData가 없을 땐 마지막에 추가
    node=Node()
    node.data=insertData
    current.link=node
    return

def deleteNode(deleteData) :
    global memory, head, current, pre
    if head.data == deleteData: #첫노드 삭제
        current = head
        head =head.link
        del(current)
        return
    #첫 노드 외의 삭제
    current = head
    while current.link != None:
        pre = current
        current= current.link
        if current.data==deleteData:
            pre.link=current.link
            del(current)
            return

def findNode(findData): # 노드 검색
    global memory, head, current, pre
    current = head
    if current.data == findData:
        return current
    while current.link != None :
        current = current.link
        if current.data == findData:
            return current
    return Node()
## 전역
memory=[]
head, current, pre = None, None, None
dataArray=['다현','정연','쯔위','사나','지효']

## 메인

node=Node() # 첫 노드
node.data=dataArray[0]
head = node #헤드를 설정하는 것은 매우 중요!!
memory.append(node) #강노4-18 그림 참고


for i in dataArray[1:]: #[정연, ~ ,지효]
    pre=node # 직전 노드를 pre로 설정
    node=Node()
    node.data=i
    pre.link=node
    memory.append(node)

printNodes(head)

insertNode('다현','화사')
printNodes(head)

insertNode('재현','문별')
printNodes(head)

deleteNode('화사')
printNodes(head)

deleteNode('쯔위')
printNodes(head)

fNode=findNode('쯔위')
print(fNode.data)

fNode=findNode('지효')
print(fNode.data)
