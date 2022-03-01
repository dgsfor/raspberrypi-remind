# -*- coding: UTF-8 -*-
from rpi_ws281x import Color

"""
名称：笑脸图形
代码：smile
颜色：黄色
"""
class smile(object):
    def __init__(self,strip):
        super(smile,self).__init__()
        self.strip = strip

    def turn_on(self):
        self.strip.setPixelColor(2, Color(255, 255, 0))
        self.strip.setPixelColor(3, Color(255, 255, 0))
        self.strip.setPixelColor(4, Color(255, 255, 0))
        self.strip.setPixelColor(5, Color(255, 255, 0))

        self.strip.setPixelColor(9, Color(255, 255, 0))
        self.strip.setPixelColor(14, Color(255, 255, 0))

        self.strip.setPixelColor(16, Color(255, 255, 0))
        self.strip.setPixelColor(18, Color(255, 255, 0))
        self.strip.setPixelColor(21, Color(255, 255, 0))
        self.strip.setPixelColor(23, Color(255, 255, 0))

        self.strip.setPixelColor(24, Color(255, 255, 0))
        self.strip.setPixelColor(31, Color(255, 255, 0))

        self.strip.setPixelColor(32, Color(255, 255, 0))
        self.strip.setPixelColor(34, Color(255, 255, 0))
        self.strip.setPixelColor(37, Color(255, 255, 0))
        self.strip.setPixelColor(39, Color(255, 255, 0))

        self.strip.setPixelColor(40, Color(255, 255, 0))
        self.strip.setPixelColor(43, Color(255, 255, 0))
        self.strip.setPixelColor(44, Color(255, 255, 0))
        self.strip.setPixelColor(47, Color(255, 255, 0))

        self.strip.setPixelColor(49, Color(255, 255, 0))
        self.strip.setPixelColor(54, Color(255, 255, 0))

        self.strip.setPixelColor(58, Color(255, 255, 0))
        self.strip.setPixelColor(59, Color(255, 255, 0))
        self.strip.setPixelColor(60, Color(255, 255, 0))
        self.strip.setPixelColor(61, Color(255, 255, 0))
    def turn_off(self):
        self.strip.setPixelColor(2, Color(0, 0, 0))
        self.strip.setPixelColor(3, Color(0, 0, 0))
        self.strip.setPixelColor(4, Color(0, 0, 0))
        self.strip.setPixelColor(5, Color(0, 0, 0))

        self.strip.setPixelColor(9, Color(0, 0, 0))
        self.strip.setPixelColor(14, Color(0, 0, 0))

        self.strip.setPixelColor(16, Color(0, 0, 0))
        self.strip.setPixelColor(18, Color(0, 0, 0))
        self.strip.setPixelColor(21, Color(0, 0, 0))
        self.strip.setPixelColor(23, Color(0, 0, 0))

        self.strip.setPixelColor(24, Color(0, 0, 0))
        self.strip.setPixelColor(31, Color(0, 0, 0))

        self.strip.setPixelColor(32, Color(0, 0, 0))
        self.strip.setPixelColor(34, Color(0, 0, 0))
        self.strip.setPixelColor(37, Color(0, 0, 0))
        self.strip.setPixelColor(39, Color(0, 0, 0))

        self.strip.setPixelColor(40, Color(0, 0, 0))
        self.strip.setPixelColor(43, Color(0, 0, 0))
        self.strip.setPixelColor(44, Color(0, 0, 0))
        self.strip.setPixelColor(47, Color(0, 0, 0))

        self.strip.setPixelColor(49, Color(0, 0, 0))
        self.strip.setPixelColor(54, Color(0, 0, 0))

        self.strip.setPixelColor(58, Color(0, 0, 0))
        self.strip.setPixelColor(59, Color(0, 0, 0))
        self.strip.setPixelColor(60, Color(0, 0, 0))
        self.strip.setPixelColor(61, Color(0, 0, 0))
