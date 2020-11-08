f=open("fpd.csv")
b=[]
c=[]
d={}
r=[]
p=[]
count=0

for x in f:
    y=(x.rstrip()).split(",")
    if y[14]!="":
        b.append(y)
for x in b:
    print(x[14])
for y in range(len(b)):
    j=b[y][4].split(" ")
    print(j)
for x in j:
        if int(x[1])<12:
            int(x[1])+24
            b[y].append(int(x[1]))
print(b)
for y in b:
    if int(y[14])<12:
        int(y[14])+24
        p.append(int(y[14]))
for x in r:
    for y in p:
        c.append(x-y)
f.close()
    

