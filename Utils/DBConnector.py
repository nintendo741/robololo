import sqlite3
import sys
#import Utils.QueryUtils as QU
from Utils import QueryUtils as QU
#import Utils.LogUtils as LU
from Utils import LogUtils as LU
#import Utils.TimeChecker as TC
from Utils import TimeChecker as TC
#import Tests.CheckDevices as CD
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
                status integer NOT NULL);""")
		#1 - wait, 2 - in progress, 3 - sucseful, 0 - error
		dbsess.execute("""CREATE TABLE IF NOT EXISTS queryArduino 
                (id INTEGER PRIMARY KEY NOT NULL, 
                time text NOT NULL, 
                command text NOT NULL, 
                status integer NOT NULL);""")
		#1 - wait, 2 - in progress, 3 - sucseful, 0 - error
		dbsess.execute("""CREATE TABLE IF NOT EXISTS log 
                (id INTEGER PRIMARY KEY NOT NULL, 
                time text NOT NULL, 
                log text NOT NULL);""")
		dbsess.execute("""CREATE TABLE IF NOT EXISTS startTime
                (time text NOT NULL);""")
		dbsess.execute("""INSERT INTO startTime
                VALUES('%s');"""%(TC.Time()))
		dbsess.execute("""CREATE TABLE IF NOT EXISTS devices
                (id INTEGER PRIMARY KEY NOT NULL,
                device text NOT NULL,
                path text NOT NULL);""")
		dbsess.execute("""INSERT INTO devices (device, path)
                VALUES('MovingArduino', '%s');"""%(CD.DevicePath(CF.MovingArduinoId)))
		dbsess.execute("""INSERT INTO devices (device, path)
                VALUES('SortedArduino', '%s');"""%(CD.DevicePath(CF.SortedArduinoId)))
		sel = next(dbsess.execute("""SELECT device || ' ' || path FROM devices WHERE (device = 'MovingArduino')"""))[0]
		dbsess.execute("""INSERT INTO log (time, log) VALUES('%s', '%s');""" %(TC.TimeDate(), sel))
		sel = next(dbsess.execute("""SELECT device || ' ' || path FROM devices WHERE (device = 'SortedArduino')"""))[0]
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
		print ("Error %s:" % e.args[0])
		sys.exit(1)
	finally:
		if conn:
			conn.close()

def JsonWrite(frameid, type, score, ymin, ymax, xmin, xmax):
	try:
		conn = sqlite3.connect('database1.db')
		dbsess = conn.cursor()
		dbsess.execute("""INSERT INTO json
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
		print ("Error %s:" % e.args[0])
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
		print ("Error %s:" % e.args[0])
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
		print ("Error %s:" % e.args[0])
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
		print ("Error %s:" % e.args[0])
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
