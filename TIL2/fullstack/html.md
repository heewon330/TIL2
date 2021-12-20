# 웹프로그래밍 개발 환경

- JavaScript로 프론트앤드 구축 많이 함

- sample.html -> `! + tab`

  

## 웹 동작 방식

1. HTTP(Hyper-Text Transfer Protocol)
   - HTML에서 만든 소스코드 or 텍스트를 브라우저에 전송해서 화면에 표현함,`랜더링` 

2. HTML(Hyper-Text Markup Language)
   - 하이퍼-텍스트로 이루어진 소스코드
   - 마크업 언어 : <,>로 이루어진 텍스트



- 프론트 앤드 / 백앤드
  - 프론트 앤드 : 웹브라우저에서 실행(HTML,CSS,JavaScript)
    - 소스코드를 모두 다운로드 받아서 실행하기 때문에 코드가 전부 공개되어 있음
  - 백 앤드 :  서버에서 실행
    - 코드가 공개되어 있지 않음
    - 브라우저에서 확인 가능한 것은 서버에서 실행하고 난 후에 반환된 값
    - 자바의 스프링, 파이썬의 장고,루비의 레일즈 등



## HTTP

- 네트워크 전송 규약 
  - 하이퍼 텍스트를 주고 받기 위한 네트워크 표준
- HTTP 이해 = 헤더를 이해하는 것

### 소켓 프로그래밍

- 네트워크를 통한 입/출력 통신을 하기 위한 프로그래밍 - 소켓을 이용한 통신
- TCP 소켓 

```
import socket

# 네트워크 통신을 하기 위한 소켓 객체 생성
# IPv4를 이용한 TCP 통신용 소켓이란 뜻
# 생성된 소켓 객체를 통해 서버와 통신(입/출력)이 가능
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print('DEBUG:::소켓 생성 완료')

#파일 입/출력 할 때 open을 통해서 입/출력하기 위 한 파일 객체를 얻어온 것처럼
# 통신(입/출력)하기 위한 서버와의 객체를 생성
# 소켓 프로그래밍에서는 connect()를 통해서 통신하기 위한 서버의 객체를 얻어올 수 있음
# 생성된 객체를 통해 입/출력(통신) 가능

#읽거나 쓰기 위한 파일의 경로와 유사
#통신하기 위한 네트워크 상의 경로 
serverAddress = socket.gethostbyname('info.cern.ch')
serverPort=80

sock.connect((serverAddress, serverPort))
print('DEBUG:::connect 완료')

#서버에 HTML 코드 요청 => Request Header
#대소문자 띄어쓰기 주의
# 이 header 부분이 중요!!!!!!!!!!!!!
request_header= 'GET /index.html HTTP/1.1\r\n'
request_header += 'Host: info.cern.ch\r\n'
request_header += '\r\n'

#요청대로 처리가 되어서 HTML 코드가 잘 다운로드 되는지 확인
sock.send(request_header.encode())
response = sock.recv(1024)
print(response.decode())


# 생성된 소켓을 닫아줌
sock.close()  #문제를 최소화하는 방향..
```

### Request Header

- 요청 헤더
  - 오타 하나라도 있으면 통신 불가!!!!

```
GET /index.html HTTP/1.1\r\n 
-----------------------------
start-line(request-line) CRLF
#이 줄 해석이 제일 중요


Host: info.cern.ch\r\n
---------------------------
헤더 필드: *

\r\n
-----
여기서의 CRLF :헤더의 끝을 의미
```

** **CRLF**= 뉴라인(줄바꿈)- HTTP 헤더에서는 `구분자`의 의미를 가짐

->라인과 라인, 필드와 필드를 구분해주는 구분자의 역할

** **헤더 필드** : 서버와의 동시에 필요한 여러 정보를 표현

->'post'필드 이외에도 많은 값을 가질 수 있음



http://info.cern.ch/ 에서 확인

*header들*(몇개만~)

Accept : 이 브라우저가 처리할 수 있는 파일 형태

Accept-Encoding : 이 브라우저가 처리할 수 있는 형태

등등 헤더는 많이 존재함~



#### request-line

```
GET           sp          /index.html       sp         HTTP/1.1              \r\n 
---			-----		 -------------				  -----------			--------
method		 공백				URL(URI)				 protocol ver		     sep
```

- 3개의 필드 -> 각 필드의 구분자는 `sp(공백)`  **!!규칙이므로 오타 주의!!**

##### method

*요청 메시지 종류들*

