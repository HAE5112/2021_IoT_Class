#7segment.py
import Rpio.GPIO as GPIO
import time

#GPIO 7개 핀번호 설정
#               A B C D E F G
SEGMENT_PINS = [2,3,4,5,6,7,8]

GPIO.setmode(GPIO.BCM)

for segment in SEGMENTPINS:
    GPIO.setup(segmet, GPIO.OUT)
    GPIO.output(segment, GPIO.LOW)

#Common Cathode (HIGH -> ON, LOW -> OFF)
data = [1,1,1,1,1,1,0]

try:
    for  in range(3): #0~2 (_값 쓸모없음)
        for i in range(len(SEGMENT_PINS)):
            GPIO.output(SEGMENT_PINS[i], data[i])

        time.sleep(1)

        for i in range(7):
            GPIO.ouput(SEGMENT_PINS[i], GPIO.LOW)
finally:
    GPIO.cleanup()
    print('cleanup and exit')