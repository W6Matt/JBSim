from datetime import datetime, timedelta


fileColumn = open('W:\\JBSim\\DBinfo\\Fiscal_Period_upload.txt', 'w')

# Title Columns
tableName = "INSERT INTO Fiscal_Period (Fiscal_Period, Name, Per_Nbr, Fiscal_Year, Start_Date, End_Date, Last_Updated ) VALUES "


# loop through table
e = 1

txtFY = 23
dateStart = '2022-09-26'
date_1 = datetime.strptime(dateStart, '%Y-%m-%d')
txtMon = datetime.strftime(date_1, '%b')
numWeek = 40

fileColumn.write('USE DBA1001 \n\n')

fileColumn.write('DECLARE @UID VARCHAR(60);\n')
fileColumn.write("SELECT @UID = Fiscal_Year FROM Fiscal_Year WHERE name = 'FY" + str(txtFY) + "'\n\n")


for i in range(1, 55):
    txtName = 'FY' + str(txtFY)  + '_' + str(numWeek) + '_' + str(txtMon)
    txtPerNum = str(i)
    txtStart = str(date_1)
    txtEnd = str(date_1 + timedelta(days=6))

    # Concatenate all the variables
    txtVar = tableName + "(" + "NEWID()" + ", '" + txtName.upper() + "', " + txtPerNum + ", @UID, '" + txtStart + "', '" + txtEnd + "', CURRENT_TIMESTAMP ); \n"


    # write the line
    fileColumn.write(txtVar)

    numWeek = numWeek + 1
    date_1 = date_1 + timedelta(days=7)
    if numWeek == 53:
            numWeek = 1


print('Finish')
