num1=int(input("enter the 1num"))
num2=int(input("enter the 2num"))
num3=int(input("enter the 3num"))
if ((num1>num2)&(num1>num3)):
    print(num1 ,"is larg")
elif ((num2>num1)&(num2>num3)):
    print(num2,"is larg")
elif ((num3 > num1) & (num3 > num2)):
        print(num3,"is larg")
else:
    print("numbers are equal")