import RPi.GPIO as GPIO
import time
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
Trig1 = 8	# left
Echo1 = 10
Trig2 = 12	# mid
Echo2 = 16
Trig3 = 18   	# right
Echo3 = 22
#LCD
scl = 5
sda = 3
#main
while True:
	if distance(12,16)>10:
		if GPIO.input(s1):# turn left
			GPIO.output(in1,GPIO.HIGH)
			time.sleep(1)
			GPIO.output(in1,GPIO.LOW)
			#forward
			GPIO.output(in1,GPIO.HIGH)
			GPIO.output(in1,GPIO.LOW)
			GPIO.output(in3,GPIO.HIGH)
			GPIO.output(in3,GPIO.LOW)

		if GPIO.input(s2):# turn left
			GPIO.output(in1,GPIO.HIGH)
			time.sleep(1)
			GPIO.output(in1,GPIO.LOW)
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

		if GPIO.input(s4):# turn right
			GPIO.output(in3,GPIO.HIGH)
			time.sleep(1)
			GPIO.output(in3,GPIO.LOW)
			#forward
			GPIO.output(in1,GPIO.HIGH)
			GPIO.output(in1,GPIO.LOW)
			GPIO.output(in3,GPIO.HIGH)
			GPIO.output(in3,GPIO.LOW)

		if GPIO.input(s5):# turn right
			GPIO.output(in3,GPIO.HIGH)
			GPIO.output(in3,GPIO.LOW)
			time.sleep(1)
			#forward
			GPIO.output(in1,GPIO.HIGH)
			GPIO.output(in1,GPIO.LOW)
			GPIO.output(in3,GPIO.HIGH)
			GPIO.output(in3,GPIO.LOW)
	else
		if distance(8,10)>distance(18,22)
			turnleft(2)
			forward(2)
			turnright(2)
			forward(2)
		else
			turnright(2)
			forward(2)
			turnleft(2)
			forward(2)
def turnleft(x)
	GPIO.output(in1,GPIO.HIGH)
	time.sleep(x)
	GPIO.output(in1,GPIO.LOW)
def turnright(x)
	GPIO.output(in3,GPIO.HIGH)
	time.sleep(x)
	GPIO.output(in3,GPIO.LOW)
def forward(x)
	GPIO.output(in1,GPIO.HIGH)
	time.sleep(x)
	GPIO.output(in1,GPIO.LOW)
	GPIO.output(in3,GPIO.HIGH)
	time.sleep(x)
	GPIO.output(in3,GPIO.LOW)
def backward(x)
	GPIO.output(in2,GPIO.HIGH)
	time.sleep(x)
	GPIO.output(in2,GPIO.LOW)
	GPIO.output(in4,GPIO.HIGH)
	time.sleep(x)
	GPIO.output(in4,GPIO.LOW)
def distance(Trig,Echo):
	GPIO.setup(Trig, GPIO.OUT)
	GPIO.output(Trig,0)
	GPIO.setup(Echo, GPIO.IN)
	time.sleep(1)#
	GPIO.output(Trig,1)
	time.sleep(0.00001)
	GPIO.output(Trig,0)
	while GPIO.input(Echo) == 0:
		    start = time.time()
	while GPIO.input(Echo) == 1:
		    stop = time.time()
	dis = (stop - start)*17150
	dis - round(dis,2)
	print "stop"
	return dis
GPIO.cleanup()






























