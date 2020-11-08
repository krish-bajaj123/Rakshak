import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
st.write("""
# Ambulance Analysis Web Application
**Visually** show data on ambulance!
""")
image = Image.open("")
st.image(image, use_column_width=True)


st.sidebar.header("User Input")

def get_input():
    start_date=st.sidebar.text_input("Start Date","2020-01-02")
    end_date=st.sidebar.text_input("End Date", "2020-08-04")
    response_symbol=st.sidebar.text_input("Response Symbol" , "Response")
    return start_date, end_date
start= pd.to_datetime(start)
end= pd.to_datetime(end)

start_row=0
end_row=0

f=open("gus.csv")
b=[]
c={}
d=[]
r=[]
count=0
for x in f:
    b.append((x.rstrip()).split(","))
for y in b:
    if y[0] in c:
        c[y[0]]=c[y[0]]+1
    else:
        c[y[0]]=1
g=open("tqr.csv","w")
for j in c:
    if c[j]>1:
        g.write(str(j)+ ","+ str(c[j])+"\n")
g.close()
g=open("tqr.csv")
for x in g:
    r.append((x.rstrip()).split(","))
h=open("gtr.csv","w")
for p in r: 
    for y in b:
        if y[0].rstrip()==p[0].rstrip():
            print(y)
            count=count+1
        
print(count)


g.close()
h.close()
f.close()


