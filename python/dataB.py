import mysql.connector 
from datetime import datetime

def connect():
    return mysql.connector.connect(
        host="localhost",          
        user="root",               
        password="",               
        database="parking_Db"       
    )

def checkAvailability():
    con = connect()
    cur = con.cursor()
    cur.execute("SELECT spaceNo FROM customer_tb")
    rows = cur.fetchall()
    con.close()
    return rows

def addRec(spaceNo, customerName, vehicleType, plateNo, entry_time):
    con = connect()
    cur = con.cursor()
    cur.execute("""INSERT INTO customer_tb(spaceNo, customerName, vehicleType, plateNo, 
                checkTime) VALUES (%s, %s, %s, %s, %s);""", 
                (spaceNo, customerName, vehicleType, plateNo, entry_time))
    con.commit()
    con.close()

def checkDuplicate():
    con = connect()
    cur = con.cursor()
    cur.execute("SELECT spaceNo from customer_tb")
    row = cur.fetchall()
    con.close()
    return row

def addToHistory(spaceId, customerName, vehicleType, plateNo, entry_time, exitTime, parkingFee):
    con = connect()
    cur = con.cursor()
    cur.execute("""INSERT INTO History(spaceId, customerName, vehicleType, plateNo, 
                entryTime, exitTime, parkingFee) VALUES (%s, %s, %s, %s, %s, %s, %s);""", 
                (spaceId, customerName, vehicleType, plateNo, entry_time, exitTime, parkingFee))
    con.commit()
    con.close()

def showHistory():
    con = connect()
    cur = con.cursor()
    cur.execute("SELECT * FROM History")
    rows = cur.fetchall()
    con.close()
    return rows

def showData():
    con = connect()
    cur = con.cursor()
    cur.execute("UPDATE customer_tb SET exitTime = NOW() WHERE spaceNo IS NOT NULL")
    cur.execute("SELECT * FROM customer_tb")
    rows = cur.fetchall()
    con.close()
    return rows

def getSpaceNo():
    con = connect()
    cur = con.cursor()
    cur.execute("SELECT spaceNo FROM customer_tb")
    spNo = [row[0] for row in cur.fetchall()]
    con.close()
    return spNo

def deleteRec(spaceNo):
    con = connect()
    cur = con.cursor()
    cur.execute("DELETE FROM customer_tb WHERE spaceNo = %s", (spaceNo,))
    con.commit()
    con.close()

def searchData(spaceNo="", customerName="", plateNo=""):
    con = connect()
    cur = con.cursor()
    cur.execute("SELECT * FROM customer_tb WHERE spaceNo = %s OR customerName = %s OR plateNo = %s", (spaceNo, customerName, plateNo))
    rows = cur.fetchall()
    con.close()
    return rows

def dataUpdate(totalFee, spaceNo):
    con = connect()
    cur = con.cursor()
    cur.execute("""
        UPDATE customer_tb 
        SET parkingFee = %s
        WHERE spaceNo = %s
    """, (totalFee, spaceNo))
    con.commit()
    con.close()

def Desc():
    con = connect()
    cur = con.cursor()
    cur.execute("SELECT * FROM tb_students ORDER BY id DESC")
    rows = cur.fetchall()
    con.close()
    return rows

def vhType(spaceNo):
    con = connect()
    cur = con.cursor()
    cur.execute('SELECT vehicleType FROM customer_tb WHERE spaceNo = %s', (spaceNo, ))
    res = cur.fetchone()
    con.close()
    return res[0]
    
def entryTime(spaceNo=""):
    con = connect()
    cur = con.cursor()
    cur.execute("SELECT checkTime FROM customer_tb WHERE spaceNo = %s", (spaceNo,))
    res = cur.fetchone()
    con.close()
    return res[0]

def updateExitTIme(exitTime, spaceNo):
    con = connect()
    cur = con.cursor()
    cur.execute("""
                UPDATE customer_tb
                SET exitTime = %s WHERE spaceNo = %s""", (exitTime, spaceNo))
    con.commit()
    con.close()

def exitTime(spaceNo=""):
    con = connect()
    cur = con.cursor()
    cur.execute("SELECT exitTime FROM customer_tb WHERE spaceNo = %s", (spaceNo,))
    res = cur.fetchone()
    con.close()
    return res[0]