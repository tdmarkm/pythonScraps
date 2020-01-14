import teradatasql as tds
import pandas as pd

hostn="192.168.170.128"
usern="dbc"
passw="dbc"

#query blocks

statement="""
select time;
select date;
"""

results=[]
with tds.connect(host=hostn,user=usern,password=passw) as sessionTD:
    with sessionTD.cursor() as tdCur:      
        for query_line in statement.split(';'):
            tdCur.execute(query_line.strip())
            results+=tdCur.fetchall()
print(results)
