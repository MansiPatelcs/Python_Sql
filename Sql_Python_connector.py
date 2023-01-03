import mysql.connector

mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password='password',
  database='mydatabse'
)

mycursor = mydb.cursor()

# mycursor.execute('CREATE DATABASE MYDATABSE')
# mycursor.execute('show databases')
# for x in mycursor:
#   print(x)

# mycursor.execute('CREATE TABLE CUSTOMERS (NAME VARCHAR(255), ADDRESS VARCHAR(255))')
# mycursor.execute('SHOW TABLES')
# for x in mycursor:
#   print(x)

# mycursor.execute('ALTER TABLE CUSTOMERS ADD COLUMN ID INT AUTO_INCREMENT PRIMARY KEY')

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql,val)
# mydb.commit()
# print(mycursor.rowcount, "record inserted.")

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]
#
# mycursor.executemany(sql, val)
# mydb.commit()
#print(mycursor.rowcount, "was inserted.")

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("Michelle", "Blue Village")
# mycursor.execute(sql, val)
# mydb.commit()
# print("1 record inserted, ID:", mycursor.lastrowid)

# sql='SELECT * FROM CUSTOMERS'
# mycursor.execute('SELECT NAME, ADDRESS FROM CUSTOMERS')
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)

# mycursor.execute('SELECT * FROM CUSTOMERS')
# myresult = mycursor.fetchone()
# print(myresult)

# sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)

# sql = "SELECT * FROM customers WHERE address = %s"
# adr = ("Yellow Garden 2", )
# mycursor.execute(sql, adr)
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)

# sql = "SELECT * FROM customers ORDER BY name"
# sql = "SELECT * FROM customers ORDER BY name DESC"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)

# sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "record(s) deleted")


# sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

# sql = "UPDATE customers SET address = %s WHERE address = %s"
# val = ("Valley 345", "Canyon 123")
#
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "record(s) affected")


# mycursor.execute("SELECT * FROM customers LIMIT 5")
# mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)