- get :  응답헤더 + HTML 코드 둘다 전달해줌. 클라이언트가 서버에게 URL에 해당하는 자료 전송을 요청
- head : 헤더만 전달해줌
- post : 클라이언트가 서버에서 처리할 수 있는 자료를 보냄
- options 

##### URL/URI 

- 리소스 접근 방식, 경로 표현
- Uniform Resource Locator : 네트워크 상에서 접근하려는 리소스(파일)의 경로
  - 요즘 잘 안씀, 보안 상 취약
- Uniform Resource Identifier : URL과 동일한 경로 표현이지만 뭐에 접근하려는지 알 수 없음, 파일 정보 노출이 안되어 있음.
  - 식별자를 적어놓으면 백앤드 측에서 식별자에 맞는 리소스를 반환해줌

### Request Header

```
HTTP/1.1 200 OK
Date: Fri, 17 Dec 2021 07:39:53 GMT
Server: Apache
Last-Modified: Wed, 05 Feb 2014 16:00:31 GMT
ETag: "286-4f1aadb3105c0"
Accept-Ranges: bytes
Content-Length: 646
Connection: close
Content-Type: text/html
```

```
HTTP/1.1 200 OK\r\n
----------------
start-line(response-line) CRLF  여기 해석이 제일 중요!!


Date: Fri, 17 Dec 2021 07:39:53 GMT\r\n
Server: Apache\r\n
Last-Modified: Wed, 05 Feb 2014 16:00:31 GMT\r\n
ETag: "286-4f1aadb3105c0"\r\n
Accept-Ranges: bytes\r\n
Content-Length: 646\r\n
Connection: close\r\n
Content-Type: text/html\r\n
---------------------------------------------
header-field: *


\r\n
-----
헤더의 끝
```

#### response-line

- 클라이언트의 요청에 대한 처리 결과를 나타내줌

```
HTTP/1.1 	sp 		200		sp		 OK\r\n
---------			----			--------
protocol ver	  status code(중요!)   status string
```

- 3개의 필드로 구성 - 구분자는 공백(sp)
- 상태코드(status code)의 해석이 제일 중요
  - 1XX 
  - 2XX : 서버가 요청을 수락했음
    - 200 OK : 클라이언트 요청을 수락했고 처리가 잘 되었음
  - 3XX : 요청에는 문제가 없지만, 요청에 대한 optional한 처리
    - 304 Not Modified : 요청된 리소스가 변경되지 않았음
    - 301, 302 : Redirection과 관련
      - 영구이동, 임시이동과 관련됨
      - 지금 요청한 리소스의 위치가 바뀐 경우 새로운 위치를 알려줄 때
  - **4XX** : 클라이언트 요청 오류 - 요청에 문제가 있는 경우
    - 400 Bad Request : 오탈자, 없는 리소스
    - 401 Unauthorized, 403 Forbidden : 권한과 관련됨
      - 401:인증키 없는 경우
      - 403:인증키와 상관 없이 해당 리소스에 대한 접근 권한이 없는 경우
    - 404 Nof Found : 리소스 못 찾는 경우, 없는 리소스
  - **5XX** : 서버 에러 - 요청 처리하다가 서버에서 오류가 난 경우
    - 500 Internal Server Error : 예를 들어 파이썬 코드에 문제 발생 시 



**START LINE 해설이 매우 중요**



## HTML

- Hyper-Text Markup Language
- 문서의 구조를 표현. 제어문이 없음
- `자바스크립트`가 이 부족한 부분을 대신함

### 기본 구조

```html
<!DOCTYPE html>   <!-- HTML5 표준을 따르는 문서라는 뜻 -->
<html>            <!-- HTML 문서의 시작, 태그라고 불림 -->
    
    <!-- 
		화면에 보이지 않는 내용들
		주로 HTML 문서의 정보에 대한 내용들
	-->
    <head>   


    </head>
    
	<!--
		화면(웹 브라우저)에 보여지는 모든 내용들
	-->
    <body>
        
    </body>
</html>           <!-- HTML 문서의 끝-->
```

### TAG

- `<,>`를 이용해 표현
- 내용(컨텐츠)에 대한 타입을 나타냄

```html
<opening tag> 내용 </closing tag>
<tagName/> self closing :내용이 없는 경우
```

- HTML은 상위 태그와 하위 태그로 `중첩된 구조`로 형성되어 있음, 계층적인 구조
  - 최상위 태그는 `HTML`, `head`와 `body`는 하위 태그
  - 들여쓰기로 표현

#### 기본 태그

- 문서의 구조 표현
- 워드, 한글 이용해서 작성 가능한 내용 : 제목, 본문, 표, 그림, 목차 등
- 현재는 다양한 형태로 응용됨

#### 속성(Attribute)

