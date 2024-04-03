import calendar
from datetime import date
import pandas as pd
import mysql.connector as myconn

def add_new_employees():
    mydb = myconn.Connect(host = 'localhost', user = 'root', password = '9876', database = 'employee')
    if mydb.is_connected():
        print("Connection established!!")
    cursor = mydb.cursor()
    name = str(input("Enter name : "))
    id = int(input("Enter id : "))
    post = str(input("Enter post : "))
    age = int(input("Enter age : "))
    query = "insert into emp3(id,name,post,age)values({},'{}','{}',{})".format(id,name,post,age)
    df = pd.read_csv("employee.csv",index_col = 0)
    values = []
    for i in range(0,len(df)):
        values.append("A")
    df[str(id)] = values
    df.to_csv('employee.csv')
    cursor.execute(query)
    mydb.commit()
    permission = "Y"
    while(permission == "Y"):
        permission = str(input("Do you want to enter more data ? (Type 'Y' for yes) : "))
        if permission != "Y":
            break
        add_new_employees()

def attendance_system():
    df = pd.read_csv("employee.csv",index_col = 0)
    df.Date = pd.to_datetime(df.Date).dt.date
    counter = df.shape[0]
    today = date.today()
    print("Today's date is: ", today)
    cols = len(df.columns)
    attendance = [today]
    for i in range(1,cols):
        print("Enter today's attendance of ",df.columns[i]," : ", end = "")
        x = int(input())
        if x == 1:
            x = "P"
        else:
            x = "A"
        attendance.append(x)
    
    counter = df.shape[0]
    df.loc[counter] = attendance
    df.to_csv('employee.csv')

def attendance_calculator():
    df = pd.read_csv("employee.csv",index_col = 0)
    for i in range(1,df.columns.size):
        P = 0
        A = 0
        i = str(i)
        for j in df[str(i)]:
            if j == "P":
                P += 1
            else:
                A += 1
        print("Employee id ",i," is present for ",P," days and was absent for ",A,"days.")

def select(status):
    match status:
        case 1 :
            attendance_system()
        case 2 :
            attendance_calculator()
        case 3 :
            add_new_employees()
        case _ :
            print("Error!!")

def main():
    print("Good Morning!!")
    print("Today's Date - ",date.today())
    print()
    print("Select tool \n Enter 1 for Attendance \n Enter 2 for Attendance calculator \n Enter 3 to add new employees \n Enter any no. to exit ")
    tool = int(input("Enter choice : "))
    while(tool<=4):
        select(tool)
        tool = int(input("Enter choice : "))

main()