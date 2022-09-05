import pandas as pd
import os
import random

'''
Work Center Generator: 
'''

# Remove old file
os.remove('W:\\JBSim\\DBinfo\\Work_Center_upload.sql')

# create file
fileColumn = open('W:\\JBSim\\DBinfo\\Work_Center_upload.sql', 'a')

# Number of Work Centers to create
totalWC = 10


# Title Columns
tableName = 'INSERT INTO Work_Center (Work_Center, User_Values_OLD, Department, Type, Setup_Labor_Rate, Run_Labor_Rate, Labor_Burden, Machine_Burden, GA_Burden, Sched_Hrs_OLD, Queue_Hrs, Nbr_Limiting_Rsrc_OLD, Capacity_OLD, Link_Material, Link_Component, Note_Text, Last_Updated, Is_Parent, Has_Parent, Parent_ID, ObjectID, Machines, Operators, Operators_Per_Machine, Parent_OID, Link_FinishedGoods, Link_Hardware, Link_Supplies, Link_Misc, Link_RawStock, Finite_Schedule, Lag_Hrs, UVDate1, UVDate2, UVText1, UVText2, UVText3, UVText4, UVText5, UVAmount1, UVAmount2, UVNumeric1, UVNumeric2, UVDecimal1, UVNote_Text, Equipment, Status) \n'
fileColumn.write(tableName)
fileColumn.write('\n' + 'VALUES' + '\n')

# loop thru table
e = 1
while e < totalWC:
    txtWork_Center = 'NULL'
    txtUser_Values_OLD = 'NULL'
    txtDepartment = 'NULL'
    txtType = 'NULL'
    txtSetup_Labor_Rate = 'NULL'
    txtRun_Labor_Rate = 'NULL'
    txtLabor_Burden = 'NULL'
    txtMachine_Burden = 'NULL'
    txtGA_Burden = 'NULL'
    txtSched_Hrs_OLD = 'NULL'
    txtQueue_Hrs = 'NULL'
    txtNbr_Limiting_Rsrc_OLD = 'NULL'
    txtCapacity_OLD = 'NULL'
    txtLink_Material = 'NULL'
    txtLink_Component = 'NULL'
    txtNote_Text = 'NULL'
    txtLast_Updated = 'NULL'
    txtIs_Parent = 'NULL'
    txtHas_Parent = 'NULL'
    txtParent_ID = 'NULL'
    txtObjectID = 'NULL'
    txtMachines = 'NULL'
    txtOperators = 'NULL'
    txtOperators_Per_Machine = 'NULL'
    txtParent_OID = 'NULL'
    txtLink_FinishedGoods = 'NULL'
    txtLink_Hardware = 'NULL'
    txtLink_Supplies = 'NULL'
    txtLink_Misc = 'NULL'
    txtLink_RawStock = 'NULL'
    txtFinite_Schedule = 'NULL'
    txtLag_Hrs = 'NULL'
    txtUVDate1 = 'NULL'
    txtUVDate2 = 'NULL'
    txtUVText1 = 'NULL'
    txtUVText2 = 'NULL'
    txtUVText3 = 'NULL'
    txtUVText4 = 'NULL'
    txtUVText5 = 'NULL'
    txtUVAmount1 = 'NULL'
    txtUVAmount2 = 'NULL'
    txtUVNumeric1 = 'NULL'
    txtUVNumeric2 = 'NULL'
    txtUVDecimal1 = 'NULL'
    txtUVNote_Text = 'NULL'
    txtEquipment = 'NULL'
    txtStatus = 'NULL'

    # Concatenate all the variables
    txtVar = "(" + txtWork_Center + ', ' + txtUser_Values_OLD + ', ' + txtDepartment + ', ' + txtType + ', ' + txtSetup_Labor_Rate + ', ' + txtRun_Labor_Rate + ', ' + txtLabor_Burden + ', ' + txtMachine_Burden + ', ' + txtGA_Burden + ', ' + txtSched_Hrs_OLD + ', ' + txtQueue_Hrs + ', ' + txtNbr_Limiting_Rsrc_OLD + ', ' + txtCapacity_OLD + ', ' + txtLink_Material + ', ' + txtLink_Component + ', ' + txtNote_Text + ', ' + txtLast_Updated + ', ' + txtIs_Parent + ', ' + txtHas_Parent + ', ' + txtParent_ID + ', ' + txtObjectID + ', ' + txtMachines + ', ' + txtOperators + ', ' + txtOperators_Per_Machine + ', ' + txtParent_OID + ', ' + txtLink_FinishedGoods + ', ' + txtLink_Hardware + ', ' + txtLink_Supplies + ', ' + txtLink_Misc + ', ' + txtLink_RawStock + ', ' + txtFinite_Schedule + ', ' + txtLag_Hrs + ', ' + txtUVDate1 + ', ' + txtUVDate2 + ', ' + txtUVText1 + ', ' + txtUVText2 + ', ' + txtUVText3 + ', ' + txtUVText4 + ', ' + txtUVText5 + ', ' + txtUVAmount1 + ', ' + txtUVAmount2 + ', ' + txtUVNumeric1 + ', ' + txtUVNumeric2 + ', ' + txtUVDecimal1 + ', ' + txtUVNote_Text + ', ' + txtEquipment + ', ' + txtStatus + ')'

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
