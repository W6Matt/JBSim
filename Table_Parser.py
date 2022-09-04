import pandas as pd
import os
'''
Table_Parser: this program parses the column data from DB_Schema.csv then prepares the data for scripts like Employee_Generator
    Creates a variables for each column
    Concatenates the variables to for use in scripting
    formats the data for the sql insert statement
'''


# open DB Schema CSV file, set to dataframe a
df = pd.read_csv('W:\\JBSim\\DBinfo\\DB_Schema.csv')

# Remove old file
os.remove('W:\\JBSim\\DBinfo\\Table_insert.txt')

# Create output file
outPrint = open('W:\\JBSim\\DBinfo\\Table_insert.txt', 'a')

#By table name loop thru the table
e = 1

tableName = 'Work_Center'

# Employee
# Work_Center

while e < len(df.index):
    if tableName == df.iloc[e]['TABLE_NAME']:
        txtItem = str('txt' + df.iloc[e]['COLUMN_NAME'] + "= 'NULL'")
        outPrint.write('\n' + txtItem)
        e += 1
    else:
        e += 1
e = 1

outPrint.write('\n' + '\n' + '\n')

txtItem = 'txtVar = "VALUES ("'
outPrint.write(txtItem)
while e < len(df.index):
    if tableName == df.iloc[e]['TABLE_NAME']:
        txtItem = str('txt' + df.iloc[e]['COLUMN_NAME'] + " + ', ' + ")
        outPrint.write(txtItem)
        e += 1
    else:
        e += 1
txtItem = ')'
outPrint.write(txtItem)
outPrint.write('\n' + '\n' + '\n')

e = 1
txtItem = 'INSERT INTO ' + tableName + '('
outPrint.write(txtItem)
while e < len(df.index):
    if tableName == df.iloc[e]['TABLE_NAME']:
        txtItem = str(df.iloc[e]['COLUMN_NAME'] + ', ')
        outPrint.write(txtItem)
        e += 1
    else:
        e += 1
txtItem = ')'
outPrint.write(txtItem)



