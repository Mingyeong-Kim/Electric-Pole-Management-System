# Electric-pole-safety-management-system

- **프로젝트 기간: 2021.08.12 - 2021.08.29(3주, 팀)**
- **프로젝트 개요: IoT 기술을 적용한 전신주 안전 관리 시스템 개발**
- **사용기술: 라즈베리파이
- Python, IBM Cloud, Javascript, Node-RED
- **역할: 상태판단 및 모니터링 시스템 알고리즘 구현(S/W)**


## 프로젝트 목표
⦁ IoT 기반의 지주(폴) 상태정보 검출·진단 시스템 및 모니터링 시스템 개발로 사고예방 및 신속한 유지보수 환경 구축하고자 했습니다.
⦁ 기상 정보를 실시간 모니터링 할 수 있는 환경 구축하고자 했습니다.


## 프로젝트 과정 및 내용

- IoT 기반 지주(POLE) 기울기, 충격 측정 장치 개발
- IoT 기반 생활 환경 센서(온/습도, 미세먼지 등) 측정 장치 개발
- 지주 상태 및 환경 측정 정보 실시간 모니터링 시스템 개발

- **프로젝트 개요(Project Outline)**
<img width="500"  height="300" src="https://user-images.githubusercontent.com/65681568/137986387-da792c15-503e-409f-a9c1-66da58155ea6.PNG">

- **프로그램 로직(Program logic)**
<img width="600"  height="350" src="https://user-images.githubusercontent.com/65681568/137985791-d138313c-136c-44ab-93bd-e58c9be79766.PNG">


1. 필요 라이브러리 및 API 설정
   1-1.필요한 프로그램 설치(Prepare Requirements tools)
   
    * (1)	python 3.7(visual studio code)

    * (2)	PyAudio 0.2.11(Microphone) 
        – pip install pyaudio
    
    * (3)	PocketSphinx 
        – recognizer_instance.recognize_sphinx
    
    * (4)	Google API Client Library for Python 
        - recognizer_instance.recognize_google_cloud
        - pip install google-api-python-client
    
    * (5) FLAC encoder(voice file)
        - sudo apt-get install flac

    1-2. install SpeechRecognition
        - pip install SpeechRecognition

    1-3. download python library (from PyPI)

    1-4. python setup.py install
    
2. 데이터 베이스 생성 및 데이터 저장
   - 데이터(Data): 시카고 공공자전거 이용 데이터(Divvy data 2015_Q2)
 
3. 마이크 음성인식 설정 및 테스트
   - 음성인식 코드 구현
   - Microphone 변수(parameter) 조절  
   - 음성인식이 가장 잘되는 요건 및 변수설정 찾기

4. STT,TTS 로직 코드 구현
   - 인식된 문장(질문)을 바탕으로 얻고자하는 정보(대답) 추출을 위한 SQL쿼리로 변경해주는 코드 구현(Speech to Text)
   - 사용자가 얻고자 하는 답변을 영어 문장으로 구현하여 음성으로 전달하는 코드 구현(Text To Speech)
   - 예시 문장과 답변을 설정하여 코드를 구현함

5. 프로그램 테스트

## 프로젝트 결과
- 6개 질문에 대한 Q&A speaker 프로그램 로직 코드 완성

**추후 보완점**
- 외부의 소음이나 다양한 사람의 발음을 인식하지 못하는 경우가 있음
- 다양한 질문에 대한 STT,TTS 로직 코드 구현 필요

# A Research on Market Segmentation Based on E-Commerce User Reviews Using Clustering Algorithm

- **연구 기간: 2020.09 - 2021.12(1년 6개월, 팀)**
- **연구 개요: 머신러닝 클러스터링 기법을 활용한 이커머스 사용자 리뷰에 따른 시장 세분화 연구(졸업연구)**
- **사용기술: python(pycharm), selenium, Scikit-learn, pandas, numpy**
- **역할: 팀장, 데이터 수집(크롤링), 데이터 전처리, 모델 결과 분석**

## 연구 배경 및 목적
- 코로나로 인한 e커머스 시장 확대 및 인터넷 쇼핑몰 이용률 증가
- 고객 리뷰가 소비자 구매 의사결정에 미치는 영향력 증대
- 다양한 형태의 고객 리뷰어들에 대한 고객 분석 및 관리 필요
- 본 연구를 통해 고객들이 작성한 리뷰에 대해 분석하고 시장 세분화를 통해 고객관리를 위한 자료와 그 방안을 제공하고자 했습니다.

## 연구 방법 및 내용
1. (데이터 수집) 크롤링 기법을 활용한 약 1200명 이상의 e커머스 고객 리뷰 데이터 수집
2. (데이터 전처리) 데이터 정제 및 정규화
   - 텍스트 마이닝을 기반으로 변형된 KOSAC 감성사전을 이용한 고객 리뷰 긍/부정 분석
   - 32개 입력변수 설정 및 전처리 
3. (모델링) K-means clustering 모델을 활용한 고객 군집화 
4. (결과분석) 군집 결과를 바탕으로 시장 세분화 및 고객 특징 분석

## 연구 결과
- **1250명 모델링 결과(2차원)**
<img src="https://user-images.githubusercontent.com/65681568/137635732-80483126-6166-425b-85ed-954ca91c3a36.png" width="400" height="300"/>

- **1250명 모델링 결과(3차원)**
 <img src="https://user-images.githubusercontent.com/65681568/137635748-c5df96e6-3586-4ceb-a683-cb7b66942df7.png" width="400" height="360"/>
 <img src="https://user-images.githubusercontent.com/65681568/137998712-49996c6a-e1ed-4276-a808-a0dc9e365305.png" width="400" height="360"/>

- **1250명 시장 세분화 결과**
<img src="https://user-images.githubusercontent.com/65681568/137635755-f1e67feb-81fb-4543-938e-e06aa821063f.png" width="500" height="300"/>


- **기대효과 및 시장성**
   - e커머스 시장의 고객 유형 파악 및 고객 관리 용이
   - 잠재 고객 발굴을 통한 맞춤형 고객 관리 서비스 제공
   - 고객 군집별 타겟 마케팅을 통한 기업의 마케팅 비용 절감 및 수익 창출







