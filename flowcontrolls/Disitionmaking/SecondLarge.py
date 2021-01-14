num1=int(input("enter the 1num"))
num2=int(input("enter the 2num"))
num3=int(input("enter the 3num"))
if ((num1>num2)&(num1>num3)):
    if(num2>num3):
        print(num2,"is second large ")
        print("sorted order",num1,num2,num3)
    else:
        print(num3 ,"is 2larg")
        print("sorted order",num1,num3,num2)

elif ((num2>num1)&(num2>num3)):
    if(num1>num3):
        print(num1,"is 2nd large")
        print("sorted order",num2,num1,num3)
    else:
        print(num3,"is 2larg")
        print("sorted order",num2,num3,num1)

elif ((num3 > num1) & (num3 > num2)):
    if(num1>num2):
        print(num1,"is 2larg")
        print("sorted order",num3,num1,num2)
    else:
        print(num2,"is 2nd large")
        print("sorted order",num3,num2,num1)

else:
    print("numbers are equal")