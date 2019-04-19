import subprocess
import serial
#import Utils.DBConnector as DB
from Utils import DBConnector as DB
import time
try: #запуск последовательных портов на ардуинки и запись объектов в словарь
    Serials=dict()

    print(DB.DevicePath("MovingArduino"))
    Serials['Moving'] = serial.Serial(DB.DevicePath("MovingArduino"), 9600, timeout=None)
    time.sleep(2)
    print("serialPortToMovingArduinoCreatingSuccess")
    Serials['Sorted'] = serial.Serial(DB.DevicePath("SortedArduino"), 9600, timeout=None)
    time.sleep(2)
    print("serialPortToMovingArduinoCreatingSuccess")
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
#subprocess.check_output('echo '+Comand+' > '+PathToDevice, shell=True)