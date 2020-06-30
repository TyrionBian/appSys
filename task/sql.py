import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="passwd",
    database="testdb"
)

mycursor = mydb.cursor()

# mycursor.execute('''CREATE TABLE application (uuid VARCHAR(36) NOT NULL,
# productNum VARCHAR(30) NOT NULL,
# channelNum VARCHAR(30) NOT NULL,
# name VARCHAR(30) NOT NULL,
# idcardEncrypt VARCHAR(30) NOT NULL,
# phone VARCHAR(20) NOT NULL,
# applytime VARCHAR(20) NOT NULL,
# PRIMARY KEY ( uuid )
# )''')

# mycursor.execute('''CREATE TABLE status 
# (uuid VARCHAR(36) NOT NULL,
# chainid VARCHAR(30) NOT NULL,
# chainversion VARCHAR(30) NOT NULL,
# status VARCHAR(30) NOT NULL,
# createtime VARCHAR(20) NOT NULL,
# updatetime VARCHAR(20) NOT NULL,
# applytime VARCHAR(20) NOT NULL,
# PRIMARY KEY ( uuid )
# )''')

# mycursor.execute("show tables;")

mycursor.execute("select * from status;")
for x in mycursor:
  print(x)