1. 일반 속성

- 속성에 따라 사용 가능한 태그가 다름

2. **글로벌 속성**

- 모든 태그에서 공통적으로 사용할 수 있는 속성
  - class, id, hidden , ...
- 이벤트 속성
- 스타일 속성

#### Heading

- 제목 표현, 6단계 <h1>~<h6>
- body의 하위 태그

```html
<!DOCTYPE html>
<html>
    <head>

    </head>

    <body>
    	<h1> 가장 큰 제목 </h1>
    	<h3> 중간 제목 </h3>
    	<h5> 소제목 </h5>
        
    </body>
</html>
```

#### Paragraph

- 문단, 본문, 단락 등을 표현, 문자를 표현할 때 사용

```html
<!DOCTYPE html>
<html>
    <head>

    </head>

    <body>
        <h1> 가장 큰 제목 </h1>
    	<h3> 중간 제목 </h3>
    	<h5> 소제목 </h5>
        
        <p> 
            일반적으로 텍스트를 표현하는 용도로 사용.
            태그 안에 있어도 CRLF는 적용되지 않음
        </p>
        그치만 텍스트를 반드시 p 태그에 넣지 않아도 출력이 됨.
        HTML은 줄바꿈(엔터) 문자로 CRLF 사용 안함. 
        줄바꿈 안됨
        
        <p>공백               해석 불가</p>
    </body>
</html>
```

- 브라우저는 CRLF를 해석하지 않음
- 공백 문자도 해석하지 않음



- Line Break
  - html은 엔터도 태그로 표현
  - `<br>` 태그
- Non-breaking Space
  - `&nbsp;`, `&ensp;`, `&emsp;`
  - 공백 대신에 사용하는 공백 문자. 문자열 이스케이프 정도로 해석



#### 리스트

- 목차, 목록 등을 표현, 기본 태그의 응용된 버전으로 생각
- 정렬된 리스트 : Ordered List ->  `<ol>`
- 비정렬 리스트 : Unordered List  ->  `<ul>`

```html
        <ol> 순서 있는  리스트  <!--아라비아 숫자 넘버링-->
            <li> 첫번째</li>
            <li> 두번째</li>
            <li> 세번째</li>
        </ol>
        <ul> 순서 없는  리스트
            <li> 첫번째</li>
            <li> 두번째</li>
            <li> 세번째</li>
        </ul>
```

#### 이미지

- `<img>`, 내용이 없는 태그 중 하나
  - 셀프 클로징을 한다는 뜻
- 이미지의 주소를 속성에 입력 (저작권 주의~~)

```html
<img src='url/path' /> 
```

- 'height','width' 속성 : 사진 크기 조절, 픽셀 단위

```html
<img src='url/path' width='10', height='px' /> 
```

#### 테이블

- 표
- 테이블을 이용해 웹 페이지 레이아웃을 표현, div를 많이 사용

```html
<table>		<!--테이블의 시작-->
    <thead> <!--제목 라인-->
        <tr> <!--행, table row-->
            <th></th> <!--컬럼-->
        </tr>
    </thead>
    
    <tbody> <!--표에 들어갈 내용-->
        <tr> <!--1행, table row-->
            <td></td> <!--컬럼, table data-->
        </tr>
    </tbody>
</table>	<!--테이블의 끝-->
```

#### anchor

- 하이퍼 링크
  - 지금의 웹이 만들어지는 데 가장 중요한 기능
  - 봇(bot) - 자동화된 프로그램, 웹 페이지 자동 수집을 할 때 사용됨
    - 시드(seed) 페이지를 통해 하이퍼-링크를 통해서 연결되어 있는 다른 웹 페이지를 찾는 방식

```html
<a> 연결된 페이지의 이름 </a>
```

- 속성
  - href : 연결된 페이지 주소(URL/URI)
  - target : 연결된 페이지로 이동
    - **_self** : 디폴트값, 현재 창에서 해당 페이지로 바로 이동
    - **_blank** : `새 창`을 열어 해당 페이지로 이동
    - _parent : 현재 창보다 상위 창에서 해당 페이지로 이동
    - _top : 최상위 창에서 해당 페이지로 이동

### HTML Box Model

- 태그들은 배치되는 형태에 따라 두 가지로 분류 (어떤 태그를 사용하느냐에 따라 레이아웃이 결정됨)
  - **Block 기반의 태그**
  - **Inline 기반의 태그**

#### Block 기반의 태그

- 특징
  - 한줄에 하나씩 배치됨

- **DIV** = `익명태그`
  - 용도가 정해져 있지 않은 태그, 활용성 높아서 많이 사용
