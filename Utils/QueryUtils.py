import sqlite3
import sys
#import Utils.TimeChecker as TC
from Utils import TimeChecker as TC

def QueryWrite(que, com):
	if (que == 'query') or (que == 'queryArduino'):
		try:
			conn = sqlite3.connect('database1.db')
			dbsess = conn.cursor()
			qwe = """INSERT INTO %s(time, command, status) VALUES('%s', '%s', '%d');""" %(que, TC.TimeDate(), com, 1)
			dbsess.execute(qwe)
			conn.commit()
		except sqlite3.Error as e:
			if conn:
				conn.rollback()
			print ("Error %s:" % e.args[0])
			sys.exit(1)
		finally:
			if conn:
				conn.close()
	else:
		print("Error, '%s' - is not query table"%(que))
		sys.exit(1)

def QueryDelete(que, com):
	if (que == 'query') or (que == 'queryArduino'):
		try:
			conn = sqlite3.connect('database1.db')
			dbsess = conn.cursor()
			qwe = """DELETE FROM %s WHERE (command = '%s');""" %(que, com)
			dbsess.execute(qwe)
			conn.commit()
		except sqlite3.Error as e:
			if conn:
				conn.rollback()
			print ("Error %s:" % e.args[0])
			sys.exit(1)
		finally:
			if conn:
				conn.close()
	else:
		print("Error, '%s' - is not query table"%(que))
		sys.exit(1)

def QueryStatusChange(que, com, st):
	if (que == 'query') or (que == 'queryArduino'):
		try:
			conn = sqlite3.connect('database1.db')
			dbsess = conn.cursor()
			dbsess.execute("""UPDATE %s SET status = '%d' WHERE (command = '%s');""" %(que, st, com))
			conn.commit()
		except sqlite3.Error as e:
			if conn:
				conn.rollback()
			print ("Error %s:" % e.args[0])
			sys.exit(1)
		finally:
			if conn:
				conn.close()
	else:
		print("Error, '%s' - is not query table"%(que))
		sys.exit(1)

def QueryStatusCheck(que, com):
	if (que == 'query') or (que == 'queryArduino'):
		try:
			conn = sqlite3.connect('database1.db')
			dbsess = conn.cursor()
			st = next(dbsess.execute("""SELECT status FROM %s WHERE (command = '%s');""" %(que, com)))[0]
			conn.commit()
			return st
		except sqlite3.Error as e:
			if conn:
				conn.rollback()
			print ("Error %s:" % e.args[0])
			sys.exit(1)
		finally:
			if conn:
				conn.close()
	else:
		print("Error, '%s' - is not query table"%(que))
		sys.exit(1)

def QueryToLog(que, com):
	if (que == 'query') or (que == 'queryArduino'):
		try:
			conn = sqlite3.connect('database1.db')
			dbsess = conn.cursor()
			temp = """SELECT time || ' ' || command || ' ' || status FROM %s WHERE (command = '%s')""" %(que, com)
			sel = next(dbsess.execute(temp))
			sel = sel[0]
			qwe ="""INSERT INTO log (time, log) VALUES('%s', '%s');""" %(TC.TimeDate(), sel)
			#qwe2="""INSERT INTO log (time, log) VALUES('%s', (SELECT ('time' || ' ' || 'command' || ' ' || 'status') FROM query WHERE command = '%s'))""" %( TC.TimeDate(), com)
			#qwe3="""INSERT INTO log (time, log) VALUES('%s', "GROUP_CONCAT( SELECT (time, command, status) FROM query WHERE command = '%s')")""" %( TC.TimeDate(), com)
			dbsess.execute(qwe)
			conn.commit()
		except sqlite3.Error as e:
			if conn:
				conn.rollback()
			print ("Error %s:" % e.args[0])
			sys.exit(1)
		finally:
			if conn:
				conn.close()
	else:
		print("Error, '%s' - is not query table"%(que))
		sys.exit(1)

def QueryFill():
	try:
		conn = sqlite3.connect('database1.db')
		dbsess = conn.cursor()
		QueryWrite("Start moving")
		QueryWrite("Activate experiment")
		QueryWrite("Atom collect")
		QueryWrite("Drop on libra")
		QueryWrite("Drop on field")
		conn.commit()
	except sqlite3.Error as e:
		if conn:
			conn.rollback()
		print ("Error %s:" % e.args[0])
		sys.exit(1)
	finally:
		if conn:
			conn.close()

def DoneCheck(que, com):
	if (que == 'query') or (que == 'queryArduino'):
		try:
			conn = sqlite3.connect('database1.db')
			dbsess = conn.cursor()
			if (QueryStatusCheck(que, com) == 3):
				return 1
			else:
				return 0
			conn.commit()
		except sqlite3.Error as e:
			if conn:
				conn.rollback()
			print ("Error %s:" % e.args[0])
			sys.exit(1)
		finally:
			if conn:
				conn.close()
	else:
		print("Error, '%s' - is not query table"%(que))
		sys.exit(1)

def QueryMinId(que):
	if (que == 'query') or (que == 'queryArduino'):
		try:
			conn = sqlite3.connect('database1.db')
			dbsess = conn.cursor()
			st = next(dbsess.execute("""SELECT command FROM %s WHERE (id = (SELECT MIN(id) FROM query));"""%(que)))[0]
			conn.commit()
			return st
		except sqlite3.Error as e:
			if conn:
				conn.rollback()
			print("Error %s:" % e.args[0])
			sys.exit(1)
		finally:
			if conn:
				conn.close()
	else:
		print("Error, '%s' - is not query table"%(que))
		sys.exit(1)
