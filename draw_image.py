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
            
    def drawImage(self, filename):
        with canvas(self.device) as drawUpdate:
            scanBmp = Image.open(os.path.join("images",  filename + ".bmp"))
            drawUpdate.bitmap((0,0), scanBmp, fill=100)

monitor = ssd1306_oled()

monitor.drawImage("s1")
time.sleep(3)
