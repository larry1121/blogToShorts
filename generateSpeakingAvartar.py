# -*- coding: utf-8 -*-
import requests
import time
import urllib.request

script_ko = "이 글은 인도 마을의 경제, 사회, 종교 및 정치 구조를 포함한 다양한 측면을 탐구한다. "

def generateSpeakingAvatar():
    url = "https://api.d-id.com/talks"

    payload = {
        "script": {
            "type": "text",
            "provider": {
                "type": "microsoft",
                "voice_id": "ko-KR-YuJinNeural", # 음성 종류
            },
            "ssml": "false",
            "input": script_ko # 스크립트
        },
        "config": {
            "fluent": "false",
            "pad_audio": "0.0"
        },
        "source_url": "https://d2u3dcdbebyaiu.cloudfront.net/uploads/atch_img/986/a6ce4b4aea6105f4097dce9769e914b5_res.jpeg"
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Bearer 본인의 베어러 키 입력"
    }

    response = requests.post(url, json=payload, headers=headers)
    print(response.json())
    print(response.text)


    time.sleep(60) # 영상이 생성될때까지 60초 정도 기다린다.
    #####################################################################
    url = f"https://api.d-id.com/talks/{response.json()['id']}"
    headers = {
        "accept": "application/json",
        "authorization": "Bearer 본인의 베어러 키 입력"
    }

    response = requests.get(url, headers=headers)

    print(response.text)

    urllib.request.urlretrieve(response.json()['result_url'], 'temp2/avatar.mp4') 

    return response.text


res = generateSpekingAvatar()
print(res)