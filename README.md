## 프로젝트 배경

- youtube를 보다가 한 시각 장애를 가진 youtuber의 고충을 알게 되었다.
- 시각장애인 눈을 실명한 분들보다 색깔 정도를 구분 할 수 있거나 가까이서 봐야 글자를 어느 정도 구분 할 수 있는 사람들이 대부분이라고 한다.
- 시각 장애인은 점자 블록 파손 및 잘못된 설치, 탑승 안내 점자 오류, 스크린도어 미 설치, 길거리 보행 중 방해물, 표지판 색깔 혼동 등 많은 불편함을 느낀다.
- 시각장애인은 **지하철에 음성 안내를 들을 수 없는 경우 출구와, 비상구 찾기가 힘들다.**
- 지하철에서 **시각 장애인 용 편의 시설의 노후화로 인한 불편함을 보안하고** 도움을 주는데 도움을 주고 싶다.

## 프로젝트 목표

### 카메라를 이용해 출구를 찾을 수 있는 object detection모델을 만드는 것

## 프로젝트 진행 순서

**2022.05.16 ~ 2022.05.23**

1. yolov5 라이브러리 사용법 숙지
2. 비상구 표지판 사진 크롤링 100장

    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e59d5a39-c467-401c-985c-2d46ef19313c/Untitled.png)
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0aec9ecf-1852-4a7d-8a4a-36db4d159c36/Untitled.png)
    
3. pyyaml 라이브러리로 기본 yolov5s.yaml(가벼운 모델링) 파일을 class 개수 2개로 custom yaml파일 저장

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/21415f2c-7ed1-45d5-9fd7-e80c1068a659/Untitled.png)

1. 80 epochs학습
2. 학습 완료된 [best.pt](http://best.pt) 저장
3. test data 영상, 사진 예측

**2022.09.16 ~ 2022.09.20**

- 학습 방식은 위와 동일
1. 개화산역에서 왕십리 그리고 고속 터미널을 통해서 집으로 돌아오기까지 출구가 많은 역을 내려 표지판과 비상구 사진을 직접 각도를 달리하여 영상으로 찍고 프레임으로 나누어 약 500장으로 만듦
2. 표지판 라벨링 후 train, validation set 나누기
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bf5aba3f-a796-4ade-87db-f4594b2e4891/Untitled.png)
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ef1c5a17-f4b7-478d-812a-fd7d63c48200/Untitled.png)
    
3. 100 epochs학습

> **라이브러리**
> 
- YOLO v5
- yaml

> **파일 이름 변경 툴**
> 

DarkNamer_080210_fixed

> **라벨링 툴**
> 

windows_v1.8.1

## 데이터 셋 설명

**두 표지판 데이터의 공통 장점**

1. 규격이 어느 역이나 같다.
2. 서울 교통 공사 지하철에서 표지판 데이터를 얻을 가능성이 있음

**나가는 곳 표지판**

1. 글자 폰트가 통일되어있다.
2. 배경이 노란색이다.

- **프로젝트 1차 데이터**

— 구글과 네이버에서 얻은 나가는 곳 비상구 표지판 사진

1. 화질이 좋지 않음
2. 다양한 각도의 사진이 없음
- **프로젝트 2차 데이터**

— 직접 찍은 사진

1. 화질 개선
2. 다양한 각도 개선

## 프로젝트 모델 결과

### 딥러닝 학습 사진 약 100장 결과 (2022.05.16 ~ 2022.05.23)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0b4a7dc6-9cd6-4bb8-a432-3c188558a4ac/Untitled.png)

**표지판 detection 정확도 0.75**

---

### 딥러닝 학습 사진 약 500장 결과 ****2차**** (**2022.09.16 ~ 2022.09.20**)

![exit_image.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/cc7e0325-59aa-4958-adda-def3c92115ae/exit_image.jpg)

 **표지판 detection 정확도 0.82**

![20171009123531_dftrqtwf.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1b1349c4-8d4d-4888-8ddb-ba3c91c4f3e4/20171009123531_dftrqtwf.jpg)

![8372546b580a89148e0be79842c66118.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5c5de29f-926e-437a-9797-4f0d2c1b6bf8/8372546b580a89148e0be79842c66118.jpg)

![201311192201418902.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d14df68e-2c67-422a-94f4-92020b718672/201311192201418902.jpg)

![unknown.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3da3298e-9772-49af-a2ba-d39388a19cba/unknown.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ec5b40db-263e-4515-87ef-82dc71016438/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/97a1e04f-1adf-4fa2-9d09-227ca1cca29d/Untitled.png)

- 인식률이 떨어지거나
- 어떤 사진은 관련 없는 다른 물체를 인식하는 경우가 있다.

## 프로젝트의 한계, 느낀 점

1. 데이터 포털 사이트에 표지판 데이터가 없다.
2. 다양한 각도에서 찍은 표지판 데이터 필요하다.
3. 개인적으로 많은 데이터를 얻기 힘들다.

## 프로젝트 모델 성능 개선

1. “나가는 곳” 이라는 글자만 라벨링하여 정확도를 높이고 학습 상 이상치를 줄인다
2. 직접 데이터를 모으는 수고가 필요하다.
3. 총합 약 100장의  나가는 곳 표지판의 데이터 학습 결과 정확도 **0.75**
총합 약 500장의  나가는 곳 표지판의 데이터 학습 결과 정확도 **0.82**
결과를 봤을 때 class의 사진 데이터만 1000장이 넘는다면 0.90 이상의 정확도가 예상된다.

## 프로젝트 목표 외 서비스 구현 (접근 방식)

1. 객체와의 거리 계산을 통해 표지판의 위치를 따라갈 수 있도록 설계 (진동 or 소리)
2. 출구 번호와, 화살표를 학습하여 출구 번호와 방향을 알려줌
혹은 문자 데이터를 학습하여 표지판 안에 있는 글자만 인식하게 하여 음성으로 안내
3. 매 역마다 QR코드를 부착해 찾는 출구를 알려주는 음성 메시지를 들려준다
4. 앱 사용시 간판 데이터 실시간 추가 수집하여 성능 개선
5. 지하철 뿐만 아니라 길 안내, 장애물 위치 안내, 찾는 간판, 등 확장 활용 (길거리 보행자 데이터 셋이 있음)

![장애물 경고](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c1149365-0855-4f5f-a861-bbd48e588549/Untitled.png)

장애물 경고

![횡단보도를 건너도 되는지 물어보면 안내 음성](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d861cc1f-56c3-4fc9-ab11-9d782f576f73/Untitled.png)

횡단보도를 건너도 되는지 물어보면 안내 음성

![원하는 상품 찾기](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d8af6a86-5770-48bf-8400-bdb8948cb3a6/Untitled.png)

원하는 상품 찾기
