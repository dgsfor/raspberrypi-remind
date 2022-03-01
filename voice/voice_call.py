#coding=utf-8
import os,time
from aip import AipSpeech

# 别人的，免费的
baidu_aksk = {
    "appid": "15079673",
    "key": "mGxvq3Nwr3aVjD4UFIFGsaMD",
    "secret": "YIN3wxizj16zCRYZ6EGpdopuA6FwHRhB"
}

def say_something(string):
    client = AipSpeech(baidu_aksk["appid"], baidu_aksk["key"], baidu_aksk["secret"])
    result = client.synthesis(string, 'zh', 1, {
        'vol': 5,
    })
    print(result)
    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open('test.mp3', 'wb') as f:
            f.write(result)

    os.system("mplayer test.mp3")
    time.sleep(1)
    os.system("rm test.mp3 -rf")
