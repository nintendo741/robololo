import Utils.QueryUtils as QU
import time

MovingArduinoPath = 0

#опрос железа
#порты TTY, где Ардуино
#ACM на все порты

while(True):
    Action = QU.QueryMinId('queryArduino')
    if (QU.QueryStatusCheck('queryArduino', Action) == 1):
      QU.QueryStatusChange('queryArduino', Action, 2)
    elif(QU.QueryStatusCheck('queryArduino', Action) == 3):
        QU.QueryToLog('queryArduino', Action)
        QU.QueryDelete('queryArduino', Action)
    time.sleep(0.1)
    if (False):
        QU.QueryStatusChange('queryArduino', Action, 3)


# из Бд брать очередь
#     если статус 1, изменить на 2(в процессе)
# фунция действа
#     Если выполнено, статус 3
# СЕЛЕКТ по МИН индексу для проверки действия
