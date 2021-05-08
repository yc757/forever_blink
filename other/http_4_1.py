import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
mode = GPIO.getmode()
GPIO.setup(25,GPIO.OUT)

from flask import Flask
app = Flask(__name__)

import time
from flask import request
import threading

global off, on, loop_5, error
def off():
    GPIO.output(25,GPIO.LOW)
def on():
    GPIO.output(25,GPIO.HIGH)
def loop_5():
    for i in range (0,5):
        GPIO.output(25,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(25,GPIO.LOW)
        time.sleep(0.5)
def error():
    while True:
        GPIO.output(25,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(25,GPIO.LOW)
        time.sleep(0.1)

@app.route('/', methods = ['GET'])
def index():
    global off, on, loop_5, error, my_led_status
    my_led_status = request.args.get("led_status")
    if my_led_status == "0":
        return_string = 'off'
        off_t = threading.Thread(target = off)
        off_t.start()
    elif my_led_status == "1":
        return_string = 'on'
        on_t = threading.Thread(target = on)
        on_t.start()
    elif my_led_status == "2":
        return_string = '1s_loop'
        loop_5_t = threading.Thread(target = loop_5)
        loop_5_t.start()
    else:
        return_string = 'status_id_error'
        error_t = threading.Thread(target = error)
        error_t.start()
        if my_led_status == "0" or "1" or "2":
            return request.args.get("led_status")
        
    return return_string

if __name__=='__main__':
    global off, on, loop_5, error, my_led_status
    app.run()
