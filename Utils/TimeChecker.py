import time
from config import Debug as D

def Time():
	StartTime = time.time()
	if D > 0:
		print("Time" + str(StartTime))
	return StartTime

#def TimeCheck(StartTime):
#    return (time.time()-StartTime)

def TimeDate():
	if D > 0:
		print("TimeDate")
	return time.strftime("%d.%m.%y %H:%M:%S")
