#if we enter 2
#result #2+22
num=input("enter the number")
data=""
res=0
for i in range(1,int(num)+1):
    data=num*i
    res=res+int(data)
print(res)