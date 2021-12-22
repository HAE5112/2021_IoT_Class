from flask import Flask
import RPi.GPIO as GPIO
import time

BLUE_LED_PIN= 23
LED_PIN = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BLUE_LED_PIN, GPIO.OUT)

app = Flask(__name__)

@app.route("/")
def hello():

    return '''
        <p>Hello, Flask!!</p>
        <a href="/led/red/on">RED LED ON</a>
        <a href="/led/red/off">RED LED OFF</a><br>
        <a href="/led/blue/on">BLUE LED ON</a>
        <a href="/led/blue/off">BLUE LED OFF</a>
    '''
@app.route("/led/red/<cmd>")
def led_red(cmd):
    print(cmd)
    if cmd == "on":
        GPIO.output(LED_PIN, GPIO.HIGH)
        return '''
            <p>RED LED ON</p>
            <a href="/">Go Home</a>
        '''
    elif cmd == "off":
        GPIO.output(LED_PIN, GPIO.LOW)
        return '''
            <p>RED LED OFF</p>
            <a href="/">Go Home</a>
        '''

@app.route("/led/blue/<cmd>")
def led_blue(cmd):
    print(cmd)
    if cmd == "on":
        GPIO.output(BLUE_LED_PIN, GPIO.HIGH)
        return '''
            <p>BLUE LED ON</p>
            <a href="/">Go Home</a>
        '''
    elif cmd == "off":
        GPIO.output(BLUE_LED_PIN, GPIO.LOW)
        return '''
            <p>BLUE LED OFF</p>
            <a href="/">Go Home</a>
        '''

if __name__ == "__main__":
    try:
        app.run(host = "0.0.0.0")
    finally:
        GPIO.cleanup()