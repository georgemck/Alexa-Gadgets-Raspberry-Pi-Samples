#sudo vi python_test/switchGPIO.py
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
print "LED on"
GPIO.output(2,GPIO.LOW)
GPIO.output(3,GPIO.LOW)
GPIO.output(4,GPIO.LOW)
time.sleep(7)
print "LED off"
GPIO.output(2,GPIO.HIGH)
GPIO.output(3,GPIO.HIGH)
GPIO.output(4,GPIO.HIGH)
time.sleep(7)
print "LED on"
GPIO.output(2,GPIO.LOW)
GPIO.output(3,GPIO.LOW)
GPIO.output(4,GPIO.LOW)
time.sleep(7)
print "LED off"
GPIO.output(2,GPIO.HIGH)
GPIO.output(3,GPIO.HIGH)
GPIO.output(4,GPIO.HIGH)