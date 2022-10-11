from datetime import datetime, timedelta

import os


'''
Fiscal Year Generator 
'''


# Remove old file
os.remove('W:\\JBSim\\DBinfo\\Fiscal_year_upload.txt')

# create file
fileColumn = open('W:\\JBSim\\DBinfo\\Fiscal_year_upload.txt', 'a')

# Title Columns
tableName = "INSERT INTO Fiscal_Year (Fiscal_Year, Name, Nbr_Periods, Start_Date, End_Date, Last_Updated ) VALUES "


# loop through table
e = 1

txtFY = 20
dateStart = '2019-09-30'
date_1 = datetime.strptime(dateStart, '%Y-%m-%d')
txtMon = datetime.strftime(date_1, '%b')

for i in range(1, 6):
    txtFiscal_Year = 'NEWID()'
    txtName = 'FY' + str(txtFY)
    txtStart_Date = str(date_1)
    txtEnd_Date = str(date_1 + timedelta(days=371))
    txtLast_Updated = 'CURRENT_TIMESTAMP'
    print('year')

    # Concatenate all the variables
    txtVar = tableName + "(" + txtFiscal_Year + ", '" + txtName + "', " + "'0'" + ", '" + txtStart_Date + "', '" + txtEnd_Date + "', " + txtLast_Updated + "); \n"


    # write the line
    fileColumn.write(txtVar)
    txtFY = txtFY + 1
    date_1 = date_1 + timedelta(days=364)


print('Finish')
