import streamlit as st
import numpy as np
try:
    f=open("gus.csv")
    b=[]
    c={}
    d={}
    r=[]
    p=[]
    count=0

    for x in f:
        b.append((x.rstrip()).split(","))
    for y in b:
        if y[13]=="corona virus" or y[13]=="Corona suspected":
            if y[2] in c:
                c[y[2]]=c[y[2]]+1
            else:
                c[y[2]]=1
        else:
            if y[2] in d:
                d[y[2]]=d[y[2]]+1
            else:
                d[y[2]]=1
    for x in list(c.items()):
        y=list(x)
        y.append("corona")
        p.append(tuple(y))
    for x in list(d.items()):
        y=list(x)
        y.append("non corona")
        p.append(tuple(y))
        print(y)
    xyz=[("vhname","S20"),("count",int),("ctype","S20")]
    a=np.array(p,dtype=xyz)
    b=np.sort(a,order="vhname")
    x=input("enter a vhicle id")
    for y in b:
        if x in y[0].decode('utf-8'):
            print(y)
finally:
    f.close("gus.csv")




