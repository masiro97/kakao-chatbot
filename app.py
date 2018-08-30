from flask import Flask, request, jsonify
import os
import json
import random

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
        
    else:
        return_msg = "현재 메뉴만 지원합니다."
        
    message = {
        "text" : return_msg
    }
    
    keyboard = {
        "type" : "buttons",
        "buttons" : ["메뉴", "로또", "고양이", "영화"]
    }

    res = {
        "message": message,
        "keyboard": keyboard
    }
    
    return jsonify(res)
    
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
