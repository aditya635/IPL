import mysql.connector
from secret import mydb

mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE Team (T_name VARCHAR(255) PRIMARY KEY, COACH VARCHAR(255))")
#mycursor.execute("CREATE TABLE Player (P_name VARCHAR(255), POS INT , SKILL INT , P_id INT PRIMARY KEY)")
#mycursor.execute("CREATE TABLE Fixtures (T_name1 VARCHAR(255) ,T_name2 VARCHAR(255), Date DATE, PRIMARY KEY(T_name1,Date))")
#mycursor.execute("ALTER TABLE Player ADD COLUMN team VARCHAR(255)")
#mycursor.execute("ALTER TABLE Player ADD FOREIGN KEY (team) REFERENCES Team(T_name)")
#mycursor.execute("CREATE TABLE CPTof (T_names VARCHAR(255) PRIMARY KEY, CPT INT )")
#mycursor.execute("ALTER TABLE CPTof ADD FOREIGN KEY (T_names) REFERENCES Team(T_name)")
#mycursor.execute("ALTER TABLE CPTof ADD CONSTRAINT cptof_ibfk_2 FOREIGN KEY (CPT) REFERENCES Player(P_id)")
#mycursor.execute("ALTER TABLE Fixtures ADD FOREIGN KEY (T_name1) REFERENCES Team(T_name)")
#mycursor.execute("ALTER TABLE Fixtures ADD FOREIGN KEY (T_name2) REFERENCES Team(T_name)")
#mycursor.execute("CREATE TABLE PLAYEROF (T_name VARCHAR(255), P_id INT)")
#mycursor.execute("ALTER TABLE PLAYEROF ADD FOREIGN KEY (T_name) REFERENCES Team(T_name)")
#mycursor.execute("ALTER TABLE PLAYEROF ADD FOREIGN KEY (P_id) REFERENCES Player(P_id)")
#mycursor.execute("ALTER TABLE Player MODIFY P_id INT AUTO_INCREMENT")


#sql = "INSERT INTO Player (P_name, POS,SKILL,team) VALUES (%s, %s,%s,%s)"
#val = ("Rohit Sharma", 1,98,"Mumbai Indians")

#sql = "INSERT INTO TEAM (T_name,COACH) VALUES (%s, %s)"
#val = ("Mumbai Indians", "Tendulkar")

#sql = "INSERT INTO CPTof (T_names,CPT) VALUES (%s, %s)"
#val = ("Mumbai Indians", 3)

#sql = "INSERT INTO PLAYEROF (T_name,P_id) VALUES (%s, %s)"
#val = ("Chennai Super Kings", 1)

#sql = "INSERT INTO Fixtures (T_name1,T_name2,Date) VALUES (%s, %s,%s)"
#val = ("Mumbai Indians", "Chennai Super Kings","2023-3-20")

#mycursor.execute("DELETE FROM TEAM WHERE T_name = 'Kolkata Riders' ")

#mycursor.execute(sql, val)

#mydb.commit()


mycursor.close()