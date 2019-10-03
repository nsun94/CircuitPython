import board
import digitalio
import pulseio
lcd_rs = digitalio.DigitalInOut(board.D7)
lcd_en = digitalio.DigitalInOut(board.D8)
lcd_d5 = digitalio.DigitalInOut(board.D10)
lcd_d4 = digitalio.DigitalInOut(board.D9)
red = pulseio.PWMOut(board.D3)
green = pulseio.PWMOut(board.D5)
blue = pulseio.PWMOut(board.D6)
lcd_columns = 16
lcd_rows = 2
import adafruit_character_lcd.character_lcd as characterlcd
lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)