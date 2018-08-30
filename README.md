## 파이썬 챗봇 만들기

### 1. 카카오톡 플러스친구 관리자센터

- 플러스친구 생성 후 공개설정(공개 안되면 검색안됨)
- 스마트 채팅 API형 사용

### 2. c9 

- 우측 상단의 톱니바퀴에 들어가 python3로 설정변경
- `sudo pip3 install flask` 플라스크 설치

### 3. keyboard

```python3
from flask import Flask, render_template
import os
# json으로 바꾸기 위해 library 추가
import json

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello index page!"

@app.route("/keyboard")
def keyboard():
    # keyboard dict 생성
    keyboard = {
        "type" : "buttons",
        "buttons" : ["메뉴", "로또", "고양이", "영화"]
    }
    
    # dict를 json으로 바꿔서 리턴해주기 위한 코드
    json_keyboard = json.dumps(keyboard)
    return json_keyboard
    
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))

```
> RESTful?? (CRUD)
> GET - READ
> POST - CREATE
> UPDATE - UPDATE
> DELETE - DELETE

### 4. API

4.1. requset

- url : 어떤 경로로 보낼꺼니?
- method : 어떤 방법으로 보낼꺼니?
- parameter : 어떤 정보를 담을거니?
    
4.2. response

- data type : 어떤 형식으로 답할까?

> sorted vs sort
> a.sort() : return이 없다 (list를 정렬하고 끝남) - 원본 바뀜
> sorted(a) : 정렬된 list를 return - 원본 안바뀜