import subprocess
import serial
#import Utils.DBConnector as DB
from Utils import DBConnector as DB
import time
try:
    print(DB.DevicePath("MovingArduino"))
    serMov = serial.Serial(DB.DevicePath("MovingArduino"), 9600, timeout=None)
    time.sleep(2)
    print("serialPortToMovingArduinoCreatingSuccess")
    serSort = serial.Serial(DB.DevicePath("SortedArduino"), 9600, timeout=None)
    time.sleep(2)
    print("serialPortToMovingArduinoCreatingSuccess")
except Exception as err:
    print(err)
def SendComand(Comand, Ard):
    if Ard=="Moving":
        serMov.write(Comand)
    elif Ard=="Sorted":
        serSort.write(Comand)
#subprocess.check_output('echo '+Comand+' > '+PathToDevice, shell=True)