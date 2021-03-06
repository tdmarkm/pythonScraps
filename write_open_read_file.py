
import teradatasql as tds
import pandas as pd

hostn="192.168.170.128"
usern="dbc"
passw="dbc"


#write block starts
#query blocksstatement="""
sel databasename, tablename from dbc.tables sample 10
"""

with tds.connect(host=hostn,user=usern,password=passw) as sessionTD:
    df=pd.read_sql(statement,sessionTD)

data_output=df.to_csv(index=False, header=False) #suppress index column and the column header

f=open('data.txt','w')
f.write(data_output)
f.close()
#write block ends

#read block starts
df=pd.read_csv(r"data.txt")
df=df.to_dict()  #makes it easier to handle the dataframe data into tables

print(len(df['TableName'])) #max record

results=[]
with tds.connect(host=hostn,user=usern,password=passw) as sessionTD:
    with sessionTD.cursor() as curr:
        for x in range(0 , len(df['TableName'])):
            statement = "insert into pua_test_db.testtable values ('"+df['DatabaseName'][x].strip()+"','"+df['TableName'][x].strip()+"')" 
            print(statement)
            curr.execute(statement)
        results+=curr.fetchall()  #this closes the cursor hence the placement
#read block ends
