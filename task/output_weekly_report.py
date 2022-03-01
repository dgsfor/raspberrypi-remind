# -*- coding: UTF-8 -*-

"""
输出运营周报
task_name : output_weekly_report
"""

import time
from voice import voice_call

def output_weekly_report(model_name,strip,whether_voice):
    FLASHING_COUNT = 10      # led灯闪烁次数
    FLASHING_INTERVAL = 0.2 # 闪烁间隔,200ms
    count = 0
    while 1:
        count = count + 1
        time.sleep(FLASHING_INTERVAL)
        strip.begin()
        model_name.turn_on()
        strip.show()
        time.sleep(FLASHING_INTERVAL)
        model_name.turn_off()
        strip.show()
        if count >= FLASHING_COUNT:
            break
    if whether_voice:
        voice_call.say_something("李彬，早上好，请按时输出稳定性运营周报，谢谢")