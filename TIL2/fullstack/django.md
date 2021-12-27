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





# 실습

## URL 연결하기

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



## STATIC 

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
```

**글 제목만 얻고 싶다? - 루프문 사용**

```
>>> for b in board.objects.all():
...     print(b.subject)
... 
hello
hello
>>>
```

**원하는 객체 하나 뽑아오기**

```
>>> board.objects.get(id=1)
<board: board object (1)>
```

