import time, sys
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
En_pins      = [32, 33] 
Motor_pins   = [36, 37, 38, 40] 
Encoder_pins = [24, 26]
Irss_pins = [7, 11, 13, 15, 19]
for i in Irss_pins:
        GPIO.setup(i,GPIO.IN)
#sonar sensor pin: 8,10 left // 12,16 mid \\ 18,22 right
for i in En_pins:
        GPIO.setup(i,GPIO.OUT)
        GPIO.output(i,GPIO.HIGH)
for i in Motor_pins:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i,GPIO.LOW)
for i in Encoder_pins:
        GPIO.setup(i, GPIO.IN)
GPIO.setup(23, GPIO.IN)
def forward(x):
        p2.ChangeDutyCycle(0)
        p1.ChangeDutyCycle(x)
        p3.ChangeDutyCycle(0)
        p4.ChangeDutyCycle(x)
def reverse(x):
        p1.ChangeDutyCycle(0)
        p2.ChangeDutyCycle(x)
        p4.ChangeDutyCycle(0)
        p3.ChangeDutyCycle(x)
def stop():
        p1.ChangeDutyCycle(0)
        p2.ChangeDutyCycle(0)
        p3.ChangeDutyCycle(0)
        p4.ChangeDutyCycle(0)
def turnleft(x):
        p1.ChangeDutyCycle(0)
        p2.ChangeDutyCycle(0)
        p3.ChangeDutyCycle(0)
        p4.ChangeDutyCycle(x)
def turnright(x):
        p2.ChangeDutyCycle(0)
        p1.ChangeDutyCycle(x)
        p3.ChangeDutyCycle(0)
        p4.ChangeDutyCycle(0)
def leftmode2(x):
        p1.ChangeDutyCycle(0)
        p2.ChangeDutyCycle(x)
        p3.ChangeDutyCycle(0)
        p4.ChangeDutyCycle(x)
def rightmode2(x):
        p4.ChangeDutyCycle(0)
        p3.ChangeDutyCycle(x)
        p2.ChangeDutyCycle(0)
        p1.ChangeDutyCycle(x)
def distance(Trig,Echo):
        GPIO.setup(Trig, GPIO.OUT)
        GPIO.output(Trig,0)
        GPIO.setup(Echo, GPIO.IN)
        time.sleep(1)
        GPIO.output(Trig,1)
        time.sleep(0.00001)
        GPIO.output(Trig,0)
        while GPIO.input(Echo) == 0:
                    start = time.time()
        while GPIO.input(Echo) == 1:
                    stop = time.time()
        dis = (stop - start)*17150
        dis - round(dis,2)
        return dis      
p1 = GPIO.PWM(36, 1000)
p2 = GPIO.PWM(37, 1000)
p3 = GPIO.PWM(38, 1000)
p4 = GPIO.PWM(40, 1000)

p1.start(0)
p2.start(0)
p3.start(0)
p4.start(0)
x=100

while (1):
         if distance(12,16)>10 and GPIO.input(23)==0: 
                        if GPIO.input(7) == 0:
                                print("tleft2")
                                leftmode2(x)
                        elif GPIO.input(11)  == 0:
                                print("turnleft")
                                turnleft(x)
                        elif GPIO.input(13) == 0:
                                print("s3 forward")
                                forward(x)
                        elif GPIO.input(15) == 0:
                                print("turnright")
                                turnright(x)
                        elif GPIO.input(19) == 0:
                                print("tright2")
                                rightmode2(x)
                        elif GPIO.input(7)==0 and GPIO.input(11)==0 and GPIO.input(13)==0 and GPIO.input(15)==0 and GPIO.input(19)==0:
                                stop() 
                        elif GPIO.input(7)==1 and GPIO.input(11)==1 and GPIO.input(13)==1 and GPIO.input(15)==1 and GPIO.input(19)==1:
                                stop()
        else:
                stop()
