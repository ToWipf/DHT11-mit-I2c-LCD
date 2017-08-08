import RPi.GPIO as GPIO
#import AdafruitDHT
import I2C_LCD_driver
import sys
import Adafruit_DHT

from time import *

mylcd = I2C_LCD_driver.lcd()

mylcd.lcd_display_string("Start")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

while True:
    
    instance = Adafruit_DHT.read_retry(11, 4)
    result = instance

    print (instance)
    mylcd.lcd_display_string("Temp: %d%s C " % (instance[1], chr(223)), 1)
    mylcd.lcd_display_string("Humidity: %d %% " % instance[0], 2)
