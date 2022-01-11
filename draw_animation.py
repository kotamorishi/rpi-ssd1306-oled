# -*- coding: utf-8 -*-
# if the update is slow edit /boot/config.txt
# dtparam=i2c_arm=on,i2c_arm_baudrate=400000
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
from PIL import Image, ImageFont, ImageDraw, ImageOps
import time
import os


bootupSequence = ["b1","b2","b3","b3","b3", # wake up
    "s1","s2","s3","s4","s5","s6","s7","s8","s7","s6", # left-right
    "b4","b5","b6","b5","b4"]

scanSequence = ["b1","b2","b3","b3","b3", # wake up
    "s1","s2","s3","s4","s5","s6","s7","s8","s9","s8","s7","s6", # left-right
    "s11","s12","s13","s12","s11"] # blink]

imageXShift = {
    "s1":"0",
    "s2":"-4",
    "s3":"-6",
    "s4":"-6",
    "s5":"-4",
    "s6":"0",
    "s7":"4",
    "s8":"6",
    "s9":"6",
    "s10":"4",
    "s11":"0",
    "s12":"0",
    "s13":"0",
    "s14":"0",
    "s15":"0",
    "s16":"0",
}

class ssd1306_oled(object):
    def __init__(self, i2c_address=0x3C):
        self.serial = i2c(port=1, address=i2c_address)
        self.device = ssd1306(self.serial)
            
    def drawImage(self, filename):
        with canvas(self.device) as drawUpdate:
            scanBmp = Image.open(os.path.join("images",  filename + ".bmp"))
            drawUpdate.bitmap((self.imageShiftAmount(filename),5), scanBmp, fill=100)

    def imageShiftAmount(self, name):
        if(name[0] == "s"):
            return int(imageXShift[name])
        else:
            return 0

monitor = ssd1306_oled()

for filename in bootupSequence:
        monitor.drawImage(filename)
        time.sleep(0.03)

while True:
    for filename in scanSequence:
        monitor.drawImage(filename)
        time.sleep(0.03)
        
