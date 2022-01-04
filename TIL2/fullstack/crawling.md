# 크롤링

## 라이브러리 이용한 크롤링

### urllib

```python
import urllib.request

url='url'

request=urllib.request.Request(url)
response=urllib.request.urlopen(request)
print(response.read().decode())
```

#### 사진 파일 크롤링

```python
import urllib.request

url='사진경로'

urllib.request.urlretrieve(url,'')
```

#### 사진 저장

```python
import urllib.request
from fake_useragent import UserAgent

agent = UserAgent()

# urllib은 urlretrieve함수를 이용해서 한 번에 파일로 저장
url = '사진경로'

# 파일을 저장할 경로
path = 'web/data/download.jpg'
# opener 객체를 생성해서 헤더를 수정을 먼저 해줍니다.
opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', agent.chrome)]
urllib.request.install_opener(opener)
urllib.request.urlretrieve( url, path )
```

보안문제만 없다면 이렇게 간단하게 가능

```python
import urllib.request

# urllib은 urlretrieve함수를 이용해서 한 번에 파일로 저장
url = '사진경로'
path = 'web/data/download2.jpg'
urllib.request.urlretrieve( url, path ) # urlretrieve를 통해 사진을 바로 저장
```

### requests 이용한 크롤링

#### requests 설치

```
>>>pip install requests
```

#### 크롤링

```python
import requests

url='url'
response=requests.get(url)
print(response.text)
```

#### 파일 저장 

- 바이너리 형태로 파일 객체를 생성 및 저장
- 0과 1로 이루어진 형태

```python
import requests
from fake_useragent import UserAgent

agent = UserAgent()
header = {'User-Agent':agent.chrome}

url = '사진경로'

response = requests.get(url, headers=header)

with open('web/data/download4.jpg','wb') as file:
    file.write(response.content)
```

# 스크래핑

- 원하는 정보만 가져오기(파싱)
- 영화 리뷰 이용해보기
  - 내가 원하는 리뷰를 파싱해오기

```python
import requests

url = 'https://movie.naver.com/movie/point/af/list.naver'
#일단 영화평점 페이지 주소를 크롤링 함
response=requests.get(url)
print(response.text)
```

## BeatifulSoup 라이브러리

bs4 설치 

```
>>>pip install bs4
```

css 셀렉터 이용해 원하는 요소 검색 가능

```python
import requests
import bs4

url = 'https://movie.naver.com/movie/point/af/list.naver'
#일단 영화평점 페이지 주소를 가져옴
response=requests.get(url)
html=response.text
review=bs4.BeautifulSoup(html)
```

```python
type(review) #bs4.BeautifulSoup
```

### bs4 이용한 파싱

#### find

- 일치하는 태그 요소들을 찾아줌
- 태그가 여러개인 경우 제일 처음 위치하는 태그를 반환

```python
review.find('a') 
```

```python
import requests
import bs4

url = 'https://movie.naver.com/movie/point/af/list.naver'
response = requests.get(url)
html = response.text
review = bs4.BeautifulSoup(html)

# 리뷰만 확인
search = {
  'class':'title'
}
td_elements = review.find_all('td', attrs=search)

for element in td_elements:
  print( element.text.split('\n')[5] )
```

제목, 평점, 리뷰 뽑아오기

```python
import requests
import bs4

url = 'https://movie.naver.com/movie/point/af/list.naver'
response = requests.get(url)
html = response.text
review = bs4.BeautifulSoup(html)

# 리뷰만 확인
search = {
  'class':'title',
}
td_elements = review.find_all('td', attrs=search)

for element in td_elements:
    title=element.find('a').text
    score=element.find('em').text
    r=element.text.split('\n')[5]
    print(f'영화제목: {title}')
    print(f'평점: {score}')
    print(f'리뷰: {r}')
```

모든 페이지(~10페이지)의 리뷰를 가져오기 위해선

