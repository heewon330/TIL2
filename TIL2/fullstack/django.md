# Django 시작

장고 프로젝트 만들기

```django
django-admin startproject ToDoList
```

파일 생성됨

- `__init__`.py
- asgi.py : 웹사이트를 서버를 통해 배포 시 사용
- **settings.py** : 프로젝트의 환경 설정 파일(중요)
- urls.py : URL 설정
- wsgi.py : 웹사이트를 서버를 통해 배포 시 사용
- manage.py :전체적인 프로젝트 관리 가능 -> 초기화, 이미그레이션, 앱생성,삭제 등등

가상서버 실행

```
python manage.py runserver
```

앱 만들기

- 하나의 프로젝트=여러 개의 앱

```
python manage.py startapp my_to_do_app
```

MVC 구조

- 웹 프레임워크 구조 : 구조 제어하기 편하게 미리 만들어 놓은 구조
- MVC  : Model, View, Controll - 기능별로 프레임워크가 나눠져 있음
  - Model :db관련,  models.py 이용
  - View : 화면에 보여지는 것, Templates 이용, 컨트롤 역할,  url과 탬플릿을 연결 및 중재
  - Control : view와 model 사이 제어, views.py 이용



탬플릿 작성(p.134)

- view를 담당 : 사용자에게 보여지는 기능, html을 브라우저에 보여질 수 있게 하는 기능
- templates 폴더를 앱폴더에 만들기 ->장고는 templates 폴더에서 찾을 것임
- templates 폴더 안에 앱이름과 동일하게 폴더 하나 더 만들기



## Django 프로젝트

(책 117쪽-163쪽)

### 앱 설치

settings.py에 추가

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

#기본 설치된 앱과 구분하기 위해 이렇게 표현하기도 함
INSTALLED_APPS += [
    'my_to_do_app',
    ]
```



### URL 설정(p.127)

- index.html과 url을 연결
- urls.py에서 설정

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # route가 빈 문자=서버 경로 다음에 아무것도 쓰지 않고 기본 경로로 사용하는 경우
    #include를 이용해서 하위 'URLconf'를 호출
    path('',include('my_to_do_app.urls')), #하위 url과 연결되도록함
    
    #앱 별로 url과 연결하고 싶다면
    #path('my_to_do_app',include('my_to_do_app.urls')), 
    path('admin/', admin.site.urls),
]
```

- path는 URL과 앱을 연결해주는 라우팅 함수 -> 필수 인자 2개
- path(route, view) 
  - route : URL 패턴 가진 문자열 -> 문자열에 해당하는 앱 또는 뷰와 연결



### 하위 URLconf

- 최상위 URLconf로부터 연결된다면 -> 해당 앱에 따로 'urls.py' 만들어줌

```
C:\hw\workspace\ToDoList\my_to_do_app\urls.py
```

그 urls.py에 작성

```python
from django.urls import path, include
#view랑 연결
from . import views

urlpatterns = [
#해당 url 패턴을 views.py의 index함수와 연결한다는 뜻
    path('', views.index), #view에 정의된 함수 index를 호출한다는 뜻
]
```



views.py에 작성

- view는 제어 역할을 함
- 템플릿과 모델 등의 연결 역할을 함
- index 함수

```python
def index(request):
    return render( request, 'my_to_do_app/index.html')
```



디비설정(p.143)

- 할 일(입력받은 데이터) 전달 받아서 db에 전달함



### 모델 만들기

- 할 일을 저장할 테이블은 '`models.py`'을 통해 작성
- 테이블 =pandas 'DataFrame'

ToDoList\my_to_do_app\models.py에서 작성

```python
from django.db import models

# Create your models here.
# 클래스의 이름=모델(테이블)의 이름
class Todo(models.Model): #models 모듈 내에 Model 클래스 받음
    content=models.CharField(max_length=255)
    # content는 Todo 테이블의 컬럼 이름이 됨
    # content 컬럼 타입은 문자타입. 최대 255바이트가 최대 크기
```

 

### 모델 적용

