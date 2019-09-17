import RPi.GPIO as GPIO
from time import sleep
in1 = 40
in2 = 38
in3 = 37
in4 = 36
enA = 32
enB = 33
temp1=1
GPIO.setmode(GPIO.BCM)
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
print("\n")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")

while(1):

    x=raw_input()

    if x=='r':
        print("run")
        if(temp1==1):
		    GPIO.output(in1,GPIO.HIGH)
		    GPIO.output(in1,GPIO.LOW)
		 	GPIO.output(in3,GPIO.HIGH)
		    GPIO.output(in3,GPIO.LOW)
		    print("forward")
		    x='z'
        else:
		    GPIO.output(in2,GPIO.LOW)
		    GPIO.output(in2,GPIO.HIGH)
			GPIO.output(in4,GPIO.LOW)
		    GPIO.output(in4,GPIO.HIGH)
		    print("backward")
		    x='z'


    elif x=='s':
        print("stop")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
		GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        x='z'

    elif x=='f':
        print("forward")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in1,GPIO.LOW)
		GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in3,GPIO.LOW)
        temp1=1
        x='z'

    elif x=='b':
        print("backward")
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
		GPIO.output(in4,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
        temp1=0
        x='z'

    elif x=='l':
        print("low")
        p.ChangeDutyCycle(25)
        x='z'

    elif x=='m':
        print("medium")
        p.ChangeDutyCycle(50)
        x='z'

    elif x=='h':
        print("high")
        p.ChangeDutyCycle(75)
        x='z'
    elif x=='l1':
		print("left mode 1")
		GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in1,GPIO.LOW)
    elif x=='r1':
		print("right mode 1")
		GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in3,GPIO.LOW)
    elif x=='l2':
		print("left mode 2")
		GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in1,GPIO.LOW)
		GPIO.output(in4,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
    elif x=='r2':
		print("right mode 2")
		GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in3,GPIO.LOW)
		GPIO.output(in2,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)

    elif x=='e':
        GPIO.cleanup()
        print("GPIO Clean up")
        break

    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")
