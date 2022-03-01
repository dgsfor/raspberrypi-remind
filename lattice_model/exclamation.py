# -*- coding: UTF-8 -*-
from rpi_ws281x import Color

"""
名称：感叹号
代码：exclamation
颜色：竖线黄色，点红色
"""
class exclamation(object):
    def __init__(self,strip):
        super(exclamation,self).__init__()
        self.strip = strip

    def turn_on(self):
        self.strip.setPixelColor(3, Color(255, 255, 0))
        self.strip.setPixelColor(4, Color(255, 255, 0))
        self.strip.setPixelColor(11, Color(255, 255, 0))
        self.strip.setPixelColor(12, Color(255, 255, 0))
        self.strip.setPixelColor(19, Color(255, 255, 0))
        self.strip.setPixelColor(20, Color(255, 255, 0))
        self.strip.setPixelColor(27, Color(255, 255, 0))
        self.strip.setPixelColor(28, Color(255, 255, 0))
        self.strip.setPixelColor(35, Color(255, 255, 0))
        self.strip.setPixelColor(36, Color(255, 255, 0))

        self.strip.setPixelColor(51, Color(255, 0, 0))
        self.strip.setPixelColor(52, Color(255, 0, 0))
        self.strip.setPixelColor(59, Color(255, 0, 0))
        self.strip.setPixelColor(60, Color(255, 0, 0))
    def turn_off(self):
        self.strip.setPixelColor(3, Color(0, 0, 0))
        self.strip.setPixelColor(4, Color(0, 0, 0))
        self.strip.setPixelColor(11, Color(0, 0, 0))
        self.strip.setPixelColor(12, Color(0, 0, 0))
        self.strip.setPixelColor(19, Color(0, 0, 0))
        self.strip.setPixelColor(20, Color(0, 0, 0))
        self.strip.setPixelColor(27, Color(0, 0, 0))
        self.strip.setPixelColor(28, Color(0, 0, 0))
        self.strip.setPixelColor(35, Color(0, 0, 0))
        self.strip.setPixelColor(36, Color(0, 0, 0))

        self.strip.setPixelColor(51, Color(0, 0, 0))
        self.strip.setPixelColor(52, Color(0, 0, 0))
        self.strip.setPixelColor(59, Color(0, 0, 0))
        self.strip.setPixelColor(60, Color(0, 0, 0))