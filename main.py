import sys
import config as CF
import Utils.DBConnector as DB
import Utils.QueryUtils as QU
import Utils.TimeChecker as TC
import time

# F = open("time.txt", "r+")
# F.write(str(TC.TimeStart()))
# R=0
# t="123"
# while(R==0):
#   try:
#     F = open("time.txt", "r+")
#     F.write(str(TC.TimeStart()))
#     time.sleep(0.1)
#     t = F.read()
#     print(t)
#     StartTime = float(t)
#     R=1
#   except Exception as e:
#     print(e)
#     print(t)
#   finally:
#     F.close()

Actions = ["Start moving", "Activate experiment", "Atom collect", "Drop on libra", "Drop on field"]
ActionsTime = [CF.TimeStartMov, CF.TimeActivateExperiment, CF.TimeCollectAtoms, CF.TimeDropOnLibra, CF.TimeDropOnFields]
#===============================================================================
DB.DBConnect()
StartTime = float(DB.TimeCheck())

#print(StartTime)
while (not 1):
    time.sleep(0.1)
QU.QueryFill()

for i in range(len(Actions)):
  print(i)
  print(StartTime)
  while(not (QU.DoneCheck('query', Actions[i])) and ((TC.Time()-StartTime) <= ActionsTime[i])):
    print(TC.Time()-StartTime)
    print(QU.QueryMinId('query'))
    print()
    time.sleep(0.1)
  QU.QueryToLog('query', Actions[i])
  QU.QueryDelete('query', Actions[i])
print("FINISH")
# запуск первой фазы старта 
#while (not QU.DoneChek("") or TC.TimeCheck()<CF.TimeStartMov ):
#   time.sleep(0.1)
#QU.RemoveStartingMov()

#активация эксперимента
#while (not QU.DoneChek("") or TC.TimeCheck()<CF.TimeActivateExperiment ):
#    time.sleep(0.1)
#QU.RemoveActivateExperiment()

# сбор атомов
#while (not QU.DoneChek("") or TC.TimeCheck()<CF.TimeCollectAtoms ):
#    time.sleep(0.1)
#QU.RemoveCollectAtoms()

#сброс на весы
#while (not QU.DoneChek("") or TC.TimeCheck()<CF.TimeDropOnLibra ):
#    time.sleep(0.1)
#QU.RemoveDropOnLibra()

#сброс на поля
#while (not QU.DoneChek("") or TC.TimeCheck()<CF.TimeDropOnFields ):
#    time.sleep(0.1)
#QU.RemoveDropOnFields()
#===============================================================================
#predictor()
DB.Finish()
