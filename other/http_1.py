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

import time

@app.route('/<parm>', methods = ['GET'])
def index(parm):
    
    return_string = "1"
    
    if parm == "1":
        GPIO.output(25,GPIO.HIGH)
        return_string = parm
    else:
        GPIO.output(25,GPIO.LOW)
        return_string = parm
    return return_string

"""
from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello, World'
"""
if __name__=='__main__':
    app.run()

