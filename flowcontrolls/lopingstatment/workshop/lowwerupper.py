num=int(input("enter the number"))
upper=int(input("enter the upper limit"))
low=int(input("enter the lower limit"))
for i in range(1,upper+1):
    if i**num in range(low,upper+1):
        print(i**num)
    else:
        pass