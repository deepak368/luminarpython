num=int(input("enter the nnumber "))
flag=0
for i in range(2,num):
    print(i)
    if(num%i==0):
        flag=flag+1
        break
    else:
        pass
if(flag==0):
    print("prime number")
else:
    print("not prime")