- 그 외의 태그들
  - p, ol, ul, li, table, h 등

```html
<!DOCTYPE html>
<html style='border:0.5px dashed blue'>
    <head>

    </head>

    <body style='border:0.5px dashed red'>

        <!--블록기반의 태그들-->
    	<h1 style='border:0.5px dashed green'> Heading </h1>
        <p style='border:0.5px dashed yellow'> Paragraph</p>
        
        <div style='border:0.5px dashed black; width:100px; height:100px'>
        </div>
        <div style='border:0.5px dashed black; width:100px; height:100px'>
        </div>
        <div style='border:0.5px dashed black; width:100px; height:100px'>
        </div> <!--박스모델-->
    </body>
</html>
```

- border : 경계선(테두리)
  - 선의 굵기가 0.5px, 경계가 점선이고 컬러 지정

#### Inline 기반의 태그

- 특징
  - 한 줄로 배치가 됨
  - 한 줄에 전부 보여지지 않는다면 다음 줄로 넘어감

- `<span>` : 'div'와 마찬가지로 `익명태그` 중 하나, inline 기반인 것이 차이점
- 그 외의 태그
  - img, a, ...

```html
        <!--인라인 기반의 태그들-->
        <span style='border:0.5px dashed purple; width:100px; height:100px'>
            span1
        </span>
        <span style='border:0.5px dashed purple; width:100px; height:100px'>
            span2
        </span>
        <span style='border:0.5px dashed purple; width:100px; height:100px'>
            span3
        </span>
```

### 레이아웃

- **div 통해서 배치** / **semantic tag 사용해 배치** / table 이용해 배치(지금 표준으로는 사용 안함)

#### iframe

- inline frame의 약자, 웹페이지 안에 또 다른 웹페이지를 표현

```html
 <iframe src='https://www.daum.net'></iframe> <!--다음 페이지 삽입-->
```

#### semantic tag

- HTML5 표준부터 새로 만들어진 태그
- 레이아웃만을 위한 태그. 각각이 의미를 가지고 있는 태그

- 레이아웃을 나타내는 시맨틱 태그
  - header, nav, main, section, article, asise, footer



### 입력 태그

- 사용자로부터 웹 페이지를 입력 받아서 서버에 전달하기 위한 용도

#### form

- POST 방식으로 서버에 데이터를 전달, 로그인 할 때 가장 많이 사용됨

```html
<form action='' method=''>
    <!--여러 입력 태그들이 올 수 있음 -->
</form>
```

- 속성
  - **action** : 입력 데이터를 처리할 서버(백앤드/웹어플리케이션)의 URL
  - **method** : 데이터를 전달하는 방법(GET/POST)
    - GET 방식 : URL/URI 통해서 전달 -> URL 주소 뒤에다가 표현, 쇼핑몰에서 많이 보임 ->데이터가 매우 쉽게 외부에 노출되어 보안에 취약한 점이 단점
    - POST 방식 : 데이터를 별도의 방식으로 전달 -> 암호화가 되어있기 때문에 외부에 쉽게 노출이 되지 않음
      - 암호화된 통신(https)

#### input

- 입력받고자 하는 형태를 정의
  - text, radio button, checkbox, select, button, submit 등 매우 많음

```html
    <input type ='text'>
    <select>
        <option value='첫번째'>1</option>
        <option value='두번째'>2</option>
        <option value='세번째'>3</option>
    </select>
    <input type='hidden' /> <!--안보이는 속성-->

    <input type='button' value='버튼'/>
    <input type='submit' value='제출'/> <!--폼을 만들었을 때 서브밋이 있어야 전송 가능-->
```

- 속성
  - **name** : 각 입력요소를 구분하는 중요한 요소, 데이터를 서버에 전달 시 변수의 이름으로 사용하므로 정의 필수





## CSS

- CaseCade Style Sheet
- html 홈페이지 꾸밀 때 사용

1. inline style : 태그 안에 'style' 속성을 이용

```html
 <body style='border:5px dashed red'><!--inline 형태-->
```

잘 사용하지 않음, 우선순위가 높기 때문

2. internal style

```html
        <style>
            body {border:2px dashed blue'} <!--internal 형태-->
        </style>
```

3. **external style**

- 이것만 사용하면 됨
- css 파일을 따로 만들어서 링크를 달아 놓음, 외부 스타일 시트를 이용해서 css 적용
- 스타일 시트 파일을 html 페이지에 가져와서 적용하는 방법

```html
 <link rel='stylesheet' type='text/css' href='../css/style.css' /> <!--리눅스 형태의 경로 표현-->
```

