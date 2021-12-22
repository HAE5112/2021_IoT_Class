import RPi.GPIO as GPIO
import time

LED_PIN = 17
YELLOW_PIN = 27
GREEN_PIN = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(YELLOW_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)

while (1):
   GPIO.output(LED_PIN, GPIO.HIGH)
   print("led on")
   time.sleep(0.1)
   GPIO.output(LED_PIN, GPIO.LOW)
   print("led off")

   GPIO.output(YELLOW_PIN, GPIO.HIGH)
   print("yellow on")
   time.sleep(0.1   )
   GPIO.output(YELLOW_PIN, GPIO.LOW)
   print("yellow off")   

   GPIO.output(GREEN_PIN, GPIO.HIGH)
   print("green on")
   time.sleep(0.1)
   GPIO.output(GREEN_PIN, GPIO.LOW)
   print("green off")
 


GPIO.cleanup()