- 만들어진 모델을 실제 db에 반영
- 모델을 변경시킨 내용과 변경사항을 장고에 알려줌

```
python manage,py makemigrations 앱이름
```

- 변경사항을 실제 DB에 반영

```
python manage.py migrate
```

### 테이블 속성 확인

![image-20211223160626774](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20211223160626774.png)



### createTodo 기능 추가

- 전달받은 할일을 디비에 저장
  - URL 과 view 연결
  - view에 해당 기능 구현



urls.py

- 'createTodo' 요청 + views 연결
- ToDoList\my_to_do_app\urls.py에 입력

```python
urlpatterns = [
    path('', views.index),
      #createTodo에 대한 URL 요청과 view를 연결
    path('createTodo/', views.createTodo),
]
```



views.py

- 'URLconf'에서 설정된 내용대로 함수 정의
- 연결 잘 되었는지 확인용
- ToDoList\my_to_do_app\views.py에 입력

```python
def createTodo( request):
    #URL과 view가 잘 연결되었는지 확인하기 위해 아래 코드를 사용
    return HttpResponse('create Todo를 할 것입니다')
```

```python
def createTodo( request):

    #사용자가 입력한 할일을 잘 받아오는지 확인
    #입력값 전달은 POST 방식, 'todoContent' 변수 사용
    user_input_str=request.POST['todoContent']
    return HttpResponse(f'사용자가 입력한 값: {user_input_str}')
```





### DB에 저장하기

ToDoList\my_to_do_app\urls.py

```python
urlpatterns = [
    path('', views.index, name='index'), #인덱스 설정
      #createTodo에 대한 URL 요청과 view의 createTodo 함수를 연결 
    path('createTodo/', views.createTodo),
]
```



ToDoList\my_to_do_app\views.py 에 설정

```python
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# 미리 만들어진 model 가져오기
from .models import *

#index 페이지로 돌아가기 위한 reverse를 임포트
from django.urls import reverse

# Create your views here.

# url과 template을 연결. 장고에서 가장 많이 쓰임
def index(request):
    return render( request, 'my_to_do_app/index.html')

def createTodo( request):
    #URL과 view가 잘 연결되었는지 확인하기 위해 아래 코드를 사용
    #return HttpResponse('create Todo를 할 것입니다')

    #사용자가 입력한 할일을 잘 받아오는지 확인
    #입력값 전달은 POST 방식, 'todoContent' 변수 사용
   # user_input_str=request.POST['todoContent']
    #return HttpResponse(f'사용자가 입력한 값: {user_input_str}')

    user_input_str=request.POST['todoContent']
    #models.py에서 정의된 클래스를 이용해 전달받은 값을 db에 전달
    new_todo = Todo(content=user_input_str)
    new_todo.save()

    return HttpResponseRedirect(reverse('index')) #원래 페이지로 돌아가기
```



### 브라우저에 보이게 하려면?

view.py

```python
def index(request):

    #DB의 내용이 브라우저에 보이게끔 설정
    todos=Todo.objects.all()
    content={'todos':todos}
    
    return render( request, 'my_to_do_app/index.html',content)
```

### 삭제 delete

책 169쪽

**삭제하고 싶은 id 전달**

- get : 데이터를 전달할 때 URL을 통해서 전달

```
Request Method:	GET
Request URL:	http://127.0.0.1:8000/doneTodo/?todoNum=4
```

- post : form이 꼭 있어야만 함. 없으면 전달 불가능

shell에서 데이터 확인

```
>>> from my_to_do_app.models import Todo
>>> Todo.objects.all()
<QuerySet [<Todo: Todo object (1)>, <Todo: Todo object (2)>, <Todo: Todo object (3)>, <Todo: Todo object (4)>, <Todo: Todo object (5)>, <Todo: Todo object (6)>]>
```

**조건에 맞는 객체들만 가져오기**

1. filter

- `query set`  가져옴
- 조건에 맞는게 여러개여도 하나만 가져옴

