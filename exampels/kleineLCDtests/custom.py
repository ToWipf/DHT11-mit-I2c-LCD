import I2C_LCD_driver
from time import *

mylcd = I2C_LCD_driver.lcd()

fontdata1 = [      
        [ 0b01010, 
          0b01010, 
          0b00000, 
          0b10001, 
          0b01110, 
          0b00000, 
          0b00000, 
          0b00000 ],
]

mylcd.lcd_load_custom_chars(fontdata1)
mylcd.lcd_write(0x80)
mylcd.lcd_write_char(0)

