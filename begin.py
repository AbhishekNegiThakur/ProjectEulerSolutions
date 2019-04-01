s1=0
s2=0
for i in range(3,1000,3):
    if(i%5==0):
        continue
    else:
        s1=s1+i


for j in range(5,1000,5):
    s2=s2+j


print(s1+s2)