```
>>> Todo.objects.filter(id=1)
<QuerySet [<Todo: Todo object (1)>]>
```

2. get 

- `객체`를 가져옴
- 조건에 맞는 여러개가 있으면 여러개 다 가져옴

```
>>> Todo.objects.get(id=1)
<Todo: Todo object (1)>
```

**삭제**

```
>>> obj=Todo.objects.get(id=1)
>>> obj.delete()
(1, {'my_to_do_app.Todo': 1})
>>> Todo.objects.all()
<QuerySet [<Todo: Todo object (2)>, <Todo: Todo object (3)>, <Todo: Todo object (4)>, <Todo: Todo object (5)>, <Todo: Todo object (6)>]>
```

### Update 데이터 수정

```
>>> obj=Todo.objects.get(id=5)
>>> obj.content='수정해봄'      
>>> obj.save()
```



ToDoList\my_to_do_app\urls.py

```python
urlpatterns = [
    path('', views.index, name='index'), #인덱스 설정
      #createTodo에 대한 URL 요청과 view의 createTodo 함수를 연결 
    path('createTodo/', views.createTodo),
    path('deleteTodo/', views.deleteTodo),
]
```

ToDoList\my_to_do_app\views.py

```python
def deleteTodo(request):
    print('요청변수 :', request.GET['todoNum'])
    todo = Todo.objects.get(id=request.GET['todoNum'])
    todo.delete()

    return HttpResponseRedirect(reverse('index'))
```





## Board 실습

### URL 연결하기

**workspace\board\board\urls.py**

```python
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('board/',include('board_app.urls')), 

    path('admin/',admin.site.urls),
]
```

- 기본 설정값 237.0.0.1:8000/board/



**workspace\board\board_app\urls.py**

```python
urlpatterns = [
    path('', views.index),
    path('login/', views.index2),
    path('write/', views.index3),

]
```

- url에 /board/login/, /board/write/가 뜰 수 있게끔 설정
- 설정이 안되어있는 경우엔 그냥 /board/



**workspace\board\board_app\views.py**

```python
def index(request):
    return render(request,'board_app/list.html')

def index2(request):
    return render(request,'board_app/login.html')

def index3(request):
    return render(request,'board_app/write.html')
```

- index함수들을 만들어서 해당되는 url과 연결



### STATIC 

**static 폴더 설정 -settings.py**

```python
STATIC_URL = 'static/'

STATICFILES_DTRS=[

  BASE_DIR / 'static'

]
```

**static 폴더를 바디(board) 폴더에 만들기**





### Table 만들어서 DB 저장

**클래스 정의**

board\board_app\models.py

```python
from django.db import models

# Create your models here.
# ORM(Object Relation mapping)

class board( models.Model) : #모델 클래스 상속
    createDate = models.DataField() #작성 날짜
    writer= models.CharField(max_length=128) #작성자
    subject = models.CharField(max_length=255) #글 제목
    content = models.TextField() 
```

**DB migration**

```
(multicampus) C:\hw\workspace\board>python manage.py migrat
```

**DB 입력& 저장**

```
>>> from board_app.models import board
         --------  ------        -----
         package    module        modules에 정의된 board 클래스
         
         
(multicampus) C:\hw\workspace\board>python manage.py shell

>>> import datetime
>>> b = board(createDate=datetime.date.today(), writer='me', subject='hello', content='bye')
>>> b.save()

>>> board.objects.all()
<QuerySet [<board: board object (1)>]>
>>> board.objects.filter(id=1)
<QuerySet [<board: board object (1)>]>
>>> board.objects.filter(id=10)
<QuerySet []>
>>>

>>> b=board(createDate=datetime.date.today(), writer='jhw', subject='hello', content='다음입력')
>>> b.content
'다음입력'
>>> b.createDate
datetime.date(2021, 12, 27)
>>> b.save()
>>> board.objects.all()
<QuerySet [<board: board object (1)>, <board: board object (2)>]>
-----------------------------------------------------------------
board클래스 타입의 객체를 원소로 가지고 있는 리스트를 반환(리스트는 이터레이블)=>쿼리셋도 이터레이블

```

