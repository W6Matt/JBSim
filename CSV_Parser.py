import pandas as pd
import os

'''
CVS Parser imports DB_Schema.csv and DB_Columns. The script iterates through DB_Columns, matching to Table name
in DB_Schema. The Script then builds a SQL CREATE TABLE argument with the collected data

'''

# open DB Schema CSV file, set to dataframe a
dfa = pd.read_csv('W:\\JBSim\\DBinfo\\DB_Schema.csv')

# Open Column CSV
dfb = pd.read_csv('W:\\JBSim\\DBinfo\\DB_Columns.csv')

# Remove old file
os.remove('W:\\JBSim\\DBinfo\\Output.sql')

# Create output file
outPrint = open('W:\\JBSim\\DBinfo\\Output.sql', 'a')

#By table name loop thru the table
i = 1
e = 1
while i < len(dfb.index):
        tableName =str(dfb.iloc[i]['TABLE_NAME'])
        rowNew = 'CREATE TABLE ' + tableName +  ' ('
        while e < len(dfa.index):
                if tableName == dfa.iloc[e]['TABLE_NAME']:
                        columnName = str(dfa.iloc[e]['COLUMN_NAME'])
                        dataType = str(dfa.iloc[e]['DATA_TYPE'])
                        if dfa.iloc[e]['CHARACTER_MAXIMUM_LENGTH'] > 0:
                            varSize = str(int(dfa.at[e, 'CHARACTER_MAXIMUM_LENGTH']))
                        if dfa.iloc[e]['NUMERIC_PRECISION'] > 0:
                            varSize = str(int(dfa.iloc[e]['NUMERIC_PRECISION']))
                        if dfa.iloc[e]['DATETIME_PRECISION'] > 0:
                            varSize = str(int(dfa.iloc[e]['DATETIME_PRECISION']))
                        if dfa.iloc[e]['IS_NULLABLE'] == 'YES':
                            nullAble = 'NULL'
                        if dfa.iloc[e]['IS_NULLABLE'] == 'NO':
                                nullAble = 'NOT NULL'
                        dataType = dataType.upper()
                        rowNew = rowNew + columnName + ' ' + dataType + ' ' + nullAble + ','
                e += 1
        else:
                e += 1
        e = 1
        print(rowNew)
        rowNew = rowNew + ');'
        rowNew = rowNew.replace(',)', ')')
        outPrint.write('\n' + rowNew)
        i += 1

# ' (' + varSize + ') '
# TABLE_NAME
# COLUMN_NAME
# DATA_TYPE
# CHARACTER_MAXIMUM_LENGTH
# NUMERIC_PRECISION
# DATETIME_PRECISION
