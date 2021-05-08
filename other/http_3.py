import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
mode = GPIO.getmode()
GPIO.setup(25,GPIO.OUT)

from flask import Flask
app = Flask(__name__)

import time
from flask import request

@app.route('/', methods = ['GET'])

def index():
    my_led_status = request.args.get("led_status")
    
    if my_led_status == "0":
        GPIO.output(25,GPIO.LOW)
        return_string = 'off'
    if my_led_status == "1":
        GPIO.output(25,GPIO.HIGH)
        return_string = 'on'
    if my_led_status == "2":
        for i in range (0,5):
            GPIO.output(25,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(25,GPIO.LOW)
            time.sleep(0.5)
            return_string = 'loop5'
    return return_string

if __name__=='__main__':
    app.run()