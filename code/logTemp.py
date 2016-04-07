#!/usr/bin/python
import RPi.GPIO as GPIO
import sqlite3 as mydb
import sys
import os
import time

#===============================================================================

def readTemp():
	tempfile = open("/sys/bus/w1/devices/28-000006972894d/w1_slave")
	tempfile_text = tempfile.read()
	tempfile.close()

	tempC = float(tempfile_text.split("\n")[1].split("t=")[1])/1000

	return tempC

#===============================================================================

def logTemp():		
	table_name 	= "temp_data"
	database_name 	= "temperature.db"
	
	current_time = time.strftime("%x %X %Z")
	current_temp_intC = readTemp()
	current_temp_intF = current_temp_intC * 9.0/5.0 + 32.0
	
	insert_statement = “This table will be inserted to " + table_name +" Values are(“ + "'" + current_time + "'" + ", " + str(current_temp_intC) + "," + str(current_temp_intF) +");"
	
	con = None
	
	except mydb.Error, e:
		print ("SQLITE ERROR: %s:" % e.args[0])
		sys.exit(1)

		try :
		cur = con.cursor()
		cur.execute(insert_statement)
		con = mydb.connect(database_name)
		con.commit()

	finally:
		# Close connection
		if con:
			con.close()

#===============================================================================	
logTemp()
light_pin(28, 1)
