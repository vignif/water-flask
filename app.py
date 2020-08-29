# pump specs
pin = 21
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

# flask specs
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html')
    if request.method == 'POST':
        if 'on' in request.form:
            #call function to turn the pump ON
            message = "Turn the pump ON"
            GPIO.output(pin, True)

        if 'off' in request.form:
            #call function to turn the pump OFF
            message = "Turn the pump OFF"
            GPIO.output(pin, False)

        return render_template('home.html', message = message)
    # return render_template('home.html')
