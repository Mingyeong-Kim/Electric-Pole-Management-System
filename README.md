# Electric-pole-safety-management-system

- **프로젝트 기간: 2021.08.12 - 2021.08.29(3주, 팀)**
- **프로젝트 개요: IoT 기술을 적용한 전신주 안전 관리 시스템 개발**
- **H/W 개발 사용 기술: Python, IBM Watson IoT**
- **H/W 개발 사용 디바이스: Raspberry Pi(라즈베리파이), Sensor(기울기, 충돌감지, 미세먼지, 온/습도, LED 센서)**
- **S/W 개발 사용 기술: IBM Cloud, Javascript, Node-RED**
- **역할: 상태판단 및 모니터링 시스템 알고리즘 구현(S/W)**

## 프로젝트 배경
- 즉각적인 위험 예방이나 유지보수가 가능하게 함으로써 지주로부터 발생되는 위험 최소화 필요
- 지주는 환경적 데이터를 얻기에 좋은 매개체로 기상 관련 데이터를 수집 및 모니터링 하여 실시간 기상정보를 제공할 수 있음 

## 프로젝트 목표
- IoT 기반의 지주(폴) 상태정보 검출·진단 시스템 및 모니터링 시스템 개발로 사고예방 및 신속한 유지보수 환경 구축
- 기상 정보를 실시간 모니터링 할 수 있는 환경 구축

## 프로젝트 시나리오
<img width="500"  height="300" src="https://user-images.githubusercontent.com/65681568/138469263-769dc3e6-43ef-43f3-8147-9f8898e7d538.png">
<img width="550"  height="550" src="https://user-images.githubusercontent.com/65681568/138469941-e2fb2826-912e-461b-a961-14b986b83b00.png">

## 프로젝트 과정 및 내용
1. H/W(하드웨어) 개발
   - 1-1. 라즈베리 파이와 센서를 사용한 디바이스 회로 구성 
   - 1-2. 센서와 클라우드 플랫폼(IBM Watson IoT)이 통신할 수 있는 환경 구축
   - 1-3. 기울기 센서, 충돌감지 센서, 미세먼지 센서, 온/습도 센서 제어 및 통신 코드 작성(OPH 플랫폼 구현)

2. 모니터링 S/W(소프트웨어) 개발
   - 2-1. Node-RED를 통해 각 센서에서 수신되는 정보 처리 및 모니터링 설계도 작성
   - 2-2. 각 센서에서 수신되는 정보처리 및 모니터링 알고리즘 구현(Javascript)
   
## 프로젝트 결과

- **H/W 개발 결과**
<img width="200"  height="200" src="https://user-images.githubusercontent.com/65681568/138470720-3c011709-f6c1-448a-8ba2-dd91711f5a8c.png">

- **모니터링 S/W 개발 결과**
<img width="750"  height="350" src="https://user-images.githubusercontent.com/65681568/138473072-4056c64a-3831-4060-a38b-04bc9c7e8f7a.png">

- **프로그램 시연 영상**
https://youtu.be/yatn3Jptla8