- 반복 가능한 객체가 존재하기 때문에(반복문으로 가져다가 쓸 수 있음) 이터레이블
- 각 객체 자체들이 테이블의 로우들이 된다! = ORM(Object Relation Mapping)
  - "객체를 관계형 테이블과 매핑한 것"  **클래스.objects.all()**



**글 제목만 얻고 싶다? - 루프문 사용**

```
>>> for b in board.objects.all():
...     print(b.subject)
... 
hello
hello
>>>
-------------------------------------
이터레이블 객체를 가져오는 루프문
```

**원하는 객체 하나 뽑아오기**

```
>>> board.objects.get(id=1)
<board: board object (1)>
```

**DBshell로 데이터베이스 확인 가능**

```
(multicampus) C:\hw\workspace\board>python manage.py dbshell
SQLite version 3.36.0 2021-06-18 18:36:39
Enter ".help" for usage hints.

sqlite> .tables
auth_group                  board_app_board
auth_group_permissions      django_admin_log
auth_permission             django_content_type
auth_user                   django_migrations
auth_user_groups            django_session
auth_user_user_permissions

sqlite> select * from board_app_board;
1|2021-12-27|me|hello|bye
2|2021-12-27|jhw|hello|다음입력
3|2021-12-28|jwe|hi|next
```

sqlite(dbshell)를 사용할 때는 sql을 사용 => but orm으로 이용해서 객체를 다룰 수 있으므로 sql 몰라도 상관은 없음 -> **클래스.objects.all()** 이런 형태가 ORM이다~



### 게시글을 작성해서 게시판에 올리고 싶다면?

**<a = href='board/write'>**

```html
      <a href="board/write/">
        <button type="submit" class="btn btn-primary">게시글 작성하기</button>
      </a>
```

**write.html**

```html
<!DOCTYPE html>
<html>
  <head>
    {% load static %}
    <link type='text/css' rel='stylesheet' href='{% static "bootstrap.min.css" %}' />
    <link type='text/css' rel='stylesheet' href='{% static "bootstrap-theme.min.css" %}' />
    <link type='text/css' rel='stylesheet' href='{% static "list.css" %}' />

  <body>
    <nav class="navbar navbar-inverse navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">아주 간단한 게시판</a>
        </div>
        <div id="navbar" class="navbar-collapse collapse">
          <div class="navbar-form navbar-right">
            <button type="submit" class="btn btn-info">Sign in</button>
            <button type="submit" class="btn btn-success">Sign up</button>
          </div>
        </div><!--/.navbar-collapse -->
      </div>
    </nav>

    <hr> <!--가로선-->

    <div class='container'>
      <form action='../create' method='POST'> <!--제출하면 넘어가는 페이지 설정-->
        {% csrf_token %}
        <div class="form-group">
          <label for="exampleInputPassword1">작성 날짜</label>
          <input type="date" class="form-control" id='now_date'>
          <script>
            document.getElementById('now_date').valueAsDate = new Date();
          </script>
         
         
        </div>
        <div class="form-group">
          <label for="exampleInputEmail1">작성자</label>
          <input type="text" class="form-control" placeholder="작성자">
        </div>
        <div class="form-group">
          <label for="exampleInputPassword1">글 제목</label>
          <input type="text" class="form-control" >
        </div>
        <div class="form-group">
          <label for="exampleInputFile">게시글</label>
          <textarea class="form-control" rows=10></textarea>
        <button type="submit" class="btn btn-default">등록</button>
      </form>
    </div>
  </body>

</html>
```

**create와 연결하기**

write.html에 작성

```
{% csrf_token %}
```

board\board_app\urls.py

```python
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.index),
    path('write/', views.index3),
    path('create', views.create),

]
```

board\board_app\views.py

```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'board_app/list.html')

def index3(request):
    return render(request,'board_app/write.html')

def create(request):
    return HttpResponse('게시글을 생성합니다')
```

### DB에 저장