### CSS 구조

```css
선택자(selector) {
    속성이름1:속성값1 속성값2 속성값3 ...;
    속성이름2:속성값1 ...;
    
}
```

- 선택자: 스타일을 적용할 태그
- 속성과 속성은 `;`으로 구분됨
- 속성과 속성값은 `:`으로 구분
- 속성값이 여러개인 경우 `(공백)` 으로 구분

#### 글자와 관련된 속성들

- 상속 : CSS 속성이 부모 태그에서 자식 태그로 상속되어 동일한 속성이 적용됨
  - 무조건 상속은 안됨
  - 글자와 관련된 속성들은 상속이 가능한 대표적인 속성이라고 볼 수 있음

```css
html{
    border: 3px dashed blue;
}
```

html과 관련이 있는 모든 곳은 같은 속성을 갖게 됨

```css
html{
    font-size:20px;
    font-family: 글꼴;
}
```

단, 사용할 글꼴이 로컬에 설치가 되어 있어야 함 

- 여러 글꼴을 설정함(저장이 안되어있을 것을 대비)
- 전부 없을 땐 기본 글꼴이 사용될 수 있도록 설정
- serif, sand-serif,monospace 등등 
- 아니면 메모장에 있는 글꼴 가져와도 됨

```css
html{
    border: 3px dashed blue;
    font-size:20px;
    font-family:'굴림체',' 나눔고딕코딩', 'serif', 'sans-serif';
    line-height: 2;
    color: #006400; /*글자 색, rgb 색상 넣어줘도 됨 */
    background-color:black; /*배경색*/
}
```

#### Selector (!!매우중요!!)

- CSS-Selector
  - 원하는 태그에 스타일을 정확히 적용하는 방법
  - CSS 외에 다른 곳에서도 동일한 셀렉터를 지원
- `태그 셀렉터`,`id 셀렉터`,`class 셀렉터` 등이 많이 쓰임

##### 전체 선택자

- **`*`:와일드 카드**
- html 내의 모든 태그를 선택

```css
*{
    ...
}
```



##### 태그 선택자

- 태그 이름으로 선택, 동일한 모든 태그에 전부 적용됨

```css
태그이름 {
    ...
}
```

##### ID 선택자

- id 속성을 이용

```css
#id속성값{
    ...
}
```

##### 클래스 선택자

- 'class' 속성을 이용

```css
.class속성값{
    ...
}
```

id 속성은 유일한 값을 가져야 하며, class 속성은 중복 가능한 값을 가질 수 있음

-> 두 속성 동시에 가질 수도 있음

##### 그룹 선택자

- 여러개의 선택자를 동시에 사용(콤마로 구분)

```css
선택자, 선택자, 선택자, ...{
    ...
}
```

##### 하위 선택자

- 태그들이 계층구조를 이용해서 선택. 공백으로 표현됨
  - 선택자1 sp 선택자2 ->선택자1의 하위 선택자2
  - 어떠한 하위 태그들 다 포함 가능함

```css
상위선택자 하위선택자 {
    ...
}
```

##### 자식 선택자

- 하위 선택자와 마찬가지로 계층구조를 이용, `>`로 표현됨
- `직계 자손`: 바로 밑에 하위 태그만 자식으로 인정

```css
상위선택자>하위선택자{
    ...
}
```

- 우선순위 : **id 선택자 > class 선택자 > 태그 선택자**

### box-model

- html에서 태그는 영역을 상자로 표현 가능. 이를 '박스모델'
- 속성
  - margin
    - margin-left
    - margin-right
    - margin-top
    - margin-bottom
  - border
  - padding
    - padding-left
    - padding-right
    - padding-top
    - padding-bottom

![](C:\Users\user\Desktop\KakaoTalk_20211220_170623094.jpg)

```css
.column3 {
    border:5px solid blue;
    margin: 50px; /*top, bottom, left,right 모두 동일한 여백의 margin을 줌*/
    padding:50px; /*동일한 여백의 패딩*/
}
```

### 실습

```css
.title {
    display: inline;
}

.list{
    display: inline;
    position: absolute;
    left:500px;
    bottom:15px;

}

.list-item {
    display: inline; /*원래는 속성이 block이었음*/
}

.container{
    border:1px dashed blue;
    position: relative; /*태그의 위치를 설정. */
    
}

.span {
   /* position: static; 원래 기본값이 스테틱이라 변경되는 건 없음*/
  /* position: relative; 원래 자기 자신 위치에서 변경*/
   position : absolute; /*상위 태그가 static이면 안되므로 container를 변경*/
   top:30px;
   left: 180px;
}
```

