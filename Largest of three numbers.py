num1=int(input("enter the number :"))
num2=int(input("enter the number :"))
num3=int(input("enter the number :"))
a= ("all are equal")
if num1==num2==num3 :
    print(a)
elif num1>=num2 and num1>= num3:
    print(num1 , "is the largest ")
elif num2 >= num3 and num2>=num1:
    print(num2 , "is the largest ")
    if num1==num2==num3:
        print("all are equal")
else:
    print(num3, "is the largest")