board\board_app\views.py -> create함수 참고

```python
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

from board_app.models import board

# Create your views here.

def index(request):
    return render(request,'board_app/list.html')

def index3(request):
    return render(request,'board_app/write.html')

# create 이용해 데이터베이스 저장하기!
def create( request):
    createDate=request.POST['createDate']
    writer=request.POST['user']
    subject=request.POST['subject']
    content=request.POST['content']

    new_list = board(createDate=createDate, writer=writer, subject=subject, content=content)
    new_list.save()

    print(createDate)
    print(writer)      #이 값들은 터미널로 출력됨

    return HttpResponse('게시글을 생성합니다')
```

dbshell로 확인

```
(multicampus) C:\hw\workspace\board>python manage.py dbshell
SQLite version 3.36.0 2021-06-18 18:36:39
Enter ".help" for usage hints.
sqlite> select * from board_app_board
   ...> ;
1|2021-12-27|me|hello|bye
2|2021-12-27|jhw|hello|다음입력
3|2021-12-28|jwe|hi|next
4|2021-12-28|11|11|1
5|2021-12-28|gd|asdf|asdfasdfasf
6|2021-12-28|fdd|asdf|afffff
7|2021-12-28|fdd|asdf|afffff
```

### DB에 있는 값들을 리스트로 가지고 오기

board\board_app\views.py

```python
def index(request):
    #db의 board 테이블의 모든 내용을 가져옴
    rows=board.objects.all()
    content={'rows':rows}
    
    return render(request,'board_app/list.html', content)
```

list.html -> **객체출력**

```html
    <!--템플릿 태그-->
    {{ rows }} <!--인덱스 함수에 설정해놓은 rows 객체를 출력, 쿼리셋을 가져옴-->

    {% for row in rows %}
      <p>{{ row.createDate }}</p>
      <p>{{ row.writer }}</p>
      <p>{{ row.subject }}</p>
      <p>{{ row.content }}</p>
    {% endfor %}
```

표에 적용하기

```html
        <tbody>
          {% for row in rows %}
          <tr>
            <td> {{ forloop.counter }} </td>
            <td> {{ row.createDate }} </td>
            <td> {{ row.writer }} </td>
            <td> {{ row.subject }} </td>
            <td>
              <button type="submit" class="btn btn-warning">수정</button>
            </td>
            <td>
              <button type="submit" class="btn btn-danger">삭제</button>
            </td>
          </tr>
          {% endfor %}
```

![image-20211228152255315](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20211228152255315.png)



### 삭제 버튼

list.html

```html
<form action='delete/', method='POST'>
 {% csrf_token %}
 <input type='hidden' name=id value={{row.id}}>
 <button type="submit" class="btn btn-danger">삭제</button>
</form>
```

views.py

```python
def delete(request):
    #print(request.POST['id'])
    b=board.objects.get(id=request.POST['id'])
    b.delete()
    return HttpResponseRedirect(reverse('list'))
```

urls.py

```python
urlpatterns = [
    path('', views.index, name='list'),
    path('write/', views.index3),
    path('create', views.create),
    path('delete/', views.delete),
]
```

### 수정 버튼

updtae.html 만들기(write와 유사)

```html
    <div class='container'>
      <form action='../modify/' method='POST'> <!--제출하면 넘어가는 페이지 설정,입력한 것을 post 방식으로 서버로 넘김-->
        {% csrf_token %}
        <input type='hidden' name='id' value={{post.id}}>
        <div class="form-group">
          <label for="exampleInputPassword1">작성 날짜</label>
          <input type="date" class="form-control" id='now_date' name='createDate' value="{{post.createDate | date:'Y-m-d'}}"><!--네임변수 꼭 지정해줘야함!!! 그래야 post방식으로 전달 시 변수 사용함-->
         
         
        </div>
        <div class="form-group">
          <label for="exampleInputEmail1">작성자</label>
          <input type="text" class="form-control" placeholder="작성자" name='user' value={{post.writer}}>
        </div>
        <div class="form-group">
          <label for="exampleInputPassword1">글 제목</label>
          <input type="text" class="form-control" name='subject' value={{post.subject}}>
        </div>
        <div class="form-group">
          <label for="exampleInputFile">게시글</label>
          <textarea class="form-control" rows=10 name='content' >{{post.content}}</textarea>
        <button type="submit" class="btn btn-default">수정</button>
      </form>
    </div>
  </body>

</html>
```

