import pandas as pd
import os

# open CSV file, set to dataframe a
df = pd.read_csv('W:\\JBSim\\DBinfo\DB_Schema.csv')

# Remove old file
os.remove('W:\\JBSim\\DBinfo\\DB_Columns.csv')

# create file
fileColumn = open('W:\\JBSim\\DBinfo\\DB_Columns.csv', 'a')

# Count Rows
totalRow = len(df.index)

e = 1
tableName = 'TABLE_NAME' + ','

fileColumn.write(tableName)

while e < totalRow:
    if tableName == df.iloc[e]['TABLE_NAME']:
        e += 1
    else:
        tableName = df.iloc[e]['TABLE_NAME']
        a = df.iloc[e]['TABLE_NAME']
        print(tableName)
        fileColumn.write('\n' + a + ',')





# TABLE_NAME
# COLUMN_NAME
# DATA_TYPE
# CHARACTER_MAXIMUM_LENGTH
# NUMERIC_PRECISION
# DATETIME_PRECISION
