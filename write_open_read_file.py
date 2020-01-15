
import teradatasql as tds
import pandas as pd

#query blocks
query="""
insert pua_test_db.testtable 
"""

df=pd.read_csv(r"data.txt")
df=df.to_dict()  #makes it easier to handle the dataframe data into tables

print(len(df['TableName'])) #max record

hostn="192.168.170.128"
usern="dbc"
passw="dbc"

results=[]
with tds.connect(host=hostn,user=usern,password=passw) as sessionTD:
    with sessionTD.cursor() as curr:
        for x in range(0 , len(df['TableName'])):
            statement = "insert into pua_test_db.testtable values ('"+df['DatabaseName'][x].strip()+"','"+df['TableName'][x].strip()+"')" 
            print(statement)
            curr.execute(statement)
        results+=curr.fetchall()  #this closes the cursor hence the placement
