import Bot.Integrations.SendingComand as SC
import Utils.DBConnector as DB

MovingArduino = DB.DevicePath("MovingArduino")

def BuildMovingComand(Speed, Turn, Direction):

    if Speed<0: # проверка значений скорости и оборотов
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
        return BuildMovingComand_2(Speed, Turn, Direction) #вызов функции которая проверяет третье направление дввижение которое означает что скорость этих двигателей нужно выкртить в 0
    comand = 'M'
    for i in Direction:
        comand+='|'+i
    for i in range (4):
        comand+='|'+Speed
    for i in range (4):
        comand+='|'+Turn
    return comand

def BuildMovingComand_2(Speed, Turn, Direction):
    comand = 'M'
    for i in Direction:
        if i=='2':
            comand+='|'+'0'
        else:
            comand+='|'+i
    for i in Direction:
        if i=='2':
            comand+='|'+'0'
        else:
            comand+='|'+Speed
    for i in Direction:
        if i=='2':
            comand+='|'+'0'
        else:
            comand+='|'+Turn
    return comand

def ForwardMoving(Speed, Turn):  #принимаем скорость и обороты колеса
    Direction=['1','1','1','1']
    comand=BuildMovingComand(Speed,Turn,Direction)
    SC.SendComand(comand, MovingArduino)

def BackMoving(Speed,Turn):

    Direction=['0','0','0','0']
    comand=BuildMovingComand(Speed,Turn,Direction)
    SC.SendComand(comand, MovingArduino)

def LeftMoving(Speed,Turn):
    Direction=['0','1','1','0']
    comand=BuildMovingComand(Speed,Turn,Direction)
    SC.SendComand(comand, MovingArduino)

def RightMoving(Speed,Turn):
    Direction=['1','0','0','1']
    comand=BuildMovingComand(Speed,Turn,Direction)
    SC.SendComand(comand, MovingArduino)

def TurnLeftMoving(Speed,Turn):
    Direction=['0','1','0','1']
    comand=BuildMovingComand(Speed,Turn,Direction)
    SC.SendComand(comand, MovingArduino)

def TurnRightMoving(Speed,Turn):
    Direction=['1','0','1','0']
    comand=BuildMovingComand(Speed,Turn,Direction)
    SC.SendComand(comand, MovingArduino)

def ForwardLeftMoving(Speed,Turn):
    Direction=['2','1','1','2']
    comand=BuildMovingComand(Speed,Turn,Direction)
    SC.SendComand(comand, MovingArduino)

def ForwardRightMoving(Speed,Turn):
    Direction=['1','2','2','1']
    comand=BuildMovingComand(Speed,Turn,Direction)
    SC.SendComand(comand, MovingArduino)

def BackLeftMoving(Speed,Turn):
    Direction=['0','2','2','0']
    comand=BuildMovingComand(Speed,Turn,Direction)
    SC.SendComand(comand, MovingArduino)

def BackRightMoving(Speed,Turn):
    Direction=['2','0','0','2']
    comand=BuildMovingComand(Speed,Turn,Direction)
    SC.SendComand(comand, MovingArduino)
