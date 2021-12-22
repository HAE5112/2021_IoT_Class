#작은별  출력하기
import RPi.GPIO as GPIO
import time

SEGMENT_PINS = [3,2,9,10,22,27,17]
GPIO.setmode(GPIO.BCM)

for segment in SEGMENT_PINS :
    GPIO.setup(segment,GPIO.OUT)
    GPIO.output(segment,GPIO.LOW)

data = [[1, 1, 1, 1, 1, 0, 1],  #0
        [0, 1, 1, 0, 0, 0, 0],  #1
        [1, 1, 0, 1, 1, 1, 0],  #2
        [1, 1, 1, 1, 0, 1, 0],  #3
        [0, 1, 1, 0, 0, 1, 1],  #4
        [1, 0, 1, 1, 0, 1, 1],  #5
        [1, 0, 1, 1, 1, 1, 1],  #6
        [1, 1, 1, 0, 0, 0, 0],  #7
        [1, 1, 1, 1, 1, 1, 1],  #8
        [1, 1, 1, 0, 0, 1, 1]]  #9

LED_PIN = 14
YELLOW_PIN = 15
GREEN_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(YELLOW_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)

BUZZER_PIN = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# 주파수 설정 (262Hz)
pwm = GPIO.PWM(BUZZER_PIN, 262)
pwm.start(10) # duty cycle (0 ~10)
num=0
#작은별  #도 262 #레 294 #미 330 #파 349 #솔 392 #라 440 #시 494 #도 523
melody = [262,262,392,392,440,440,392,349,349,330,330,294,294,262,392,392,349,349,330,330,294,392,392,349,349,330,330,294,262,262,392,392,440,440,392,349,349,330,330,294,294,262]
         # 도  도  솔  솔  라  라  솔  파   파  미  미  레  레  도   솔  솔   파  파 미  미  레   솔 솔  파  파  미   미  레  도  도   솔  솔  라  라  솔  파  파  미  미  레  레  도
try:
    for i in melody:
        pwm.ChangeFrequency(i)
        time.sleep(0.1)
        
        GPIO.output(LED_PIN, GPIO.HIGH)
        print("led on")
        time.sleep(1)
        GPIO.output(LED_PIN, GPIO.LOW)
        print("led off")

        GPIO.output(YELLOW_PIN, GPIO.HIGH)
        print("yellow on")
        time.sleep(1)
        GPIO.output(YELLOW_PIN, GPIO.LOW)
        print("yellow off")   

        GPIO.output(GREEN_PIN, GPIO.HIGH)
        print("green on")
        time.sleep(1)
        GPIO.output(GREEN_PIN, GPIO.LOW)
        print("green off")
        pwm.ChangeFrequency(12)
        for j in range(7):
            GPIO.output(SEGMENT_PINS[j], data[num%10][j])
        num += 1



finally:
    pwm.stop()
    GPIO.cleanup()  