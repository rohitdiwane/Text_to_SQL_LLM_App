import sqlite3

## Connectt to SQlite
connection=sqlite3.connect("student.db")

# Create a cursor object to insert record,create table

cursor=connection.cursor()

## create the table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);

"""
cursor.execute(table_info)

## Insert Some more records

cursor.execute('''Insert Into STUDENT values('Rohit','Data Science','A',95)''')
cursor.execute('''Insert Into STUDENT values('Sushant','Data Science','B',98)''')
cursor.execute('''Insert Into STUDENT values('Dhiraj','Data Science','A',82)''')
cursor.execute('''Insert Into STUDENT values('Ashish','DEVOPS','A',65)''')
cursor.execute('''Insert Into STUDENT values('Suraj','DEVOPS','A',70)''')

## Disspaly ALl the records

print("The isnerted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes int he databse
connection.commit()
connection.close()