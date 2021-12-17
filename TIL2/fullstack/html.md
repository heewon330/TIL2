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