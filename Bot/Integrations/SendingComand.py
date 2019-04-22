import subprocess
import serial
from config import Debug as D
#import Utils.DBConnector as DB
from Utils import DBConnector as DB
import time

try: #запуск последовательных портов на ардуинки и запись объектов в словарь
    Serials=dict()
    #print(DB.DevicePath("MovingArduino"))
    Serials['Moving'] = serial.Serial(DB.DevicePath("MovingArduino"), 9600, timeout=None)
    time.sleep(2)
    #print("serialPortToMovingArduinoCreatingSuccess")
    Serials['Sorted'] = serial.Serial(DB.DevicePath("SortedArduino"), 9600, timeout=None)
    time.sleep(2)
    #print("serialPortToMovingArduinoCreatingSuccess")
    if D > 0:
        print("Serial ports creating success")
except Exception as err:
    print(err)

def ReadComand(Ard):
    data=None
    starttime=time.time()
    while data==None and (time.time() - starttime) < 1:
        while Serials[Ard].inWaiting():
            data = Serials[Ard].readline()

    return data
def SendComand(Comand, Ard):
    Serials[Ard].write(Comand)
    if D > 0:
        print(Comand)
#subprocess.check_output('echo '+Comand+' > '+PathToDevice, shell=True)