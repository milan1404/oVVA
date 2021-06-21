import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",               #hostname
  user="root",                   # the user who has privilege to the db
  passwd="milan",               #password for user
  database="OLIVIA_DB",               #database name
  auth_plugin = 'mysql_native_password',

)
mycursor = mydb.cursor()




########################################################################################################################


#mycursor.execute("CREATE DATABASE OLIVIA_DB")      #db creation


#mycursor.execute("SHOW DATABASES")                    #{list of db}
#for db in mycursor:
 # print(db)

#mycursor.execute("CREATE TABLE USER_DEATILS(NAME CHAR(50),MAIL_ID VARCHAR(85),LOCATION CHAR(50),SQLTIME TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL)")      #TABLE_CREATION

#mycursor.execute("SHOW TABLES")                    #{list of TABLES}
#for db in mycursor:
#  print(db)

#sqlFormula=("INSERT INTO greet (INPUT , OUTPUT) VALUES (%s, %s)")
#info1=[("greet","hello"),( "greet","hello,there"),("greet","Hello user,what would you like to do"),("greet","Greetings human", "Your wish is my command"),("greet","oliVIA at your service")]         #populating
#mycursor.executemany(sqlFormula,info1)
#mydb.commit()

#mycursor.execute("DESC INFO")          #table desc
#for db in mycursor:
 # print(db)

#mycursor=mydb.cursor()
#sql="UPDATE BOOTING_STARTUP SET INPUT="BOOTING_STARTUP" WHERE OUTPUT="oliVIA assistant is booting up""
#mycursor.execute(sql)
#mydb.commit()







#execution part start
#def execution():
 # mycursor.execute("SELECT output FROM BOOTING_STARTUP")
  #myresult=mycursor.fetchall()
  #buffer=[]
  #for i in myresult:
   # buffer.append(i)
#execution part ends

#execution()