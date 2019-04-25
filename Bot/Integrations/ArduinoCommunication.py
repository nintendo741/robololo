import RPi.GPIO as GPIO
import config as CF
from Bot.Integrations import SendingComand as SC
import time




GPIO.setmode(GPIO.BCM)
GPIO.setup(CF.GPIOPins[0], GPIO.OUT)#объявление пинов заданных из конфига
GPIO.setup(CF.GPIOPins[1], GPIO.IN)
GPIO.setup(CF.GPIOPins[2], GPIO.IN)
GPIO.setup(CF.GPIOPins[3], GPIO.IN)
GPIO.setup(CF.GPIOPins[4], GPIO.IN)

print('GPIO initialization complete')

def ArdReset():
	if CF.Debug>0:
		print("send reset signal to arduino")
	GPIO.output(CF.GPIOPins[0], True)
	time.sleep(0.1)
	GPIO.output(CF.GPIOPins[0], False)
	response = None
	while response != "Ready":
		if CF.Debug>0:
			print("waiting Arduino boot")
		response=SC.ReadComand(CF.Devices[0][0])
	if CF.Debug>0:
		print("reset complete")
def GPIODown():
	GPIO.cleanup()
	print("GPIO down complete")

def ChekMotors():
	MotorValue=0
	for i in range(4):
		MotorValue+=GPIO.input(CF.GPIOPins[i+1])
	return (MotorValue == 4)












