print("1.Addition\t2.Subtraction\t3.Multiplication\t4.Division\t5.Square\t6.Cube\t7.Sqaure Root\t8.Cube Root\t9.Factorial\t10.To get remainder\t11.Convert radians to degrees\t12.Convert degrees to radians\t13.To calculate reciprocal\t14.Raise number to some power")
ch='y'
while(ch=='y' or ch=='Y'):
    print("Enter operation you want")
    x=int(input(""))
    if x not in range(1,15):
        print("Enter valid input")
    elif(x==1):
        a=float(input("Enter first number"))
        b=float(input("Enter second number"))
        c=a+b
        print("Sum is",c)
    elif(x==2):
        a=float(input("Enter first number"))
        b=float(input("Enter second number"))
        c=a-b
        print("Difference is",c)
    elif(x==3):
        a=float(input("Enter first number"))
        b=float(input("Enter second number"))
        c=a*b
        print("Product is",c)
    elif(x==4):
        a=float(input("Enter first number"))
        b=float(input("Enter second number"))
        c=a/b
        print("Qoutient is",c)
    elif(x==5):
        a=float(input("Enter number"))
        b=a**2
        print("Square is",b)
    elif(x==6):
        a=float(input("Enter number"))
        b=a**3
        print("Cube is",b)
    elif(x==7):
        a=float(input("Enter number"))
        b=a**0.5
        print("Square root is",b)
    elif(x==8):
        a=float(input("Enter number"))
        b=a**(1/3)
        print("Cube root is",b)
    elif(x==9):
        a=float(input("Enter number"))
        fact=1
        i=1
        while(i<=a):
            fact=fact*i
            i=i+1
        print("Factorial is",fact) 
    elif(x==10):
        a=float(input("Enter first number"))
        b=float(input("Enter second number"))
        c=a%b
        print("Remainder is",c)
    elif(x==11):
        a=float(input("Enter angle in radians"))
        b=a*57.2958
        print("In degrees it is",b)
    elif(x==12):
        a=float(input("Enter angle in degrees"))
        b=a/57.2958
        print("in radians it is",b)
    elif(x==13):
        a=float(input("Enter number"))
        b=1/a
        print("Reciprocal is",b)
    elif(x==14):
        a=float(input("Enter base value"))
        b=float(input("Enter power"))
        c=a**b
        print("Answer is",c)
    ch=input("Do you want to operate again?(y for yes)")
