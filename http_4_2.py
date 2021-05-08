import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
mode = GPIO.getmode()
GPIO.setup(25,GPIO.OUT)

from flask import Flask
app = Flask(__name__)

import time
from flask import request
import threading

global stop_loop

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
        global stop_loop
        if stop_loop == 2:
            break
        GPIO.output(25,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(25,GPIO.LOW)
        time.sleep(0.1)

@app.route('/', methods = ['GET'])
def index():
    global stop_loop
    my_led_status = request.args.get("led_status")
    if my_led_status == "0":
        stop_loop = 2
        return_string = 'off'
        off_t = threading.Thread(target = off)
        off_t.start()
    elif my_led_status == "1":
        stop_loop = 2
        return_string = 'on'
        on_t = threading.Thread(target = on)
        on_t.start()
    elif my_led_status == "2":
        stop_loop = 2
        return_string = 'loop_5'
        loop_5_t = threading.Thread(target = loop_5)
        loop_5_t.start()
    else:
        stop_loop = 1
        return_string = 'status_id_error'
        error_t = threading.Thread(target = error)
        error_t.start()
        
    return return_string

if __name__=='__main__':
    global stop_loop
    stop_loop = 2
    app.run()
