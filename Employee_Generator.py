import pandas as pd
import os
import random

# open CSV file, set to dataframe a
dfFirstName = pd.read_csv('W:\\JBSim\\DBinfo\\1000_Male_Names.csv')

dfSurnames = pd.read_csv('W:\\JBSim\\DBinfo\\2000_Surnames.csv')

# Remove old file
os.remove('W:\\JBSim\\DBinfo\\Employee_upload.txt')

# create file
fileColumn = open('W:\\JBSim\\DBinfo\\Employee_upload.txt', 'a')

# Number of Employees to create
totalEmp = 10

# Employee Number Start
empNumStr = str('11')
empNumEnd = 0

# Title Columns
tableName = 'INSERT INTO Employee(Employee, Work_Center, Address, User_Values, First_Name, Middle_Initial, Last_Name, SSN, Type, Status, Class, Hourly_Rate, Commission_Pct, Shift_Start, Shift_End, Hire_Date, Note_Text, Last_Updated, Shift, Department, Supervisor, Default_Tran_Limit, Begin_Tran_Prompt, Repeat_Tran_Prompt, Tran_Repeater, ObjectID) \n'
fileColumn.write(tableName)
fileColumn.write('\n' + 'VALUES' + '\n')

# loop thru table
e = 1
while e < totalEmp:
    txtFirst = dfFirstName.iloc[random.randrange(1, 250)]['FIRST_NAME']
    txtSurname = dfSurnames.iloc[random.randrange(1, 2000)]['SURNAME']
    empNumEnd += 1
    ############ all table Vars
    txtEmployee = empNumStr + str(empNumEnd).zfill(3)
    txtWork_Center = 'NULL'
    txtAddress = 'NULL'
    txtUser_Values = 'NULL'
    txtFirst_Name = str("'" + txtFirst.capitalize() + "'")
    txtMiddle_Initial = 'NULL'
    txtLast_Name = str("'" + txtSurname.capitalize() + "'")
    txtSSN = 'NULL'
    txtType = 'NULL'
    txtStatus = "'Active'"
    txtClass = 'NULL'
    txtHourly_Rate = 'NULL'
    txtCommission_Pct = 'NULL'
    txtShift_Start = 'NULL'
    txtShift_End = 'NULL'
    txtHire_Date = 'NULL'
    txtNote_Text = 'NULL'
    txtLast_Updated = 'NULL'
    txtShift = 'NULL'
    txtDepartment = 'NULL'
    txtSupervisor = 'NULL'
    txtDefault_Tran_Limit = 'NULL'
    txtBegin_Tran_Prompt = 'NULL'
    txtRepeat_Tran_Prompt = 'NULL'
    txtTran_Repeater = 'NULL'
    txtObjectID = 'NULL'
    print(txtFirst_Name + ' ' + txtLast_Name)

    # Concatenate all the variables
    txtVar = '(' + txtEmployee + ', ' + txtWork_Center + ', ' + txtAddress + ', ' + txtUser_Values + ', ' + txtFirst_Name + ', ' + txtMiddle_Initial + ', ' + txtLast_Name + ', ' + txtSSN + ', ' + txtType + ', ' + txtStatus + ', ' + txtClass + ', ' + txtHourly_Rate + ', ' + txtCommission_Pct + ', ' + txtShift_Start + ', ' + txtShift_End + ', ' + txtHire_Date + ', ' + txtNote_Text + ', ' + txtLast_Updated + ', ' + txtShift + ', ' + txtDepartment + ', ' + txtSupervisor + ', ' + txtDefault_Tran_Limit + ', ' + txtBegin_Tran_Prompt + ', ' + txtRepeat_Tran_Prompt + ', ' + txtTran_Repeater + ', ' + txtObjectID + ')'

    # add the comma
    if e > 1:
        fileColumn.write(', \n')
    # add to the llop
    e += 1
    # write the line
    fileColumn.write(txtVar)
# add to the end
fileColumn.write('\n ;')

print('Finish')


"""
    CREATE TABLE Employee (Employee VARCHAR NOT NULL,Work_Center VARCHAR NULL,Address INT NULL,User_Values INT NULL,First_Name VARCHAR NULL,Middle_Initial VARCHAR NULL,Last_Name VARCHAR NULL,SSN VARCHAR NULL,Type VARCHAR NOT NULL,Status VARCHAR NOT NULL,Class VARCHAR NOT NULL,Hourly_Rate MONEY NULL,
    Commission_Pct FLOAT NULL,Shift_Start DATETIME NULL,Shift_End DATETIME NULL,Hire_Date DATETIME NULL,Note_Text TEXT NULL,Last_Updated DATETIME NOT NULL,Shift UNIQUEIDENTIFIER NULL,Department VARCHAR NULL,Supervisor VARCHAR NULL,Default_Tran_Limit SMALLINT NULL,Begin_Tran_Prompt VARCHAR NULL,Repeat_Tran_Prompt VARCHAR NULL,Tran_Repeater BIT NULL,ObjectID UNIQUEIDENTIFIER NOT NULL);
    if tableName == df.iloc[random.randrange(1, 2000)]['SURNAME']:
        e += 1
    else:
        tableName = df.iloc[e]['TABLE_NAME']
        a = df.iloc[e]['TABLE_NAME']
        print(tableName)
        fileColumn.write('\n' + a + ',')
"""