```python
search = {
  'class':'title'
}
for no in range(1, 11):
  url = f'https://movie.naver.com/movie/point/af/list.naver?&page={no}'
  response = requests.get(url)
  html = response.text
  review = bs4.BeautifulSoup(html)
  
  td_elements = review.find_all('td', attrs=search)

  for element in td_elements:
    title = element.find('a').text
    score = element.find('em').text
    r = element.text.split('\n')[5]
    print(f'영화제목: {title}')
    print(f'평점: {score}')
    print(f'리뷰: {r}')
```

#### select

- find와 비슷

```python
import requests
import bs4

url = 'https://movie.naver.com/movie/point/af/list.naver'
response = requests.get(url)
html = response.text
review = bs4.BeautifulSoup(html)
```

css 셀렉터가 사용됨

```python
review.select('td.title')
```

## selenium 이용한 크롤링

```python
#쇼핑몰 후기-옥션
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service


options=webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-logging'])
# webdriver -> 직접 브라우저 제어
# 크롬 기준으로 버전 맞춰서 다운로드
service=Service(executable_path="c:\\hw\\workspace\\chromedriver.exe")
browser=webdriver.Chrome(service=service, options=options)

url = 'http://www.naver.com'
#browser.get(url)

#FT쌤 설명
#executable_path = "./chromedriver.exe"
#browser = webdriver.Chrome(executable_path = executable_path)
 
browser.get(url)

element = browser.find_element(By.CSS_SELECTOR, 'input#query')
```

검색어 입력 후 엔터

```python
element.send_keys('검색어')
element.send_keys('\n')
```

```python
#검색어 입력 후 마우스 클릭
# 클릭 가능한 요소라면 클릭이 가능
input = browser.find_element(By.CSS_SELECTOR, 'input#query')
button = browser.find_element(By.CSS_SELECTOR, 'button#search_btn')
input.send_keys('검색어')
button.click()
```

새로운 입력어 검색 시

```python
input = browser.find_element(By.CSS_SELECTOR, 'input#query')
button = browser.find_element(By.CSS_SELECTOR, 'button#search_btn')
input.send_keys('검색어')
button.click()

input2 = browser.find_element(By.CSS_SELECTOR, 'input#nx_query')
input2.clear()
input2.send_keys('두번째 검색어')
```

### 옥션 사이트 스크래핑

```python
#쇼핑몰 후기-옥션
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# webdriver -> 직접 브라우저 제어
# 크롬 기준으로 버전 맞춰서 다운로드
service=Service(executable_path="c:\\hw\\workspace\\chromedriver.exe")
browser=webdriver.Chrome(service=service, options=options)

url = '옥션사이트'

browser.get(url)

review_button = browser.find_element(By.CSS_SELECTOR, 'li#tap_moving_2 a')
review_button.click()


elements = browser.find_elements(By.CSS_SELECTOR,'ul.list__review p.text')
for element in elements:
    print(element.text)
```

### mlp 스크래핑

```python
#mlp
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

url = 'mlp사이트'
browser.get(url)

time.sleep(10) #페이지 로딩되는 시간을 더 길게 설정- 2초동안 대기
#inputs=browser.find_elements(By.CSS_SELECTOR,'div.input-row-line input')
#inputs[0].send_keys('아이디')
#inputs[1].send_keys('비번')

#inputs=browser.find_elements(By.CSS_SELECTOR,'div.btn-row button.login-btn')
#loginButton = browser.find_element(By.CSS_SELECTOR, 'div.btn-row button.login-btn')
#loginButton.click

#무한 스크롤 - 모든 내용을 스크래핑하고 싶을때
last_height=browser.execute_script('return document.body.scrollHeight') #초기 스크롤높이
while True: #무한반복
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight);') #스크롤높이만큼 내려줌
    time.sleep(2) #로딩되는 동안 기다려줌
    new_height=browser.execute_script('return document.body.scrollHeight') # 새로운 높이 재기

    #새로운 높이가 이전과 같을 경우 더 이상 내려갈 수 없음
    if new_height == last_height: break
    last_height = new_height
    
# 로드된 내용들을 수집
articles = browser.find_elements(By.CSS_SELECTOR, 'div.feedlist span article')
for article in articles:
  for content in article.find_elements(By.CSS_SELECTOR, 'span.feedContentBlk span'):
    print( content.text)
```