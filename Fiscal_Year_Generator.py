import pandas as pd
import os
import random

'''
Fiscal Year Generator 
'''

# open CSV file, set to dataframe a
df = pd.read_csv('W:\\JBSim\\DBinfo\\Fiscal_Year_20-25.csv')

# Remove old file
os.remove('W:\\JBSim\\DBinfo\\Fiscal_year_upload.txt')

# create file
fileColumn = open('W:\\JBSim\\DBinfo\\Fiscal_year_upload.txt', 'a')

# Title Columns
tableName = 'INSERT INTO Fiscal_Year(Fiscal_Year, Name, Nbr_Periods, Start_Date, End_Date, Last_Updated ) \n'
fileColumn.write(tableName)
fileColumn.write('\n' + 'VALUES' + '\n')

# loop through table
e = 1
while e < 366:
    txtFiscal_Year = "'" + str(int(df.iloc[e]['YEAR'])) + "'"
    txtName = "'"+ str(df.iloc[e]['FISCAL']) + str(int(df.iloc[e]['YEAR'])) + '_' + str(int(df.iloc[e]['WEEK'])).zfill(2) + "'"
    txtNbr_Periods = str(int(df.iloc[e]['WEEK']))
    txtStart_Date = "'" + str(df.iloc[e]['START']) + "'"
    txtEnd_Date = "'" + str(df.iloc[e]['END']) + "'"
    txtLast_Updated = 'NOW()'
    print('year')

    # Concatenate all the variables
    txtVar = '(' + txtFiscal_Year + ', ' + txtName + ', ' + txtNbr_Periods + ', ' + txtStart_Date + ', ' + txtEnd_Date + ', ' + txtLast_Updated + ')'

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
