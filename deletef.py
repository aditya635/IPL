import mysql.connector
from secret import mydb

def delteam():
    mycursor = mydb.cursor()
    sql1 = "DELETE FROM TEAM WHERE T_name = %s"
    sql2 = "DELETE FROM Playerof  WHERE T_name = %s"
    tname=input("Enter Team name: ")
    val = (tname, )
    mycursor.execute(sql2, val)
    mycursor.execute(sql1, val)
    mydb.commit()
    mycursor.close()

#delteam()

def delPlayer():
    mycursor = mydb.cursor()
    sql1 = "DELETE FROM Playerof  WHERE P_id = %s"
    sql2 = "DELETE FROM Player  WHERE P_id = %s"
    pid = int(input("Enter P_id : "))
    val = (pid ,)
    mycursor.execute(sql1, val)
    mycursor.execute(sql2, val)
    mydb.commit()
    mycursor.close()
delPlayer()

def delcpt():
    mycursor = mydb.cursor()
    sql = "DELETE FROM CPTof WHERE P_id = %s"
    pid = int(input("Enter P_id : "))
    val = (pid ,)
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()
#delcpt()

def delfixtures():
    mycursor = mydb.cursor()
    sql = "DELETE FROM Fixtures WHERE T_NAME1 = %s and Date = %s"
    tname1=input("Enter Team1 name: ")
    cpt=input("Enter Date ('YYYY-MM-DD') ")
    val = (tname1,cpt)
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()
#delfixtures()