import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
mode = GPIO.getmode()
GPIO.setup(25,GPIO.OUT)

from flask import Flask
app = Flask(__name__)

import time
from flask import request
import threading

@app.route('/', methods = ['GET'])

def index():
    my_led_status = request.args.get("led_status")
    
    if my_led_status == "0":
        GPIO.output(25,GPIO.LOW)
    if my_led_status == "1":
        GPIO.output(25,GPIO.HIGH)
    if my_led_status == "2":
        while True:
            GPIO.output(25,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(25,GPIO.LOW)
            time.sleep(0.5)
    else:
        while True:
            GPIO.output(25,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(25,GPIO.LOW)
            time.sleep(0.1)

t = threading.Thread(target = index)
t.start()

while True:
    my_led_status = request.args.get("led_status")
    if my_led_status == "0":
        return_string = 'off'
    if my_led_status == "1":
        return_string = 'on'
    if my_led_status == "2":
        return_string = '1s_loop'
    else:
        return_string = 'status_id_error'
    return return_string

t.join()


if __name__=='__main__':
    app.run()
    
"""
import threading
import time

def job():
    for i in range(5):
        print("Child thread:", i)
        time.sleep(1)
        
t = threading.Thread(target = job)
    
t.start()
    
for i in range(2):
    print("Main thread:", i)
    time.sleep(1)
    
t.join()
    
print("Done.")
"""