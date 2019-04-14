import subprocess
import serial
import Utils.DBConnector as DB
import time

ser = serial.Serial(DB.DevicePath("MovingArduino"), 9600, timeout=None)
time.sleep(2)

def SendComand(Comand, PathToDevice):
    ser.write(Comand)
    #subprocess.check_output('echo '+Comand+' > '+PathToDevice, shell=True)
