from lcd import drivers
import time 
import datetime
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
PIN = 4
display = drivers.Lcd()

try:
    print("Waiting to Display")
    while True:
        now = datetime.datetime.now()
        display.lcd_display_string(now.strftime("%x%X"),1)
        humidity, temperature = Adafruit_DHT.read_retry(sensor,PIN)
        #if humidity is not None and temperature is not None:
        print(f"Temperature={temperature:.1f}C, Humidity:{humidity:.1f}%")
        display.lcd_display_string("{:.1f}'C {:.1f}%".format(temperature,humidity),2)


finally:
    print("Clean Up!")
    display.lcd_clear()