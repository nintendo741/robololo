import sqlite3
import sys
from Utils import QueryUtils as QU
from Utils import LogUtils as LU
from Utils import TimeChecker as TC
from Tests import CheckDevices as CD
import config as CF
TimeGame = 100
D = CF.Debug

def TablesCreate():
	try:
		conn = sqlite3.connect('database1.db')
		dbsess = conn.cursor()
		dbsess.execute("""CREATE TABLE IF NOT EXISTS query 
				(id INTEGER PRIMARY KEY NOT NULL, 
				time text NOT NULL, 
				command text NOT NULL, 
				status integer NOT NULL);""")  #1 - wait, 2 - in progress, 3 - sucseful, 0 - error
		dbsess.execute("""CREATE TABLE IF NOT EXISTS queryArduino 
				(id INTEGER PRIMARY KEY NOT NULL, 
				time text NOT NULL, 
				command text NOT NULL, 
				status integer NOT NULL);""")  #1 - wait, 2 - in progress, 3 - sucseful, 0 - error
		dbsess.execute("""CREATE TABLE IF NOT EXISTS log 
				(id INTEGER PRIMARY KEY NOT NULL, 
				time text NOT NULL, 
				log text NOT NULL);""")
		dbsess.execute("""CREATE TABLE IF NOT EXISTS startTime
				(time text NOT NULL);""")
		dbsess.execute("""INSERT INTO startTime
				VALUES('%s');"""%(TC.Time()))		# todo сделать после ожидания начала движения
		dbsess.execute("""CREATE TABLE IF NOT EXISTS devices
				(id INTEGER PRIMARY KEY NOT NULL,
				device text NOT NULL,
				path text NOT NULL);""")
		for i in range(len(CF.Devices)):
			dbsess.execute("""INSERT INTO devices (device, path)
					VALUES('%s', '%s');"""%(CF.Devices[i][0], CD.DevicePath(CF.Devices[i][1])))
			sel = next(dbsess.execute("""SELECT device || ' ' || path FROM devices WHERE (device = '%s')"""%(CF.Devices[i][0])))[0]
			dbsess.execute("""INSERT INTO log (time, log) VALUES('%s', '%s');""" %(TC.TimeDate(), sel))
		dbsess.execute("""CREATE TABLE IF NOT EXISTS json
				(id INTEGER PRIMARY KEY NOT NULL,
				frameid integer NOT NULL,
				type float NOT NULL,
				score float NOT NULL,
				ymin float NOT NULL,
				ymax float NOT NULL,
				xmin float NOT NULL,
				xmax float NOT NULL);""")
		dbsess.execute("""CREATE TABLE IF NOT EXISTS sensors
				(id INTEGER PRIMARY KEY NOT NULL,
				data text NOT NULL);""")
		conn.commit()
		if D > 0:
			print("TableCreate")
	except sqlite3.Error as e:
		if conn:
			conn.rollback()
		print("Error %s:" % e.args[0])
		sys.exit(1)
	finally:
		if conn:
			conn.close()

def JsonWrite(frameid, type, score, ymin, ymax, xmin, xmax):
	try:
		conn = sqlite3.connect('database1.db')
		dbsess = conn.cursor()
		dbsess.execute("""INSERT INTO json(frameid, type, score, ymin, ymax, xmin, xmax)
			VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s');""" %(frameid, type, score, ymin, ymax, xmin, xmax))
		conn.commit()
	except sqlite3.Error as e:
		if conn:
			conn.rollback()
		print("Error %s:" % e.args[0])
		sys.exit(1)
	finally:
		if conn:
			conn.close()

def SensorsWrite(text):
	try:
		conn = sqlite3.connect('database1.db')
		dbsess = conn.cursor()
		dbsess.execute("""INSERT INTO sensors
		VALUES('%s');""" %(text))
		conn.commit()
	except sqlite3.Error as e:
		if conn:
			conn.rollback()
		print("Error %s:" % e.args[0])
		sys.exit(1)
	finally:
		if conn:
			conn.close()

def Finish():
	try:
		conn = sqlite3.connect('database1.db')
		dbsess = conn.cursor()
		LU.LogSave()    #save Log to file
		dbsess.execute("""DROP TABLE query;""")
		dbsess.execute("""DROP TABLE queryArduino;""")
		dbsess.execute("""DROP TABLE log;""")
		dbsess.execute("""DROP TABLE startTime;""")
		dbsess.execute("""DROP TABLE devices;""")
		dbsess.execute("""DROP TABLE json;""")
		dbsess.execute("""DROP TABLE sensors;""")
		conn.commit()
		if D > 0:
			print("Finish")
	except sqlite3.Error as e:
		if conn:
			conn.rollback()
		print("Error %s:" % e.args[0])
		sys.exit(1)
	finally:
		if conn:
			conn.close()

def DBConnect():
	try:
		conn = sqlite3.connect('database1.db')
		dbsess = conn.cursor()
		TablesCreate()
		conn.commit()
		if D > 0:
			print("DBConnect")
	except sqlite3.Error as e:
		if conn:
			conn.rollback()
		print("Error %s:" % e.args[0])
		sys.exit(1)
	finally:
		if conn:
			conn.close()

def TimeCheck():
	try:
		conn = sqlite3.connect('database1.db')
		dbsess = conn.cursor()
		st = next(dbsess.execute("""SELECT time FROM startTime;"""))[0]
		#t = TC.Time() - st
		conn.commit()
		if D > 0:
			print("TimeCheck:" + str(st))
		return st
	except sqlite3.Error as e:
		if conn:
			conn.rollback()
		print("Error %s:" % e.args[0])
		sys.exit(1)
	finally:
		if conn:
			conn.close()

def DevicePath(device):
	try:
		conn = sqlite3.connect('database1.db')
		dbsess = conn.cursor()
		st = next(dbsess.execute("""SELECT path FROM devices WHERE(device = '%s');"""%(device)))[0]
		conn.commit()
		if D > 0:
			print("DevicePath" + str(device) + str(st))
		return st
	except sqlite3.Error as e:
		if conn:
			conn.rollback()
		print("Error %s:" % e.args[0])
		sys.exit(1)
	finally:
		if conn:
			conn.close()

#QU.QueryWrite("test text")
#LU.LogWrite("test log text 1")
#QU.QueryToLog("test text")
#QU.QueryStatusChange("test text", 3)
#print(QU.QueryStatusCheck("test text"))
#LU.LogWrite("test log text 2")
#QU.QueryToLog("test text")
#QU.QueryDelete("test text", 3)
