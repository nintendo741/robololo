import subprocess
import serial
import config as CF
#import Utils.DBConnector as DB
from Utils import DBConnector as DB
import time

try: #запуск последовательных портов на ардуинки и запись объектов в словарь
    Serials = dict()
    for i in range(len(CF.Devices)):
        if CF.Debug>0:
            print(DB.DevicePath(CF.Devices[i][0]))
        Serials[CF.Devices[i][0]] = serial.Serial(DB.DevicePath(CF.Devices[i][0]), 9600, timeout=None)
        time.sleep(2)
        #print("serialPortToMovingArduinoCreatingSuccess")
        #Serials['Sorted'] = serial.Serial(DB.DevicePath("SortedArduino"), 9600, timeout=None)
        #time.sleep(2)
        #print("serialPortToMovingArduinoCreatingSuccess")
    if CF.Debug > 0:
        print("Serial ports creating success on",DB.DevicePath(CF.Devices[i][0]))
except Exception as err:
    print(err)
def InitPort(): #only Moving
    if CF.Debug > 0:
        print("Reinitializing Serial port")
    Serials[CF.Devices[i][0]] = serial.Serial(DB.DevicePath(CF.Devices[i][0]), 9600, timeout=None)
    time.sleep(2)
def DropPort(Ard):
    if CF.Debug > 0:
        print("Drop port")
    Serials[Ard].close()
def ReadComand(Ard):
    data = None
    starttime = time.time()
    while data == None and (time.time() - starttime) < 0.2:
        while Serials[Ard].inWaiting():
            data = Serials[Ard].readline()
            data = data.decode()

    return data
def SendComand(Comand, Ard):
    Comand = Comand.encode()
    Serials[Ard].write(Comand)
    if CF.Debug > 0:
        print("comand send=",Comand)
        #print('wait 1 second')
        #time.sleep(1)

    #subprocess.check_output('echo '+Comand+' > '+PathToDevice, shell=True)