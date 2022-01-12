# rpi-ssd1306-oled
Example of how to use SSD1306 based OLED monitor

# Install libraries.
tbd...

# i2c bus speed setting
i2c bus speed is not so fast by default, You can update the settings with config.txt
```bash
/boot/config.txt
```

Original
```bash
dtparam=i2c_arm=on
```

400Khz
```bash
dtparam=i2c_arm=on,i2c_arm_baudrate=400000
```