list.html

```html
<a href='update/?id={{row.id}}'>
	<button type="submit" class="btn btn-warning">수정</button>
</a>
```

```html
<a href='update/?id={{row.id}}'>  <!--아이디를 url로 보내줌, GET으로 보내줌-->
```

views.py

```python
def update(request):
    # print('id:',request.GET['id'])
    post=board.objects.get(id=request.GET['id'])
    content={'post':post}
    return render(request,'board_app/update.html',content)


def modify(request):
    post=board.objects.get(id=request.POST['id'])
    post.createDate=request.POST['createDate']
    post.writer=request.POST['user']
    post.subject=request.POST['subject']
    post.content=request.POST['content']
    post.save()

    return HttpResponseRedirect(reverse('list'))
```

urls.py

```python
urlpatterns = [
    path('', views.index, name='list'),
    path('write/', views.index3),
    path('create', views.create),
    path('delete/', views.delete),
    path('update/', views.update),
    path('modify/', views.modify),
]
```

### 게시글 내용 보기

urls.py

```python
urlpatterns = [
    path('', views.index, name='list'),
    path('write/', views.index3),
    path('create', views.create),
    path('delete/', views.delete),
    path('update/', views.update),
    path('modify/', views.modify),
    path('view/', views.view),
]
```

views.py

```python
def view(request):
    post=board.objects.get(id=request.GET['id'])
    content={'post':post}
    return render(request,'board_app/view.html',content)
```

view.html 만들기 (update와 거의 동일)

```html
<!DOCTYPE html>
<html>
  <head>
    {% load static %}
    <link type='text/css' rel='stylesheet' href='{% static "bootstrap.min.css" %}' />
    <link type='text/css' rel='stylesheet' href='{% static "bootstrap-theme.min.css" %}' />
    <link type='text/css' rel='stylesheet' href='{% static "list.css" %}' />

  <body>
    <nav class="navbar navbar-inverse navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="/board/">아주 간단한 게시판</a> <!--절대경로 /board/-->
        </div>
        <div id="navbar" class="navbar-collapse collapse">
          <div class="navbar-form navbar-right">
            <button type="submit" class="btn btn-info">Sign in</button>
            <button type="submit" class="btn btn-success">Sign up</button>
          </div>
        </div><!--/.navbar-collapse -->
      </div>
    </nav>

    <hr> <!--가로선-->


    <div class='container'>
      <form> 
        {% csrf_token %}
        <div class="form-group">
          <label for="exampleInputPassword1">작성 날짜</label>
          <input type="date" class="form-control" id='now_date' name='createDate' value="{{post.createDate | date:'Y-m-d'}}" readonly><!--네임변수 꼭 지정해줘야함!!! 그래야 post방식으로 전달 시 변수 사용함-->

        </div>
        <div class="form-group">
          <label for="exampleInputEmail1">작성자</label>
          <input type="text" class="form-control" placeholder="작성자" name='user' value={{post.writer}} readonly>
        </div>
        <div class="form-group">
          <label for="exampleInputPassword1">글 제목</label>
          <input type="text" class="form-control" name='subject' value={{post.subject}} readonly>
        </div>
        <div class="form-group">
          <label for="exampleInputFile">게시글</label>
          <textarea class="form-control" rows=10 name='content' readonly>{{post.content}}</textarea>
          <button type="submit" class="btn btn-default">수정</button>
      </form>
    </div>
  </body>

</html>
```

### 템플릿 상속

base.html

