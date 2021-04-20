import mysql.connector
from secret import mydb

def insertteam():
    mycursor = mydb.cursor()
    sql = "INSERT INTO TEAM (T_name,COACH) VALUES (%s, %s)"
    tname=input("Enter Team name: ")
    coach=input("Enter Coach name: ")
    val = (tname, coach)
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()

insertteam()

def insertPlayer():
    mycursor = mydb.cursor()
    sql = "INSERT INTO Player (P_name, POS,SKILL,team) VALUES (%s, %s,%s,%s)"
    tname = input("Enter Team name: ")
    player = input("Enter Player name: ")
    pos = int(input("Enter Position: "))
    skill = int(input("Enter Skill Level: "))
    val = (player ,pos ,skill ,tname)
    mycursor.execute(sql, val)
    adr=(player,pos,tname)
    mycursor.execute("SELECT P_id FROM Player where P_name = %s and POS = %s and team = %s", adr)

    myresult = mycursor.fetchall()
    x=[]
    for x in myresult:
        for i in x:
            sql = "INSERT INTO PLAYEROF (T_name,P_id) VALUES (%s, %s)"
            val = (tname, i)
            mycursor.execute(sql, val)

    mydb.commit()
    mycursor.close()
#insertPlayer()

def makecpt():
    mycursor = mydb.cursor()
    sql = "INSERT INTO CPTof (T_names,CPT) VALUES (%s, %s)"
    tname=input("Enter Team name: ")
    cpt=int(input("Enter Playerid to make captain: "))
    val = (tname, cpt)
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()
#makecpt()

def setfixtures():
    mycursor = mydb.cursor()
    sql = "INSERT INTO Fixtures (T_name1,T_name2,Date) VALUES (%s, %s,%s)"
    tname1=input("Enter Team1 name: ")
    tname2=input("Enter Team2 name: ")
    cpt=input("Enter Date ('YYYY-MM-DD') ")
    val = (tname1,tname2, cpt)
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()
#setfixtures()