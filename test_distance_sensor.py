import RPi.GPIO as GPIO
import time
import signal
import sys
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
Trig1 = 8	 # left
Echo1 = 10
Trig2 = 12	 # mid
Echo2 = 16
Trig3 = 18   # right
Echo3 = 22
print "start"
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
while 1:
	if distance(8,10) < 10:
		GPIO.output(in3,GPIO.HIGH)
        	GPIO.output(in3,GPIO.LOW)
        	time.sleep(1)
    	if distance(18,22) < 10:
    		GPIO.output(in1,GPIO.HIGH)
        	GPIO.output(in1,GPIO.LOW)
        	time.sleep(1)
    	if distance(8,10) < 5 and distance(18,22) < 5 and distance(12,16) > 10:
    		GPIO.output(in2,GPIO.LOW)
       		GPIO.output(in2,GPIO.HIGH)
		GPIO.output(in4,GPIO.LOW)
        	GPIO.output(in4,GPIO.HIGH)
        	time.sleep(2)
        	GPIO.output(in3,GPIO.HIGH)
        	GPIO.output(in3,GPIO.LOW)
		GPIO.output(in2,GPIO.LOW)
        	GPIO.output(in2,GPIO.HIGH)
        	time.sleep(1)
    	if distance(12,16) < 10:
    		if distane(8,10) < distane(18,22):
    			GPIO.output(in3,GPIO.HIGH)
        		GPIO.output(in3,GPIO.LOW)
        	elif distane(8,10) < distane(18,22):
        		GPIO.output(in1,GPIO.HIGH)
        		GPIO.output(in1,GPIO.LOW)
        	else
        		GPIO.output(in3,GPIO.HIGH)
        		GPIO.output(in3,GPIO.LOW)
	if distance(12,16) < 10 and distance(18,22) < 10:
		GPIO.output(in1,GPIO.HIGH)
        	GPIO.output(in1,GPIO.LOW)
		GPIO.output(in3,GPIO.LOW)
        	GPIO.output(in3,GPIO.HIGH)
        	time.sleep(1)
	if distance(12,16) < 10 and distance(8,10) < 10:
		GPIO.output(in3,GPIO.HIGH)
        	GPIO.output(in3,GPIO.LOW)
		GPIO.output(in2,GPIO.LOW)
        	GPIO.output(in2,GPIO.HIGH)
        	time.sleep(1)
	if distance(12,16) < 8 and distance(8,10) < 8 and distance(18,22) < 8:
		GPIO.output(in2,GPIO.LOW)
        	GPIO.output(in2,GPIO.HIGH)
		GPIO.output(in4,GPIO.LOW)
        	GPIO.output(in4,GPIO.HIGH)
GPIO.cleanup()


