# Instagram_bot

## (필자를 포함한) 모든 대한민국 훈련병들을 위한 인스타그램 인편지기입니다.
> Instagram bot for promoting ROKA trainee soldier(just like me)'s consolation letters.
<p align="center">
    <img src="https://user-images.githubusercontent.com/63336701/225343958-18730305-a22b-450e-bff2-af80af4c716c.jpg" width="350">
</p>

## 1. 들어가기 (Getting Started)
이 레포지토리는 **윈도우 환경**에 맞춰 제작되었습니다.
**윈도우 작업 스케줄러**에서 ```script.bat``` 파일을 실행시키는 방식으로 제작되었다는 점을 알립니다.

이 레포지토리는 **설치 후 바로 사용할 수 없습니다!**
```userInfo.py```에서 인스타 ID/PW, 더캠프 ID/PW를 직접 설정해주셔야 합니다!

**(인스타에 게시할 사진(```soldier_info.jpg```) 및 문구(```posting_texts.txt```)도 마찬가지입니다!)**

또한, ```main.py```에서는 게시물 사진의 절대경로를, ```script.bat```에서는 작업폴더의 경로를 올바르게 수정해주셔야 합니다 :)


```python
#userInfo.py
class User:
    def __init__(self):
        self.__insta_email = "blahblah@naver.com"
        self.__insta_id = "blahblah@naver.com"
        self.__insta_password = "1234"
        self.__camp_id = "blahblah@naver.com"
        self.__camp_password = "1234"
```
```python
#main.py
# 인스타에 게시할 사진 경로(절대경로)를 작성해주세요!
send_keys('C:\\Users\\ljjun\\Instagram_bot\\soldier_info.jpg')
```
```bat
rem script.bat
@echo off

cd C:\Users\ljjun\Instagram_bot
```
### 1-1. 더캠프(THE CAMP) 설정
훈련병의 인편 카페 개설 여부를 확인하기 위해, 더캠프에서 몇 가지 사항을 체크 및 설정해주셔야 합니다.

1. 보고싶은 군인 추가
   - [더캠프](https://www.thecamp.or.kr)에 로그인한 후, **보고싶은 군인**에 훈련병의 인적사항을 입력하여 추가해주시면 됩니다!
  
2. fn_cafeCreateCheck() 검색
   - 보고싶은 군인을 등록한 후, 개발자 모드(f12)에 진입하여 **훈련병의 카페 개설 여부를 확인**하는 fn_cafeCreateCheck()함수 및 parameter를 확인한 후, ```main.py```에 올바르게 변경해주시면 됩니다!
<p align="center">
    <img src="https://user-images.githubusercontent.com/63336701/225344301-2cf528f9-1c01-4c3b-85ea-cadeff31ee4b.png">
</p>

  ```python
  #main.py
  # "fn_cafeCreateCheck('{any}','이름','입영일자','생년월일','{any}','{any}','{any}')" 형식의 정보를 직접! 더캠프 홈페이지에서 찾으셔야 합니다...!!
FINDING_CAFE_SCRIPT = "fn_cafeCreateCheck('', '이름', '입영일자', '생년월일', '', '', '')"
  ```

### 1-2. 준비사항 (Prerequisites)
- **훈련병의 인스타 ID/PW, 더캠프 ID/PW**
- 훈련병의 인스타에 게시할 사진 및 문구
- python3
- Chrome
- selenium
- pywinauto

```python
# 라이브러리 설치
pip install selenium
pip install pywinauto
```

### 1-3. Chromedriver 설치

#### 1) 크롬 버전 확인
```도움말``` -> ```Chrome 정보``` 클릭
<p align="center">
    <img src="https://user-images.githubusercontent.com/63336701/225347552-125b2845-c40c-440a-ac98-86b0d3c02ca8.png">
</p>

<p align="center">
    <img src="https://user-images.githubusercontent.com/63336701/225347568-f79ebedf-2a45-41c7-86b9-b891fa85af4f.png">
</p>

#### 2) ChromeDriver 설치 및 경로 지정
[ChromeDriver - WebDriver for Chrome](https://chromedriver.chromium.org/downloads)

위 사이트에 접속하여 ```Current Releases```에서 ```본인의 크롬 버전 및 OS에 해당하는 ChromeDriver```를 설치해주세요

<p align="center">
    <img src="https://user-images.githubusercontent.com/63336701/225351346-a3f585d2-253d-496c-b91c-0cfc1b2741cb.png">
</p>

압축해제한 ```Chromedriver.exe``` 파일을 본인의 ```파이썬 경로(디렉토리)```로 옮겨주세요!