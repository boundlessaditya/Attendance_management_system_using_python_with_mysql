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
    list1 = []
    day = str(input("Enter start date : "))
    month = str(input("Enter start month : "))
    year = str(input("Enter start year : "))
    date1 = month+"/"+day+"/"+year
    day = str(input("Enter end date : "))
    month = str(input("Enter end month : "))
    year = str(input("Enter end year : "))
    date2 = month+"/"+day+"/"+year
    for i in df.Date:
        if i >= date1 and i <= date2:
            x = df[df.Date == i].iloc[0,:]
            x = np.array(x)
            list1.append(x)
    list1 = pd.DataFrame(list1)
    for i in range(1,list1.columns.size):
        P = 0
        A = 0
        for j in list1.iloc[:,i]:
            if j == "P":
                P += 1
            else:
                A += 1
        print("Employee id ",i," is present for ",P," days and was absent for ",A,"days.")

def Lookout():
    df = pd.read_csv("employee.csv",index_col = 0)
    day = str(input("Enter date : "))
    month = str(input("Enter month : "))
    year = str(input("Enter year : "))
    date = month+"/"+day+"/"+year
    print(df[df.Date == date])

def select(status):
    match status:
        case 1 :
            attendance_system()
        case 2 :
            attendance_calculator()
        case 3 :
            add_new_employees()
        case 4 :
            Lookout()
        case _ :
            print("Error!!")

def main():
    print("Good Morning!!")
    print("Today's Date - ",date.today())
    print()
    df = pd.read_csv('employee.csv',index_col = 0)
    today = date.today()
    today = pd.to_datetime(today)
    today = str(today)
    last_date = str(pd.to_datetime(df.Date.iloc[-1]))
    if last_date == today:
        print("Enter 2 for Attendance calculator \n Enter 3 to add new employees \n Enter any no. to exit ")
	def main():
    print("Good Morning!!")
    print("Today's Date - ",date.today())
    print()
    df = pd.read_csv('employee.csv',index_col = 0)
    today = date.today()
    today = pd.to_datetime(today)
    today = str(today)
    last_date = str(pd.to_datetime(df.Date.iloc[-1]))
    if last_date == today:
        print("Enter 2 for Attendance calculator \n Enter 3 to add new employees \n Enter any no. to exit ")
    else:
        print("Select tool \n Enter 1 for Attendance \n Enter 2 for Attendance calculator \n Enter 3 to add new employees \n Enter 4 for Lookout \n Enter any no. to exit ")
    tool = int(input("Enter choice : "))
    while(tool<=4):
        select(tool)
        tool = int(input("Enter choice : "))
    else:
        print("Select tool \n Enter 1 for Attendance \n Enter 2 for Attendance calculator \n Enter 3 to add new employees \n Enter 4 for Lookout \n Enter any no. to exit ")
    tool = int(input("Enter choice : "))
    while(tool<=4):
        select(tool)
        tool = int(input("Enter choice : "))
        
main()