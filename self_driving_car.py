import RPi.GPIO as GPIO
import time
from time import sleep
import signal
import sys
GPIO.setmode(GPIO.BOARD)
#motor
in1 = 40
in2 = 38
in3 = 37
in4 = 36
enA = 32
enB = 33
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
p=GPIO.PWM(enA,1000)
p=GPIO.PWM(enB,1000)
p.start(25)
#irsensor
s1 = 7
s2 = 11
s3 = 13
s4 = 15
s5 = 19
GPIO.setup(s1,GPIO.IN)
GPIO.setup(s2,GPIO.IN)
GPIO.setup(s3,GPIO.IN)
GPIO.setup(s4,GPIO.IN)
GPIO.setup(s5,GPIO.IN)
#sssensor
trig1 = 8
echo1 = 10
trig2 = 12
echo2 = 16
trig3 = 18
echo3 = 22
GPIO.setup(pinTrigger, GPIO.OUT)
GPIO.setup(pinEcho, GPIO.IN)
#LCD
scl = 5
sda = 3
#main
while True:
	if GPIO.input(s1):#left
		GPIO.output(in1,GPIO.HIGH)
		time.sleep(1)
       		GPIO.output(in1,GPIO.LOW)
       		#forward
       		GPIO.output(in1,GPIO.HIGH)
	    	GPIO.output(in1,GPIO.LOW)
	 	GPIO.output(in3,GPIO.HIGH)
	    	GPIO.output(in3,GPIO.LOW)

	if GPIO.input(s2):
		GPIO.output(in1,GPIO.HIGH)
       		GPIO.output(in1,GPIO.LOW)
       		time.sleep(1)
       		#forward
       		GPIO.output(in1,GPIO.HIGH)
	    	GPIO.output(in1,GPIO.LOW)
	 	GPIO.output(in3,GPIO.HIGH)
	    	GPIO.output(in3,GPIO.LOW)

	if GPIO.input(s3):#forward
		GPIO.output(in1,GPIO.HIGH)
	    	GPIO.output(in1,GPIO.LOW)
	 	GPIO.output(in3,GPIO.HIGH)
	    	GPIO.output(in3,GPIO.LOW)

	if GPIO.input(s4):#right
		GPIO.output(in3,GPIO.HIGH)
       		GPIO.output(in3,GPIO.LOW)
       		time.sleep(1)
       		#forward
       		GPIO.output(in1,GPIO.HIGH)
	    	GPIO.output(in1,GPIO.LOW)
	 	GPIO.output(in3,GPIO.HIGH)
	    	GPIO.output(in3,GPIO.LOW)

	if GPIO.input(s5):
		GPIO.output(in3,GPIO.HIGH)
       		GPIO.output(in3,GPIO.LOW)
       		time.sleep(1)
       		#forward
       		GPIO.output(in1,GPIO.HIGH)
	    	GPIO.output(in1,GPIO.LOW)
	 	GPIO.output(in3,GPIO.HIGH)
	    	GPIO.output(in3,GPIO.LOW)
GPIO.cleanup()






























