
import teradatasql as tds
import pandas as pd
import csv

hostn="192.168.170.128"
usern="dbc"
passw="dbc"

#query blocks

statement="""
sel databasename, tablename from dbc.tables sample 10
"""

with tds.connect(host=hostn,user=usern,password=passw) as sessionTD:
    df=pd.read_sql(statement,sessionTD)
    
data_output=df.to_csv(index=False, header=False) #suppress index column and the column header

f=open('data.txt','w')
f.write(data_output)
f.close()
