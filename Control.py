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
error = 0
si = GPIO.input(23)
s1 = GPIO.input(7)
s2 = GPIO.input(11)
s3 = GPIO.input(13)
s4 = GPIO.input(15)
s5 = GPIO.input(19)
# Funtions
def read_ir_sensor():
        #  1 0 0 0 0
        if (s1==0 and s2==1 and s3==1 and s4==1 and s5==1):
                error = 4
        #  1 1 0 0 0    
        elif (s1==0 and s2==0 and s3==1 and s4==1 and s5==1):
                error = 3
        #  0 1 0 0 0 
        elif (s1==1 and s2==0 and s3==1 and s4==1 and s5==1):
                error = 2
        #  0 1 1 0 0 
        elif (s1==1 and s2==1 and s3==0 and s4==1 and s5==1):
                error = 1
        # 0 0 1 0 0 
        elif (s1==1 and s2==1 and s3==0 and s4==1 and s5==1):  
                error = 0
        # 0 0 1 1 0
        elif (s1==1 and s2==1 and s3==0 and s4==0 and s5==1):
                error = -1
        # 0 0 0 1 0
        elif (s1==1 and s2==1 and s3==1 and s4==0 and s5==1):
                error = -2
        # 0 0 0 1 1
        elif (s1==1 and s2==1 and s3==1 and s4==0 and s5==0):
                error = -3
        # 0 0 0 0 1
        elif (s1==1 and s2==1 and s3==1 and s4==1 and s5==0):
                error = -4
        # 1 1 1 1 1
        elif (s1==0 and s2==0 and s3==0 and s4==0 and s5==0):
                error = 100
        # 0 0 0 0 0        
        elif (s1==1 and s2==1 and s3==1 and s4==1 and s5==1):
                error = 101
def forward(x,y):
        p2.ChangeDutyCycle(0)
        p1.ChangeDutyCycle(x)
        p3.ChangeDutyCycle(0)
        p4.ChangeDutyCycle(y)
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
p1 = GPIO.PWM(36, 100)
p2 = GPIO.PWM(37, 100)
p3 = GPIO.PWM(38, 100)
p4 = GPIO.PWM(40, 100)

p1.start(0)
p2.start(0)
p3.start(0)
p4.start(0)

while (1):
        read_ir_sensor()
        if distance(12,16)>10 and si==0: 
                if(error==4):
                        print("1 0 0 0 0")
                        forward(50,90)
                elif(error==3):
                        print("1 1 0 0 0")
                        forward(50,80)
                elif(error==2):
                        print("0 1 0 0 0")
                        forward(50,70)
                elif(error==1):
                        print("0 1 1 0 0")
                        forward(50,60)
                elif(error==0):
                        print("0 0 1 0 0")
                        forward(80,80)
                elif(error==-1):
                        print("0 0 1 1 0")
                        forward(60,50)        
                elif(error==-2):
                        print("0 0 0 1 0")
                        forward(70,50)
                elif(error==-3):
                        print("0 0 0 1 1")
                        forward(80,50)        
                elif(error==-4):
                        print("0 0 0 0 1")
                        forward(90,50)
                elif(error==100):# 0 0 0 0 0
                        print("stop")
                        stop()
                elif(error==101):# 1 1 1 1 1  
                        rightmode2(100)
                        time.sleep(3)
        else:
                stop()
