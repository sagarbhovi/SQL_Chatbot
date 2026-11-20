import sqlite3

#Connecting to Sqllite
connection = sqlite3.connect('student.db')

#Create a cursor object to insert record or create table
cursor = connection.cursor()

#Creating the table
table_info = """
create table STUDENT(Name varchar(25),Class varchar(25),
Section Varchar(25),Marks int)
"""
cursor.execute(table_info)

#Inserting records into the table
cursor.execute('''Insert Into STUDENT values('Krish','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('John','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Mukesh','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Jacob','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values('Dipesh','DEVOPS','A',35)''')

#Display all the records
print('The inserted records are')

data = cursor.execute('''Select * from STUDENT''')

for row in data:
    print(row)

# Committing changes in the database
connection.commit()
connection.close()