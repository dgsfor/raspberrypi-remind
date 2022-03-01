# -*- coding: UTF-8 -*-
from rpi_ws281x import Color

"""
名称：禁止图形
代码：forbidden
颜色：红色
"""
class forbidden(object):
    def __init__(self,strip):
        super(forbidden,self).__init__()
        self.strip = strip

    def turn_on(self):
        # 第1行
        self.strip.setPixelColor(2, Color(255, 0, 0))
        self.strip.setPixelColor(3, Color(255, 0, 0))
        self.strip.setPixelColor(4, Color(255, 0, 0))
        self.strip.setPixelColor(5, Color(255, 0, 0))
        # 第2行
        self.strip.setPixelColor(9, Color(255, 0, 0))
        self.strip.setPixelColor(14, Color(255, 0, 0))
        # 第3行
        self.strip.setPixelColor(16, Color(255, 0, 0))
        self.strip.setPixelColor(18, Color(255, 0, 0))
        self.strip.setPixelColor(21, Color(255, 0, 0))
        self.strip.setPixelColor(23, Color(255, 0, 0))
        # 第4行
        self.strip.setPixelColor(24, Color(255, 0, 0))
        self.strip.setPixelColor(27, Color(255, 0, 0))
        self.strip.setPixelColor(28, Color(255, 0, 0))
        self.strip.setPixelColor(31, Color(255, 0, 0))
        # 第5行
        self.strip.setPixelColor(32, Color(255, 0, 0))
        self.strip.setPixelColor(35, Color(255, 0, 0))
        self.strip.setPixelColor(36, Color(255, 0, 0))
        self.strip.setPixelColor(39, Color(255, 0, 0))
        # 第6行
        self.strip.setPixelColor(40, Color(255, 0, 0))
        self.strip.setPixelColor(42, Color(255, 0, 0))
        self.strip.setPixelColor(45, Color(255, 0, 0))
        self.strip.setPixelColor(47, Color(255, 0, 0))
        # 第7行
        self.strip.setPixelColor(49, Color(255, 0, 0))
        self.strip.setPixelColor(54, Color(255, 0, 0))
        # 第8行
        self.strip.setPixelColor(58, Color(255, 0, 0))
        self.strip.setPixelColor(59, Color(255, 0, 0))
        self.strip.setPixelColor(60, Color(255, 0, 0))
        self.strip.setPixelColor(61, Color(255, 0, 0))
    def turn_off(self):
        # 第1行
        self.strip.setPixelColor(2, Color(0, 0, 0))
        self.strip.setPixelColor(3, Color(0, 0, 0))
        self.strip.setPixelColor(4, Color(0, 0, 0))
        self.strip.setPixelColor(5, Color(0, 0, 0))
        # 第2行
        self.strip.setPixelColor(9, Color(0, 0, 0))
        self.strip.setPixelColor(14, Color(0, 0, 0))
        # 第3行
        self.strip.setPixelColor(16, Color(0, 0, 0))
        self.strip.setPixelColor(18, Color(0, 0, 0))
        self.strip.setPixelColor(21, Color(0, 0, 0))
        self.strip.setPixelColor(23, Color(0, 0, 0))
        # 第4行
        self.strip.setPixelColor(24, Color(0, 0, 0))
        self.strip.setPixelColor(27, Color(0, 0, 0))
        self.strip.setPixelColor(28, Color(0, 0, 0))
        self.strip.setPixelColor(31, Color(0, 0, 0))
        # 第5行
        self.strip.setPixelColor(32, Color(0, 0, 0))
        self.strip.setPixelColor(35, Color(0, 0, 0))
        self.strip.setPixelColor(36, Color(0, 0, 0))
        self.strip.setPixelColor(39, Color(0, 0, 0))
        # 第6行
        self.strip.setPixelColor(40, Color(0, 0, 0))
        self.strip.setPixelColor(42, Color(0, 0, 0))
        self.strip.setPixelColor(45, Color(0, 0, 0))
        self.strip.setPixelColor(47, Color(0, 0, 0))
        # 第7行
        self.strip.setPixelColor(49, Color(0, 0, 0))
        self.strip.setPixelColor(54, Color(0, 0, 0))
        # 第8行
        self.strip.setPixelColor(58, Color(0, 0, 0))
        self.strip.setPixelColor(59, Color(0, 0, 0))
        self.strip.setPixelColor(60, Color(0, 0, 0))
        self.strip.setPixelColor(61, Color(0, 0, 0))