- 모든 페이지가 공통적으로 가지는 코드

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">

    {% load static %}
    <link type='text/css' rel='stylesheet' href='{% static "bootstrap.min.css" %}' />
    <link type='text/css' rel='stylesheet' href='{% static "bootstrap-theme.min.css" %}' />
    <link type='text/css' rel='stylesheet' href='{% static "list.css" %}' />
  </head>

  <body>
    <nav class="navbar navbar-inverse navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="/board/">아주 간단한 게시판</a>
        </div>
        <div id="navbar" class="navbar-collapse collapse">
          <div class="navbar-form navbar-right">
            <button type="submit" class="btn btn-info">Sign in</button>
            <button type="submit" class="btn btn-success">Sign up</button>
          </div>
        </div><!--/.navbar-collapse -->
      </div>
    </nav>

    <hr>

    <!-- 
      템플릿 태그를 삽입
      해당 템플릿 태그 사이에는 개별적으로 표현되는 내용이 들어가게 됩니다. 
    -->
    {% block content %}
    {% endblock %}

  </body>
</html>
```

다른 html들 설정

```html
{% extends 'board_app/base.html' %}
{% block content %}

...

{% endblock %}
```

### 사용자 인증

#### 관리자 -superuser

```
Username (leave blank to use 'user'): admin
Email address:
Password:
Password (again): 
This password is too short. It must contain at least 8 
characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```

127.0.0.1:8000/admin/login 여기에 로그인

#### 일반 계정

```
(multicampus) C:\hw\workspace\board>python manage.py shell
Python 3.10.0 | packaged by conda-forge | (default, Nov 10 2021, 13:20:59) [MSC v.1916 64 bit (AMD64)] on win32Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from django.contrib.auth.models import User
>>> user=User.objects.create_user('user1','','1234')
>>> user.save()
```

#### sign up

signup.html

```html
<!DOCTYPE html>

<html>
  <head>
    {% load static %}
    <!-- bootstrap css 적용 -->
    <link type='text/css' rel='stylesheet' href='{% static "bootstrap.min.css" %}' />
    <link type='text/css' rel='stylesheet' href='{% static "bootstrap-theme.min.css" %}' />
    <link type='text/css' rel='stylesheet' href='{% static "list.css" %}' />
  </head>

  <body>
    <div class='container'>
      <form class='form-horizontal' method='POST' action='../createUser/'>
        {% csrf_token %}
        <div class='form-group'>
          <label for="inputId" class="col-xs-4 col-md-4 control-label">ID</label>
          <div class='col-xs-4 col-md-4'>
            <input class="form-control" type='text' name='id' id='inputId'>
          </div>
        </div>
        <div class='form-group'>
          <label for="inputPw" class="col-xs-4 col-sm-4 control-label">PW</label>
          <div class='col-xs-4 col-md-4'>
            <input class="form-control" type='password' name='pw' id='inputPw'>
          </div>
        </div>
        <div class='form-group'>
          <div class='col-xs-offset-4 col-md-offset-4 col-xs-10 col-md-10'>
            <button class="btn btn-default" type='submit'> 회원가입 </button>
          </div>
        </div>
      </form>
    </div>
  </body>
</html>
```

accounts/views.py

```python
def signin(request):
    return render(request,'accounts/signin.html')

def signup(request):
    return render(request,'accounts/signup.html')

def createUser(request):
    id=request.POST['id']
    pw=request.POST['pw']
    user=User(username=id,password=pw)
    user.save()
    return HttpResponseRedirect(reverse('list'))
```

accounts/urls.py

```python
urlpatterns = [
    path('signin/', views.signin),
    path('signup/', views.signup),
    path('createUser/',views.createUser),

]
```

#### sign in (login)

accounts/urls.py

```python
from board_app import views as board_views
from django.contrib.auth import views as auth_views # 로그인 기능이 설정되어 있음

urlpatterns = [
    path('signin/', auth_views.LoginView.as_view(template_name='accounts/signin.html')),
    path('signup/', views.signup),
    path('createUser/',views.createUser),
    path('profile/',board_views.index),
]
```

signin.index

```html
<!DOCTYPE html>

