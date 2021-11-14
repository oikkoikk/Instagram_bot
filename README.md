# Instagram_bot

## 훈련병 이종준을 위한 인스타그램 인편지기입니다.
> Instagram bot for promoting ROKA trainee soldier(just like me)'s consolation letters.
### 들어가기 (Getting Started)
이 레포지토리는 **윈도우 환경**에 맞춰 제작되었습니다.
**윈도우 작업 스케줄러**에서 ```script.bat``` 파일을 실행시키는 방식으로 제작되었다는 점을 알립니다.

이 레포지토리는 **설치 후 바로 사용할 수 없습니다!**
```userInfo.py```에서 인스타 ID/PW, 더캠프 ID/PW를 직접 설정해주셔야 합니다!

**(인스타에 게시할 사진(```soldier_info.jpg```) 및 문구(```posting_texts.txt```)도 마찬가지입니다!)**
```python:userInfo.py
class User:
    def __init__(self):
        self.__insta_email = "blahblah@naver.com"
        self.__insta_id = "blahblah@naver.com"
        self.__insta_password = "1234"
        self.__camp_id = "blahblah@naver.com"
        self.__camp_password = "1234"
```
#### 준비사항 (Prerequisites)
- **훈련병의 인스타 ID/PW, 더캠프 ID/PW**
- 훈련병의 인스타에 게시할 사진 및 문구
- python3
- selenium
- pywinauto