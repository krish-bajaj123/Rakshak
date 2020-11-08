import numpy as np
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
