import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.IN)
GPIO.setup(11,GPIO.IN)
GPIO.setup(13,GPIO.IN)
GPIO.setup(15,GPIO.IN)
GPIO.setup(19,GPIO.IN)
# 1 -> 5 trai qua phai
while True:
	if GPIO.input(7):
		print "1"
	if GPIO.input(11):
		print "2"
	if GPIO.input(13):
		print "3"
	if GPIO.input(15):
		print "4"
	if GPIO.input(19):
		print "5"
GPIO.cleanup()
