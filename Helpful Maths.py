x = str(input())
y = []
# a = []
k = []


for i in range(0,len(x)):
    if i%2==0:
        z = y.append(x[i])
    # elif i%2!=0:
    #     d = a.append(x[i])

y.sort()        
for i in range(0,len(y)):
    k.append(y[i])
    if i<len(y)-1:
        k.append("+")
    

o = "".join(k)

print(o)
    
