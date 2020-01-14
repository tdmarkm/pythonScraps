import teradatasql as tds
import pandas as pd

hostn="192.168.170.129"
usern="dbc"
passw="dbc"

#query blocks

statement="""
sel * from dbc.tables
"""

with tds.connect(host=hostn,user=usern,password=passw) as sessionTD:
    df=pd.read_sql(statement,sessionTD)
#print(df)
print(df.columns.tolist())
print(df[['DatabaseName','TableName']][1:10])  #addressing example using column and rangeslice
print(df.loc[[1,3]]['TableName'])  #addressing example using Index
