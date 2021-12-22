from flask import Flask
from flask.templating import render_template
import RPi.GPIO as GPIO

app = Flask(__name__)
LED_PIN1 = 22
LED_PIN2 = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN1,GPIO.OUT)
GPIO.setup(LED_PIN2,GPIO.OUT)

@app.route("/")
def home():
    return render_template("led_task.html")

@app.route("/led/<op>")
def led(op):
    if op == "Ron":
        GPIO.output(LED_PIN1, GPIO.HIGH)
        return "RED LED ON"
    elif op == "Roff":
        GPIO.output(LED_PIN1, GPIO.LOW)
        return "RED LED OFF"
    elif op == "Bon":
        GPIO.output(LED_PIN2, GPIO.HIGH)
        return "BLUE LED ON"
    elif op == "Boff":
        GPIO.output(LED_PIN2, GPIO.LOW)
        return "BLUE LED OFF"

if __name__ == "__main__":
    try:
        app.run(host = "0.0.0.0")
    finally:
        GPIO.cleanup()