#coding=utf-8
import os,time
from aip import AipSpeech

# 这里不去实现获取token的方法了，很简单，参考官方文档：https://cloud.baidu.com/doc/SPEECH/s/0k38y8mfh
# token有效期为30天
# baidu_aksk = {
#     "appid": "25681779",
#     "key": "BSwBhGGIrfTGAVFjlQeQ8U30",
#     "secret": "DT8yGkGEUKL0EIkcGmbNvnNerqcB2bjE",
#     "token": "24.77e073061a336974ff2827b60c9b2712.2592000.1648692311.282335-25681779"
# }

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
