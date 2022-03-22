# 개발일지
- 매일 오후 4시 전까지 업데이트 할 수 있도록

# 2022년 03월 08일

## 개발

## 회의
- 자기소개

- 조장 선정

- 주제 선정 회의

  - 패션

    - 관련 url

      [데이콘](https://dacon.io/competitions/official/235672/overview/description)

      [캐글_H&M](https://www.kaggle.com/c/h-and-m-personalized-fashion-recommendations)

      [슬라이드쉐어](https://www.slideshare.net/BOAZbigdata/15-boaz-marketin)

    - 의견

      - 소비자들이 샀던 옷들, 사진파일
      - 정확한 트렌드와 패션 상품별 수요 예측

  - 음악

    - 관련 url

      [슬라이드쉐어](https://www.slideshare.net/BOAZbigdata/15-boaz-251045079)

      [카카오아레나](https://arena.kakao.com/c/8/data)

      [관련예시](https://pearlluck.tistory.com/473?category=948498)

    - 의견

      - 상황 or 조건에 맞는 음악 추천
      - 웹서비스, DB구축 / 모델링,예측,서비스 구축

  - 농산물

    - 관련 url

      [데이콘](https://dacon.io/competitions/official/235801/overview/description)

      [농넷사이트](https://www.nongnet.or.kr/index.do)

    - 의견

      - 농산물 가격 예측, 농넷 페이지 개선
      - 대체 식품 추천까지?

  - 재난 트윗

    - 관련 url

      [캐글](https://www.kaggle.com/c/nlp-getting-started)

      [예시]([https://nurilee.com/2020/09/12/disaster-tweet-%EC%BD%94%EB%93%9C-%EB%B6%84%EC%84%9D-1%ED%8E%B8-%EB%8D%B0%EC%9D%B4%ED%84%B0-%ED%83%90%EC%83%89/](https://nurilee.com/2020/09/12/disaster-tweet-코드-분석-1편-데이터-탐색/))

    - 의견

      - 트위터에서 재난 트윗들 text 분석

  - 쇼핑

    - 관련 url

      [카카오아레나](https://arena.kakao.com/c/1)

      [화장품리뷰]([https://tantara.medium.com/%EC%B9%B4%EC%B9%B4%EC%98%A4-%EC%95%84%EB%A0%88%EB%82%98-%EC%87%BC%ED%95%91%EB%AA%B0-%EC%83%81%ED%92%88-%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC-%EB%B6%84%EB%A5%98-%EB%8C%80%ED%9A%8C-%EB%A6%AC%EB%B7%B0-n%EC%A4%84-%EC%9A%94%EC%95%BD-c04e6e9d2606](https://tantara.medium.com/카카오-아레나-쇼핑몰-상품-카테고리-분류-대회-리뷰-n줄-요약-c04e6e9d2606)https://www.slideshare.net/BOAZbigdata/15-boaz-251044971)

    - 의견

      -  수집할 데이터가 많다 / 네이버나 다음쇼핑 ssg , 범위가 너무 큼, 댓글분석, 추천, 가격예측 어느 방향으로? 

  - 영화

    - 관련 url

      [영화리뷰](https://www.slideshare.net/BOAZbigdata/13-boaz-1-242107172?qid=91fee2b1-d863-4231-a12a-657e880fde92&v=&b=&from_search=31)

    - 의견

      -  리뷰로 스포리뷰 찾기

## 이슈 
- 임종혁 강사님 방문 후 피드백 정리
  - 패션
    - 브랜드 마다 신체치수가 달라 문제가 있을 수 있다, 사이즈에 대한 기준이 불명확
  - 음악
    - 엔지니어링, 사이언스 잘 나눠서 할 수는 있을듯…어려움?
  - 농산물
    - 스마트팜? 스마트팜관련 가상의 관리 시스템 제안
  - 재난
    - 재밌을 것같은데 어렵다
  - 댓글분석으로 가면 이런건 어떨지?
    - 리뷰로 맛집찾기, 악의적인 리뷰찾기, 돈받고 쓴건지 찐인건지요기요 크롤링가능




# 2022년 03월 10일

## 개발

- 음악
	- 장르, 악기, 가수 및 작곡가 등에 따른 음악 분류
		- 개인이 많이 듣는 노래를 기반으로 음악 추천
	- 오디오 전처리
		- 주파수를 분석
		- 푸리에 변환,Short Time Fourier Transfrom(STFT)
		- 벡터화 변환으로 **MFCC** 많이 사용
	- 관련 url
      [멜론](https://tech.kakao.com/2020/04/29/kakaoarena-3rd-part1/)
	  [음성인식 예시](https://hyunlee103.tistory.com/21?category=999732)
	  [오디오 전처리 예시](https://hyunlee103.tistory.com/39?category=999732)
	  [장르 분류 예시](https://jonhyuk0922.tistory.com/114)
	  [스포티파이 2010-2019 인기곡 데이터셋](https://www.kaggle.com/leonardopena/top-spotify-songs-from-20102019-by-year)
	  [스포티파이 나라별 인기곡 데이터셋](https://www.kaggle.com/leonardopena/top-50-spotify-songs-by-each-country)
	  [스포티파이 추천 예시](https://www.kaggle.com/vatsalmavani/music-recommendation-system-using-spotify-dataset/notebook)
	  
	- 가사 분석을 통한 노래 추천(NLP, LDA)
		- 기분 별 노래 추천~

	
	  
- 농산물(스토어팜)
	- YOLO 기술 사용 가능해보임
	
- 패션
	- 댓글분석
		- 긍정 및 부정 -> 사이즈, 재질, 색깔 등의 내용으로 분류가 될 듯 합니다??? (감성 분류와 유사, NLP)
	- 상품추천
		- 그 전의 구매 내역을 불러와서 구매 패턴(색깔, 디자인 등) 파악 후 추천 (CNN, H&M 예시 코드 활용, YOLO 기술)
	- 댓글 분석 + 상품 추천
		- 댓글들을 참고하여 개인별로 상품을 추천해주는...? (어려워 보입니다만..)



- YOLO 기술
> 다크넷, 오픈소스 구축해서 활용
> 사물감지, 욜로법
> 리눅스 시스템

	- 농작물
		- 사물 감지를 통해 병해 여부 판단, 병명 확인 등
			- 미래 예측
		- 굳이 욜로 기술 아니어도 가능할 것 같긴 합니다만...
		- 사진을 통해 수확물 예측
			- 사진 데이터 구하기가 어려워 보임
		- 생육 기간을 사진을 참고하여 예측
	-  관련 데이콘 대회 참고
	- 관련 url
	[작물 병해 진단](https://dacon.io/competitions/official/235870/data)
	[생육 기간 예측](https://dacon.io/competitions/official/235851/overview/description)



## 회의

## 이슈 


# 2022년 03월 11일

## 조사

### 오전
- 축산 
[캐글 데이터셋을 이용한 고기 품질 평가 코드](https://www.kaggle.com/nalkrolu/meat-quality-assessment)
[한국축산데이터-우주님](https://aihub.or.kr/aidata/30733) -> 레이블링 수정 작업 필요
[고기신선도 -성배님](https://scienceon.kisti.re.kr/srch/selectPORSrchArticle.do?cn=JAKO202016357498067&dbt=NART)
[소고기 등심 세부 부위](https://scienceon.kisti.re.kr/srch/selectPORSrchArticle.do?cn=JAKO202128837845066) -> 데이터 증강
- 음식
[다이어트(칼로리)](https://scienceon.kisti.re.kr/srch/selectPORSrchArticle.do?cn=NPAP13342339)
[한국 이미지(음식) 소개](https://aihub.or.kr/aidata/13594) -> 이미지 데이터
[건강관리를 위한 음식 이미지 소개](https://aihub.or.kr/aidata/27674) -> 레이블링 수정 작업 필요
[음식 이미지 및 영양정보 텍스트 소개](https://aihub.or.kr/aidata/30747) -> 레이블링 수정 작업 필요
[YOLO를 활용한 시각 장애인용 식사보조 시스템 개발](https://www.koreascience.or.kr/article/JAKO202130053160358.pdf) 

### 오후
- 음악
[내용 기반](https://s-space.snu.ac.kr/bitstream/10371/151420/1/000000154848.pdf)
	- 협업 필터링
		- 사용자의 특정 아이템에 대한 기호 정보(taste information)에 따라 사용자의 선호를 예측
		- 유사한 패턴
	- 내용 기반(자연어 처리)
		- TF-IDF
	- 오디오 기반
		- 주파수 분석, STFT
		- 어려울듯,,,
[CNN 소프트맥스로 장르 구분](https://www.koreascience.or.kr/article/JAKO201912261948902.pdf)
	- 음악의 스펙트로그램을 여러개의 샘플로 나누어 각각의 CNN 결과를 투표 시스템을 이용해 곡의 장르를 구분. 그리고 Softmax 레이어 방식을 추가

- 카페
	- 의자와 테이블 데이터 셋을 찾아서 이미지 학습
	- 서있는 자세, 앉아 있는 자세 이미지 학습
	- 마스크 착용 여부
	
[의자 데이터셋](https://www.kaggle.com/mbkinaci/chair-kitchen-knife-saucepan)
[탑승객 탐지](https://journal-home.s3.ap-northeast-2.amazonaws.com/site/2020kics/presentation/0536.pdf)
[도둑질 탐지](https://developer-thislee.tistory.com/19?category=818795)
## 회의

## 이슈 


# 2022년 03월 12일

## 이슈
### DS
- 하둡 위에 도커는 안됨
  -  할 수는 있지만 기간 내에는 안됨
1. 스포티파이 
   - 키워드에 따른 음악 플레이리스트 존재
   - 근데 스포티파이 API 막혀있는지 확인 필수
2. YOLO 
- stable 한 것은 v4
- 실시간 스트리밍에 좋은 것은 v5
  - cortex -> 쉽게 아마존에 올릴 수 있음
  - 사용자 편의성 높음
- 모두가 참여가 가능할 것 같은 주제입니다
- 재택 근무 -> 제대로 일하고 있는지, 졸린지 등
- 아마존 -> 놀이공원 실시간 줄 확인
- 욜로는 주제 다양하게 가능함
- 데이터 양 충분할지?: ''숏텀 프레딕트''
  - 작은 데이터여도 예측 가능한 경우가 있음
  - 데이터의 볼륨이 작아도 예측 가능한 모델을 한 번 찾아보는 것으로 해보시길
  - 직접 크롤링 or AI허브 찾아보기
  - 페이크 데이터 -> 제너레이터, 가라데이터, 어그맨테이션

### DE
- 하둡, 카프카, 스파크 사용
  -  하둡은 대용량
  - 카프카 스파크는 실시간
  - 실시간으로 분석할 수 있는 요건을 만들어냄
1. 음원 추천 
- 사용자별로 구분 가능한 데이터를 찾을 수 있는지를 확인해야함 - 성별, 나이대 등 : 근데 안될듯
- 몽고디비로 비정형 정형 둘다 처리 가능한데 굳이 나눠서 처리할 필요가 있나
2. 마스크
- 두 소주제를 묶어서 하기




# 2022년 03월 14일

## 조사
- **roboflow.com** -> 데이터셋 다운로드
	- label -> matches my all labels
	- it drops bad annotation -> only in frame data
	- it can split tran, validation, test data

- [마스크 여부 유튜브](https://www.youtube.com/watch?v=ncIyy1doSJ8)
- [CCTV를 통한 사람 감지](https://github.com/kkobooc/DeepLearning_YOLO)
- [마스크 감지 -roboflow 데이터 사용](https://colab.research.google.com/drive/1JFUkwnpBi0Ou7elSz2Jre5Sln6WXR_a-?usp=sharing)
- [커스텀 데이터 학습](https://minding-deep-learning.tistory.com/19)
- [마스크 탐지 예시](https://pyimagesearch.com/2020/05/04/covid-19-face-mask-detector-with-opencv-keras-tensorflow-and-deep-learning/)

## 회의
- 주제 확정 및 기획안 작성
- yolo trial 파일 공유하면서 yolo 결과 확인해봄

# 2022년 03월 15일

## 공부
- aws로 yolo 실행 해보기
- [yolov5 설치](https://blog.naver.com/PostView.nhn?blogId=remocon33&logNo=222181286676)
- [주차장 빈 공간](https://youtu.be/VO58tq3M1Jc
)
-[주차장 빈 공간2](https://www.youtube.com/watch?v=fdWx3QV5n44)

데이터 라벨링

- [라벨링 툴](https://supervise.ly/)
- [라벨링 툴2](https://byeon-sg.tistory.com/entry/labelImg%EC%82%AC%EC%9A%A9%ED%95%B4%EC%84%9C-yolo-%EC%9D%B4%EB%AF%B8%EC%A7%80-%EB%9D%BC%EB%B2%A8%EB%A7%81%ED%95%98%EA%B8%B0)

라벨링한 데이터를 데이터셋으로 만들기
- [바운딩 박스 툴](https://bong-sik.tistory.com/m/25)
## 회의
### 오전
- yolo train
	- 정확도 높이기
	- 학습자료 수 늘리기
- yolo 실시간
	-  웹캠 사용 가능
- 영상 화면 분할
	- 주차장 예시 참조
	- 빈자리 여부 확인
- ubuntu 계정으로 로그인 해서 sudo get-install 1libxcb-xinerama0
	- [sudo] : 현재 계정 말고 ubuntu 계정으로 로그인 해야함
	- ubuntu 계정으로 실수하면 프로그램을 처음부터 다시 설정해야 함 (주의)
- 마스크만 인식?? : 흑백으로 처리해도 ㄱㅊ
### 오후 
- 공부하면서 느낀 점 
	- 앉은 자세 서있는 자세는 데이터 셋이 안보이는 듯  -> 직접 사진 찍어서 어그맨테이션 해야하지 않을까?
	- 공간 구분은 예시가 많아서 가능한데, 이미 라벨링이 되어 있는 데이터로 yolo 돌리는 거라서
		- 내가 만드는 데이터로 한다면? 직접 라벨링 해야하지 않을까?
- [웹캠](https://wandb.ai/onlineinference/YOLO/reports/YOLOv5-Object-Detection-on-Windows-Step-By-Step-Tutorial---VmlldzoxMDQwNzk4#creating-bounding-boxes-with-yolov5-on-your-webcam)
- [!!라벨링!!](https://wandb.ai/onlineinference/YOLO/reports/Collect-and-Label-Images-to-Train-a-YOLOv5-Object-Detection-Model-in-PyTorch--VmlldzoxMzQxODc3?galleryTag=posts)
- 캠- 로컬?
- 결과를 앱이나 앱으로 내보낼 수 있는 것? 텐서플로우?
# 2022년 03월 16일

## 공부
- 테이블 앉아있는 데이터, 서있는 데이터 등 파악
- [!!라벨링!!](https://wandb.ai/onlineinference/YOLO/reports/Collect-and-Label-Images-to-Train-a-YOLOv5-Object-Detection-Model-in-PyTorch--VmlldzoxMzQxODc3?galleryTag=posts)
- 캠- 로컬?
- 결과를 앱이나 앱으로 내보낼 수 있는 것? 텐서플로우?
[탠서플로우로 내보내기](https://tensorflow.google.cn/lite/guide/get_started?hl=ko)
- [커스텀 데이터 사용하기](https://github.com/ultralytics/yolov5/wiki/Train-Custom-Data)
- [커스텀 데이터 사용하기2](https://sguys99.github.io/ds01)
- [웹캠으로 욜로 실행](https://www.youtube.com/watch?v=m4U-rOZZ_Lg)

- 로컬 cmd를 이용해 웹캠으로 욜로 실행
	- 문제는, 다중으로 가중치 설정하는 방법을 모름!
	- 마스크 가중치 데이터 열면 기존에 학습된 데이터들(human, cell phone 등)이 인식이 안됨

- yolo에서 학습된 자료를 안드로이드 등의 앱?웹?에서 사용하려면 .pt 파일을 .tflite 파일로 변환해야 한다 하네욥...?
	- [관련 블로그](https://bekusib.tistory.com/210)
	- [관련 블로그2](https://junyoung-jamong.github.io/machine/learning/2019/01/25/Android%EC%97%90%EC%84%9C-%EB%82%B4-YOLO%EB%AA%A8%EB%8D%B8-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0.html)

- [라벨링](https://developeryoung.tistory.com/16?category=879762)
## 회의
- YOLOv5 황희원, 김우주, 김성배
  - 욜로 -> 안드로이드 tensorflow lite 파일변경이 필요한 것 같다
  - 마스크를 썼냐 안썼냐, 자리가 비워있나?
    - 모델을 학습시키려면 샘플
	- 카페를 지정을하든 이미지가 필요, 지금 현재 쓸 데이터가 없다
	- 라운지 테이블 6개 배치하고 카페라고 가정하고 cctv
	- 샘플은 그럼 어떤식으로?
	  - 동영상을 찍고 캡처를 하든 샘플 이미지가 필요
	  - 빈자리 이미지, 사람 이미지
	- 멀티캠퍼스로 사용할수 있으면 좋겠다
	- 빈테이블이냐 빈테이블이 아니냐도 확인 필요
	- 결과에대한 부분이 저장을하냐 어떻게 가져올꺼냐
	- 기존꺼 인식 사람+마스크, 노마스크를 추가
	- 셋을 모은다면 우리 다 모여야대~ 휴게실
	- 최소 천장 이상으로~
- 웹캠, 폰캠 심다훈, 홍성희
  - 주피터, html 계획
  - yolo + 카메라
- Flutter,Django(admin, restful API) 이현호, 김용현
  - Flutter, Django(restful API)
    - YOLO 결과 값이 반환대는 부분, DB저장 부분 필요한다
	- pytorch 허브를 이용하면 pandas나 json받을 수 있는것 같다
	- 결과를 어떻게 할까 저장할까? 실시간으로 받을까?
	  - 백엔드 부분이 없는거 같다
	- Django 사용자 관리부분에만 사용이 될 것 같다
	- 앱을 통해서 보여주기 : 값을 뽑아 올 수 있는지
	- 변수를 글로벌하게 저장할 필요가 있다면 쿠키를 사용
	- Django로 어드민 관리
	  - Django랑 Flutter 연결이 잘된다
	  - 생성은 할수 있지만 삭제는 할수 없다
	  - 로그인 있어보이게 하려면??

# 2022년 03월 17일

## 공부
### 라벨링
[관련링크](https://colinch4.github.io/2020-12-04/LabelImg/)
[링크2](https://developeryoung.tistory.com/16)
1. labelImg 설치 (https://github.com/tzutalin/labelImg )
2. 아나콘다 관리자 권한 프롬프트에서 밑에 코드 실행
	- 이 때 가상환경 설정한 후 진행(multicampus)
```
cd C:\Users\User\Desktop\labelImg\labelImg-master # 예시
conda install pyqt=5
conda install -c anaconda lxml
pyrcc5 -o libs/resources.py resources.qrc
```
3. `C:\Users\User\Desktop\labelImg\labelImg-master` 에 생성된 resources.py 와  resources.qrc 를 `C:\Users\User\Desktop\labelImg\labelImg-master\libs`로 직접 옮겨준 후 밑에 코드 실행
```
pip install labelImg
labelImg
conda install python==3.9 #파이썬 버전이 3.10이 넘어가면 실행이 안됨
```
4. open dir에서 사진 파일 가져오고
5. change save dir에서 저장 폴더 지정
	- w : rectbox 생성
	- d : 다음 사진
	- a : 이전 사진
	- 꼭 YOLO로 설정하고 만들어야함 -> txt파일로 저장되게끔
6. (labelImg_master 폴더를 C드라이브로 옮겨놓기도 함->구글링)

### 욜로 튜토리얼
- [yolo tutorial](https://www.youtube.com/watch?v=NU9Xr_NYslo)
- [yolo tutorial - 한국어](https://lynnshin.tistory.com/47)
- [풍선 판단 예시](https://www.kaggle.com/vbookshelf/basics-of-yolo-v5-balloon-detection/notebook)

### Yolact 사용
- [튜토리얼 참고](https://blog.naver.com/9503090_/221994950839)
- 근데 완벽하게 다른 객체로 판단하지 않는듯
- 그 대신 픽셀 단위?로 더 정확하게 분류는 함
- 근데 예시가 너무 적어서 따라하기 힘듦
## 회의
- YOLOv5
  - 결과저장해보기 성공
  - 직접 라벨링해보기 확인, 같이 해서 박스 그려야됨
  - 빈자리 구분
     - 영상을 우선 찍어보자 빠르게
	   - 무중력 지대 대방동
       - 월-금 10:00-21:00 / 토 10:00-16:00 (일요일, 공휴일 정기휴관) 현재 코로나19 단계에 따라 단축 운영중입니다.
	 - 결과나오는거에 좌표까지 표시된다면 구분이 좀더 쉽지않을까?
	 - 안되면 노가다로 다 테이블을 지정?
- 캠
   - 주피터에서 캠 확인, 오늘 실패
   - 내일 더 해보기
   - Flutter로 실시간 영상 보내기 확인
   - 주피터에서 안된다면 로컬에서 진행 후 깃허브로 공유하는 방법으로
- Flutter,Django
   - 장고 페이지 확인
   - 플러터랑 연동 해보기

# 2022년 03월 18일
## 공부
- 좌표 파악 -> 데이터 가져올 수 있는지?
- 아니면 테이블 별로 구분이 가능할지?

- (x,y,w,h)=(bounding box 중심점의 x,bounding box 중심점의 y,bouding box의 W, bounding box의 H)
![yolo 좌표](https://media.vlpt.us/images/jaeha0725/post/530b56bf-7373-43bc-b432-28a0ef54feae/image.png)
## 회의
- [mask R-CNN]](https://reyrei.tistory.com/12)
- [object tracking and counting](https://blog.naver.com/dldudcks1779/222071049946)
- [동영상 프레임 자르기](https://sj-d.tistory.com/24)


- Mask R-CNN → 개체 분류 가능
- Panoptic Segmentation
- 선긋기
이것들 중 하나 선택해보기


# 2022년 03월 21일
## 공부
-[이론](https://www.analyticsvidhya.com/blog/2021/12/how-to-use-yolo-v5-object-detection-algorithm-for-custom-object-detection-an-example-use-case/)
### 객체 분류
- [객체 수 카운팅](https://github.com/tugot17/YOLO-Object-Counting-API)
- [객체 수 카운팅2](https://github.com/dldudcks1779/Object-Tracking-and-Counting)
	- 코드 분석하기


```
 # 사람인 경우
         if classID == 0: # yolo-coco 디렉터리에 coco.names 파일을 참고하여 다른 object 도 인식 가능(0 인 경우 사람)
                    # 객체 확률이 최소 확률보다 큰 경우
                    if confidence > args["confidence"]:
                        # bounding box 위치 계산
                        box = detection[0:4] * np.array([W, H, W, H])
                        (centerX, centerY, width, height) = box.astype("int") # (중심 좌표 X, 중심 좌표 Y, 너비(가로), 높이(세로))

                        # bounding box  좌표
                        startX = int(centerX - (width / 2))
                        startY = int(centerY - (height / 2))
                        endX = int(centerX + (width / 2))
                        endY = int(centerY + (height / 2))
            
                        # 객체 추적 정보 추출
                        tracker = dlib.correlation_tracker()
                        rect = dlib.rectangle(startX, startY, endX, endY)
                        tracker.start_track(rgb, rect)
                
                        # 인식된 객체를 추적 목록에 추가
                        trackers.append(tracker)
```
0(person), 24(backpack) ,25(umbrella), 26(handbag), 28(suitcase), 39(bottle), 41(cup), 42(fork), 43(knife), 44(spoon), 45(bowl), 63(laptop), 64(mouse), 65(remote), 66(keyboard), 67(cell phone),73(book)
 - 이것을 인식하게끔 설정하면 될듯
 
 -deep sort : counting 알고리즘
 - cfg : 네트워크 구조

## 회의
### 사이언스
- object counting 코드 분석

### 엔지니어
- Flutter와 YOLOv5 연동
  - 플러터 설치 
  - 카메라 연동, YOLOv5 구동

### 정리
- 실시간 -> 마스크
- 앱 구동 -> 빈자리(aws 가능)?


# 2022년 03월 22일
## 공부
- 수요일에 어떤 식으로 영상 찍을지?
- 공부한 내용 파악
	- 궁금한점 : 대부분의 에시가 이분할인데... 6분할 가능?
	- 차선 인지도 구경하고 있긴 함
	- [초 단위로 캡처](https://developer-thislee.tistory.com/18?category=818795)
- 객체수 카운팅 인강 따라하기
 [카운팅 인강](https://www.youtube.com/watch?v=7gz3vUmy0C0&t=217s)
## 오전 회의
- 카메라 각도
- 경우의수 : 마스크 착용 여부 / 빈자리 여부
	- 추가로 생각할 것 : 테이블 위 물건


# 2022년 03월 23일
