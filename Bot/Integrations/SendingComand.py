import subprocess
import serial
import Utils.DBConnector as DB
import time

serMov = serial.Serial(DB.DevicePath("MovingArduino"), 9600, timeout=None)
time.sleep(2)
serSort = serial.Serial(DB.DevicePath("SortedArduino"), 9600, timeout=None)
time.sleep(2)

def SendComand(Comand, Ard):
    if Ard=="Moving":
        serMov.write(Comand)
    elif Ard=="Sorted":
        serSort.write(Comand)
    #subprocess.check_output('echo '+Comand+' > '+PathToDevice, shell=True)
