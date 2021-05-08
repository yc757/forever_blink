"""
from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello, World'

if __name__=='__main__':
    app.run()
"""
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
mode = GPIO.getmode()
GPIO.setup(25,GPIO.OUT)

from flask import Flask
app = Flask(__name__)

@app.route('/led_on')
def led_on():
    GPIO.output(25,GPIO.HIGH)
    return 'LED_ON'

@app.route('/led_off')
def led_off():
    GPIO.output(25,GPIO.LOW)
    return 'LED_OFF'

if __name__=='__main__':
    app.run()
