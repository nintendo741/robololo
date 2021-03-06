import sqlite3
import sys
#import Utils.TimeChecker as TC
from Utils import TimeChecker as TC
from config import Debug as D

def LogWrite(txt):
	try:
		conn = sqlite3.connect('database1.db')
		dbsess = conn.cursor()
		qwe="""INSERT INTO log(time, log) VALUES('%s', '%s');""" %(TC.TimeDate(), txt)
		dbsess.execute(qwe)
		conn.commit()
		if D > 0:
			print("LogWrite" + str(txt))
	except sqlite3.Error as e:
		if conn:
			conn.rollback()
		print ("Error %s:" % e.args[0])
		sys.exit(1)
	finally:
		if conn:
			conn.close()

def LogSave():
	try:
		conn = sqlite3.connect('database1.db')
		dbsess = conn.cursor()
		name = TC.TimeDate()
		dbsess.execute("""CREATE TABLE '%s' (id INTEGER PRIMARY KEY, time text NOT NULL, log text);""" %(name))
		dbsess.execute("""INSERT INTO '%s' SELECT * FROM log;"""%(name))
		conn.commit()
		if D > 0:
			print("LogSave")
	except sqlite3.Error as e:
		if conn:
			conn.rollback()
		print ("Error %s:" % e.args[0])
		sys.exit(1)
	finally:
		if conn:
			conn.close()