<html>
  {% load static %}
  <link type='text/css' rel='stylesheet' href='{% static "bootstrap.min.css" %}' />
  <link type='text/css' rel='stylesheet' href='{% static "bootstrap-theme.min.css" %}' />
  <link type='text/css' rel='stylesheet' href='{% static "list.css" %}' />
</head>



...



          <div class='col-xs-4 col-md-4'>
            <input class="form-control" type='text' name='username' id='inputId'>
          </div>
        </div>
        <div class='form-group'>
          <label for="inputPw" class="col-xs-4 col-sm-4 control-label">PW</label>
          <div class='col-xs-4 col-md-4'>
            <input class="form-control" type='password' name='password' id='inputPw'>

```



#### 로그인, 로그아웃 후 board로 이동하고 싶으면?

settings.py

```python
#로그인 이후에 이동할 URL
LOGIN_REDIRECT_URL='/board/'

# 로그아웃 이후 이동할 url
LOGOUT_REDIRECT_URL='/board/'
```

#### 로그인 후에 게시글 작성하게 만들기

views.py

```python
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

from board_app.models import board


# Create your views here.

def index(request):
    #db의 board 테이블의 모든 내용을 가져옴
    rows=board.objects.all()
    content={'rows':rows}
    
    return render(request,'board_app/list.html', content)

def index3(request):
    return render(request,'board_app/write.html')


from django.contrib.auth.decorators import login_required
# 데코레이터를 이용해 로그인이 필요한 함수라는 것을 정의함
@login_required(login_url='/accounts/signin/') #로그인 안되어있으면 로그인페이지로 이동
def create( request):
    new=board(
        createDate=request.POST['createDate'],
        user=request.user,
        subject=request.POST['subject'],
        content=request.POST['content'],
    )
    new.save()
    return HttpResponseRedirect(reverse('list'))
    # return HttpResponset('게시글을 작성합니다')

@login_required(login_url='/accounts/signin/')   
def delete(request):
    #print(request.POST['id'])
    b=board.objects.get(id=request.POST['id'])
    b.delete()
    return HttpResponseRedirect(reverse('list'))

@login_required(login_url='/accounts/signin/')
def update(request):
    # print('id:',request.GET['id'])
    post=board.objects.get(id=request.GET['id'])
    content={'post':post}
    return render(request,'board_app/update.html',content)

@login_required(login_url='/accounts/signin/')
def modify(request):
    post=board.objects.get(id=request.POST['id'])
    post.createDate=request.POST['createDate']
    post.writer=request.POST['user']
    post.subject=request.POST['subject']
    post.content=request.POST['content']
    post.save()

    return HttpResponseRedirect(reverse('list'))

def view(request):
    post=board.objects.get(id=request.GET['id'])
    content={'post':post}
    return render(request,'board_app/view.html',content)

```

#### 허용된 사용자만 수정 삭제 가능하게 하기

alert.html 만들기

```html
<!DOCTYPE html> 

<html>
    <body>
        <script>
            alert('권한없는 요청');
            location.href='/board/';
        </script>
    </body>
</html>
```

board_app/views.py

```python
from django.contrib import messages
@login_required(login_url='/accounts/signin/')
def modify(request):


    post=board.objects.get(id=request.POST['id'])
    if request.user != post.user:
        return render(request,'board_app/alert.html')
    else:
        post.createDate=request.POST['createDate']
        post.writer=request.POST['user']
        post.subject=request.POST['subject']
        post.content=request.POST['content']
        post.save()

        return HttpResponseRedirect(reverse('list'))
```

### 관리자 변경

board_app\admin.py

```python
from django.contrib import admin
from .models import board

# Register your models here.

class BoardAdmin(admin.ModelAdmin):
    #관리자 페이지에서 화면에 보여지는 목록
    list_display=('createDate','user','subject')
    
    #링크 새로 정의(제목 클릭해서 상세페이지로 이동)
    list_display_links=['subject']

admin.site.register(board, BoardAdmin)
```

