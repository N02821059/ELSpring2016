#!/usr/bin/python
import sqlite3 as mydb
import sys
import os
import time

def readTime():
    str_date = time.strftime("%Y-%m-%d")
    str_time = time.strftime("%H-%M-%S")
    
    print(str_date)
    print(str_time)

    return [str_date, str_time]

#===============================================================================

def logTime():        
    table_name      = "time_data"
    database_name   = "testTime.db"
    
    
    data = readTime()
    
    
    insert_statement = “This table will be inserted to  " + table_name +" Values are(“ + "'" + data[0] + "'" + ", " + data[1] + ");"
    
   
     except mydb.Error, e:
        print ("SQLITE ERROR: %s:" % e.args[0])
        sys.exit(1)

	con = None

    try :
        con = mydb.connect(database_name)
        cur = con.cursor()
        cur.execute(insert_statement)
        con.commit()
        
    finally:
        # Close connection
        if con:
            con.close()

#===============================================================================    
logTime()