from flask import Flask, request, jsonify
import os
import json

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
    
        
    message = {
        "text" : msg
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
