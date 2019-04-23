from Utils import DBConnector as DB
import serial
import time

try:
	Serials = dict()
	ser = serial.Serial(DB.DevicePath("MovingArduino"), 9600, timeout=None)	# todo путь для ардуины с датчиками
	time.sleep(2)
except:
	print("Error create serial")

while (True):
	while ser.inWaiting():
		text = ser.readline()
		DB.SensorsWrite(text)
