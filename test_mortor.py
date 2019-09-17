import RPi.GPIO as GPIO
from time import sleep
in1 = 40
in2 = 38
in3 = 37
in4 = 36
enA = 32
enB = 33
GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(enA,GPIO.OUT)
GPIO.setup(enB,GPIO.OUT)

GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)

GPIO.output(in1,GPIO.HIGH)
time.sleep(5)
GPIO.output(in1,GPIO.LOW)

GPIO.output(in3,GPIO.HIGH)
time.sleep(5)
GPIO.output(in3,GPIO.LOW)

GPIO.output(in2,GPIO.LOW)
time.sleep(5)
GPIO.output(in2,GPIO.HIGH)

GPIO.output(in4,GPIO.LOW)
time.sleep(5)
GPIO.output(in4,GPIO.HIGH)
