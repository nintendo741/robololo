#import Utils.QueryUtils as QU
#import Utils.DBConnector as DB
from Utils import QueryUtils as QU
from Utils import DBConnector as DB
from Bot.Integrations import MovingPlantform as MP
import time
import  config as CF
from Bot.Integrations import ArduinoCommunication as AC
#опрос железа
#порты TTY, где Ардуино
#ACM на все порты
DB.DBConnect()
ArduinoComands = ['F 600 100', 'L 200 100', 'TL 100 100', 'L 600 100', 'TL 100 100', 'R 200 100', 'TR 200 100']
for i in ArduinoComands:
	QU.QueryWrite('queryArduino', i)

def ChekStatus ():
	Action = QU.QueryMinId('queryArduino')
	if (QU.QueryStatusCheck('queryArduino', Action) == 1):
		QU.QueryStatusChange('queryArduino', Action, 2)
		#StartPhase(Action)
	elif(QU.QueryStatusCheck('queryArduino', Action) == 3):
		QU.QueryToLog('queryArduino', Action)
		QU.QueryDelete('queryArduino', Action)
	time.sleep(0.1)
	if (False):
		QU.QueryStatusChange('queryArduino', Action, 3)

while (True):
	for i in ArduinoComands:
		MP.ChekMoving(i)

DB.Finish()
AC.GPIODown()
if CF.Debug > 0:
	print("Programm end")

# из Бд брать очередь
#     если статус 1, изменить на 2(в процессе)
# фунция действа
#     Если выполнено, статус 3
# СЕЛЕКТ по МИН индексу для проверки действия
