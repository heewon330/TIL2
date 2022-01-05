# 함수3

katok=[]

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


select=int(input("선택하세요(1. 추가, 2. 삽입, 3. 삭제, 4. 종료) -->"))
while (select):  
    if select==1 :
        data=input('추가할 데이터 :')
        add_data(data)
        print(katok)
    elif select==2:
        p=int(input('삽입할 위치 :'))
        data=input('삽입할 데이터 :')
        insert_data(data)
        print(katok)
    elif select==3:
        p=int(input('삭제할 위치 :'))
        delete_data(data)
        print(katok)  
    elif select ==4:
        print(katok)
        exit
    else:
        print("다시 선택하세요")
        continue