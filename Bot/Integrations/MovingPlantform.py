#import Bot.Integrations.SendingComand as SC
#import Utils.DBConnector as DB
from Bot.Integrations import SendingComand as SC
from Utils import DBConnector as DB
import config as CF
import time
from Bot.Integrations import ArduinoCommunication as AC
#MovingArduino = DB.DevicePath("MovingArduino")
MovingArduino = CF.Devices[0][0]

def BuildMovingComand(Speed, Turn, Direction):
	if Speed < 0:	# проверка значений скорости и оборотов
		Speed = 0
	if Speed > 255:
		Speed = 255
	if Turn < 0:
		Turn = 0
	if Turn > 32000:
		Turn = 32000
	Speed = str(Speed)
	Turn = str(Turn)
	if '2' in Direction:
		return BuildMovingComand_2(Speed, Turn, Direction)  #вызов функции которая проверяет третье направление дввижение которое означает что скорость этих двигателей нужно выкртить в 0
	comand = 'M'
	for i in Direction:
		comand += '|' + i
	for i in range(4):
		comand += '|' + Speed
	for i in range(4):
		comand += '|' + Turn
	comand += '@'
	if CF.Debug > 0:
		print("BuildMovingComand" + str(comand))
	return comand

def BuildMovingComand_2(Speed, Turn, Direction):
	comand = 'M'
	for i in Direction:
		if i == '2':
			comand += '|' + '0'
		else:
			comand += '|' + i
	for i in Direction:
		if i == '2':
			comand += '|' + '0'
		else:
			comand += '|' + Speed
	for i in Direction:
		if i == '2':
			comand += '|' + '0'
		else:
			comand += '|' + Turn
	comand += "@"
	if CF.Debug > 0:
		print("BuildMovingComand_2" + str(comand))
	return comand

def ForwardMoving(Speed, Turn):  #принимаем скорость и обороты колеса
	Direction = ['1', '1', '1', '1']
	comand = BuildMovingComand(Speed, Turn, Direction)
	SC.SendComand(comand.encode(), MovingArduino)
	if CF.Debug > 0:
		print(comand)

def BackMoving(Speed, Turn):
	Direction = ['0', '0', '0', '0']
	comand = BuildMovingComand(Speed, Turn, Direction)
	SC.SendComand(comand.encode(), MovingArduino)
	if CF.Debug > 0:
		print(comand)

def LeftMoving(Speed, Turn):
	Direction = ['0', '1', '1', '0']
	comand = BuildMovingComand(Speed, Turn, Direction)
	SC.SendComand(comand.encode(), MovingArduino)
	if CF.Debug > 0:
		print(comand)

def RightMoving(Speed, Turn):
	Direction = ['1', '0', '0', '1']
	comand = BuildMovingComand(Speed, Turn, Direction)
	SC.SendComand(comand.encode(), MovingArduino)
	if CF.Debug > 0:
		print(comand)

def TurnLeftMoving(Speed, Turn):
	Direction = ['0', '1', '0', '1']
	comand = BuildMovingComand(Speed, Turn, Direction)
	SC.SendComand(comand.encode(), MovingArduino)
	if CF.Debug > 0:
		print(comand)

def TurnRightMoving(Speed, Turn):
	Direction = ['1', '0', '1', '0']
	comand = BuildMovingComand(Speed, Turn, Direction)
	SC.SendComand(comand.encode(), MovingArduino)
	if CF.Debug > 0:
		print(comand)

def ForwardLeftMoving(Speed, Turn):
	Direction = ['2', '1', '1', '2']
	comand = BuildMovingComand(Speed, Turn, Direction)
	SC.SendComand(comand.encode(), MovingArduino)
	if CF.Debug > 0:
		print(comand)

def ForwardRightMoving(Speed, Turn):
	Direction = ['1', '2', '2', '1']
	comand = BuildMovingComand(Speed, Turn, Direction)
	SC.SendComand(comand.encode(), MovingArduino)
	if CF.Debug > 0:
		print(comand)

def BackLeftMoving(Speed, Turn):
	Direction = ['0', '2', '2', '0']
	comand = BuildMovingComand(Speed, Turn, Direction)
	SC.SendComand(comand.encode(), MovingArduino)
	if CF.Debug > 0:
		print(comand)

