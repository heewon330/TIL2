# 선형 리스트

# 함수
def add_data(friend):  #선형리스트에 추가
    katok.append(None)
    i=len(katok)
    katok[i-1]=friend


def insert_data(position, friend): #데이터 삽입
    katok.append(None)
    i=len(katok)
    for i in range(i-1,position,-1):
        katok[i]=katok[i-1]
        katok[i-1]=None
    katok[position] = friend


def delete_data(position):
    katok[position]= None
    i=len(katok)
    for i in range(position+1, i):
        katok[i-1]=katok[i]
        katok[i]= None
    del(katok[i])


#전역변수
katok=[]

#메인코드

add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')
add_data('모모')

insert_data(3,'미나')
print(katok)
insert_data(5,'수영')
print(katok)
delete_data(4)
print(katok)