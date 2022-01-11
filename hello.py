# -*- coding: utf-8 -*-
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
from PIL import Image, ImageFont, ImageDraw, ImageOps
import time
import os

class ssd1306_oled(object):
    def __init__(self, i2c_address=0x3C):
        self.serial = i2c(port=1, address=i2c_address)
        self.device = ssd1306(self.serial)
        self.ttf = '/usr/share/fonts/truetype/noto/NotoMono-Regular.ttf'
        self.font = ImageFont.truetype(self.ttf, 32)
            
    def drawMessage(self, message):
        print(message)
        with canvas(self.device) as drawUpdate:
            drawUpdate.text((7, 2), message , font=self.font, fill=100)

monitor = ssd1306_oled()

monitor.drawMessage("Hey")
time.sleep(1)

text = "Hello"
for i in range(1, len(text) + 1):
    monitor.drawMessage(text[:i])
    time.sleep(0.3)

time.sleep(3)