import mysql.connector
from secret import mydb



def showTeams():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT T_name FROM Team")

    myresult = mycursor.fetchall()
    x=[]
    for x in myresult:
        for i in x:
            print(i)
    mycursor.close()
def showCPTfromT():
    mycursor = mydb.cursor()
    Team = input("Enter Team ")
    adr=(Team,)
    mycursor.execute("SELECT CPT FROM CPTof where T_names = %s", adr)

    myresult = mycursor.fetchall()
    x=[]
    for x in myresult:
        for i in x:
            i=i
    adrs=(i,)
    mycursor.execute("SELECT P_name FROM Player where P_id = %s", adrs)
    myresult = mycursor.fetchall()
    x=[]
    for x in myresult:
        for i in x:
            print(i)
    mycursor.close()
def showPlayerfromT():
    mycursor = mydb.cursor()
    Team = input("Enter Team ")
    adr=(Team,)
    mycursor.execute("SELECT P_id FROM PLAYEROF where T_name = %s", adr)

    myresult = mycursor.fetchall()
    x=[]
    for x in myresult:
        for i in x:
            adrs=(i,)
            mycursor.execute("SELECT P_name FROM Player where P_id = %s", adrs)
            myresult = mycursor.fetchall()
            s=[]
            for s in myresult:
                for l in s:
                    print(l)
    mycursor.close()



def dattebayyo():
    mycursor = mydb.cursor()
    date1=input("Date from('YYYY-MM-DD')") #'2018-01-01'
    date2=input("Date to ('YYYY-MM-DD')")#'2022-01-31'
    date=(date1,date2)
    mycursor.execute("SELECT T_name1,T_name2 FROM Fixtures where DATE between %s and %s", date)
    myresult = mycursor.fetchall()
    for i in myresult:
        print(i[0],'vs',i[1])
    mycursor.close()