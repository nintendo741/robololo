import time

def Time():
	StartTime = time.time()
	return StartTime

#def TimeCheck(StartTime):
#    return (time.time()-StartTime)

def TimeDate():
	return time.strftime("%d.%m.%y %H:%M:%S")
