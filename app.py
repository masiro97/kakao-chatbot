from flask import Flask, request, jsonify
import os
import json
import random
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello index page!"

@app.route("/keyboard")
def keyboard():
    keyboard = {
        "type" : "buttons",
        "buttons" : ["메뉴", "로또", "고양이", "영화"]
    }
    
    json_keyboard = json.dumps(keyboard)
    return json_keyboard

@app.route("/message", methods=['POST'])
def message():
    
    # content라는 key의 value를 msg에 저장
    msg = request.json['content']
    img_bool = False
    img_url = "https://24.media.tumblr.com/tumblr_lg902plO3R1qfyzelo1_500.jpg"
    
    if msg == "메뉴":
        menu = ["20층", "mulcam", "menu1", "menu2"]
        return_msg = random.choice(menu)
        
    elif msg == "로또":
        
        # lotto = random.sample(range(1,46), 6)
        # return_msg = "행운의 번호 : [{} {} {} {} {} {}]".format(lotto[0],lotto[1],lotto[2],lotto[3],lotto[4],lotto[5])
        
        # 1~45 list
        numbers = list(range(1,46))
        
        # sampling 6
        pick = random.sample(numbers, 6)
        
        # 정렬 후 string으로 변환하여 저장
        return_msg = str(sorted(pick))
        
    elif msg == "고양이":
        img_bool = True
        url = "https://api.thecatapi.com/v1/images/search?mime_types=jpg"
        res = requests.get(url).json()
        return_msg = "나만 고양이 없어:("
        img_url = res[0]['url']
        
    else:
        return_msg = "현재 메뉴만 지원합니다."
    
    message1 = {
        "text" : return_msg,
        "photo": {
            "url": img_url,
            "width": 640,
            "height": 480
        }
    }
    
    message2 = {
        "text" : return_msg,
    }
    
    
    keyboard = {
        "type" : "buttons",
        "buttons" : ["메뉴", "로또", "고양이", "영화"]
    }
    
    if(img_bool):
        res = {
            "message": message1,
            "keyboard": keyboard
        }
        
    else:
        res = {
            "message": message2,
            "keyboard": keyboard
        }
    
    return jsonify(res)
    
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