def BackRightMoving(Speed, Turn):
	Direction = ['2', '0', '0', '2']
	comand = BuildMovingComand(Speed, Turn, Direction)
	SC.SendComand(comand.encode(), MovingArduino)
	if CF.Debug > 0:
		print(comand)

def ChekMoving (Comand):
	Comand = Comand.split()
	Comand[1] =int(Comand[1])
	Comand[2] = int(Comand[2])
	if Comand[0]== CF.ArduinoComands[0]:
		for i in range(Comand[1]//CF.Step):
			ReadyMotors(Comand[2])
			ForwardMoving(Comand[2],CF.Step)
		ReadyMotors(Comand[2])
		ForwardMoving(Comand[2],Comand[1]%CF.Step)
	elif Comand[0]== CF.ArduinoComands[1]:
		for i in range(Comand[1]//CF.Step):
			ReadyMotors(Comand[2])
			BackMoving(Comand[2],CF.Step)
		ReadyMotors(Comand[2])
		BackMoving(Comand[2],Comand[1]%CF.Step)
	elif Comand[0]== CF.ArduinoComands[2]:
		for i in range(Comand[1]//CF.Step):
			ReadyMotors(Comand[2])
			RightMoving(Comand[2],CF.Step)
		ReadyMotors(Comand[2])
		RightMoving(Comand[2],Comand[1]%CF.Step)
	elif Comand[0]== CF.ArduinoComands[3]:
		for i in range(Comand[1]//CF.Step):
			ReadyMotors(Comand[2])
			LeftMoving(Comand[2],CF.Step)
		ReadyMotors(Comand[2])
		LeftMoving(Comand[2],Comand[1]%CF.Step)
	elif Comand[0]== CF.ArduinoComands[4]:
		for i in range(Comand[1]//CF.Step):
			ReadyMotors(Comand[2])
			TurnRightMoving(Comand[2],CF.Step)
		ReadyMotors(Comand[2])
		TurnRightMoving(Comand[2],Comand[1]%CF.Step)
	elif Comand[0]== CF.ArduinoComands[5]:
		for i in range(Comand[1]//CF.Step):
			ReadyMotors(Comand[2])
			TurnLeftMoving(Comand[2],CF.Step)
		ReadyMotors(Comand[2])
		TurnLeftMoving(Comand[2],Comand[1]%CF.Step)
	elif Comand[0]== CF.ArduinoComands[6]:
		for i in range(Comand[1]//CF.Step):
			ReadyMotors(Comand[2])
			ForwardRightMoving(Comand[2],CF.Step)
		ReadyMotors(Comand[2])
		ForwardRightMoving(Comand[2],Comand[1]%CF.Step)
	elif Comand[0]== CF.ArduinoComands[7]:
		for i in range(Comand[1]//CF.Step):
			ReadyMotors(Comand[2])
			ForwardLeftMoving(Comand[2],CF.Step)
		ReadyMotors(Comand[2])
		ForwardLeftMoving(Comand[2],Comand[1]%CF.Step)
	elif Comand[0]== CF.ArduinoComands[8]:
		for i in range(Comand[1]//CF.Step):
			ReadyMotors(Comand[2])
			BackRightMoving(Comand[2],CF.Step)
		ReadyMotors(Comand[2])
		BackRightMoving(Comand[2],Comand[1]%CF.Step)
	elif Comand[0]== CF.ArduinoComands[9]:
		for i in range(Comand[1]//CF.Step):
			ReadyMotors(Comand[2])
			BackLeftMoving(Comand[2],CF.Step)
		ReadyMotors(Comand[2])
		BackLeftMoving(Comand[2],Comand[1]%CF.Step)

def ReadyMotors(Speed):
	StartTime = time.time()
	Delay=CF.Step/50
	if Delay > 0.05:
		Delay=0.05
	while not AC.ChekMotors():
		time.sleep(Delay)#todo Checksensors, check AI.
		if (time.time()-StartTime)>(CF.Step*3/Speed):
			AC.ArdReset()
			break
