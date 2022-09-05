import pandas as pd
import os
import random

'''
Employee Generator uses data from Table_Parser to create Creates Employee
    Employee Number 11xxx incremental increases by 1
    Random selects name from list
    Random selects surname from list
    sets hourly rate to $100.
    set start date to 2022-1-1
'''

# open CSV file, set to dataframe a
dfFirstName = pd.read_csv('W:\\JBSim\\DBinfo\\1000_Male_Names.csv')

dfSurnames = pd.read_csv('W:\\JBSim\\DBinfo\\2000_Surnames.csv')

# Remove old file
os.remove('W:\\JBSim\\DBinfo\\Employee_upload.sql')

# create file
fileColumn = open('W:\\JBSim\\DBinfo\\Employee_upload.sql', 'a')

# Number of Employees to create
totalEmp = 100

# Employee Number Start
empNumStr = str('11')
empNumEnd = 0

# Title Columns
tableName = 'INSERT INTO Employee(Employee, Work_Center, Address, User_Values, First_Name, Middle_Initial, Last_Name, SSN, Type, Status, Class, Hourly_Rate, Commission_Pct, Shift_Start, Shift_End, Hire_Date, Note_Text, Last_Updated, Shift, Department, Supervisor, Default_Tran_Limit, Begin_Tran_Prompt, Repeat_Tran_Prompt, Tran_Repeater, ObjectID) \n'
fileColumn.write(tableName)
fileColumn.write('\n' + 'VALUES' + '\n')

# loop through table
e = 1
while e < totalEmp:
    txtFirst = dfFirstName.iloc[random.randrange(1, 250)]['FIRST_NAME']
    txtSurname = dfSurnames.iloc[random.randrange(1, 2000)]['SURNAME']
    empNumEnd += 1
    # all table Vars
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
    txtHourly_Rate = '100.00'
    txtCommission_Pct = 'NULL'
    txtShift_Start = 'NULL'
    txtShift_End = 'NULL'
    txtHire_Date = "'2022-01-01'"
    txtNote_Text = 'NULL'
    txtLast_Updated = 'NOW()'
    txtShift = 'NULL'
    txtDepartment = 'NULL'
    txtSupervisor = 'NULL'
    txtDefault_Tran_Limit = 'NULL'
    txtBegin_Tran_Prompt = 'NULL'
    txtRepeat_Tran_Prompt = 'NULL'
    txtTran_Repeater = 'NULL'
    txtObjectID = 'MD5(random()::text)'
    print(txtFirst_Name + ' ' + txtLast_Name)

    # Concatenate all the variables
    txtVar = '(' + txtEmployee + ', ' + txtWork_Center + ', ' + txtAddress + ', ' + txtUser_Values + ', ' + txtFirst_Name + ', ' + txtMiddle_Initial + ', ' + txtLast_Name + ', ' + txtSSN + ', ' + txtType + ', ' + txtStatus + ', ' + txtClass + ', ' + txtHourly_Rate + ', ' + txtCommission_Pct + ', ' + txtShift_Start + ', ' + txtShift_End + ', ' + txtHire_Date + ', ' + txtNote_Text + ', ' + txtLast_Updated + ', ' + txtShift + ', ' + txtDepartment + ', ' + txtSupervisor + ', ' + txtDefault_Tran_Limit + ', ' + txtBegin_Tran_Prompt + ', ' + txtRepeat_Tran_Prompt + ', ' + txtTran_Repeater + ', ' + txtObjectID + ')'

    # add the comma
    if e > 1:
        fileColumn.write(', \n')
    # add to the loop
    e += 1
    # write the line
    fileColumn.write(txtVar)
# add to the end
fileColumn.write('\n ;')

print('Finish')

