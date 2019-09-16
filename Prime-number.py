x=int(input("Enter number"))
if(x==1):
    print("It is neither prime nor composite")
else:
    i=1
    count=0
    while(i<=x):
        if(x%i==0):
            count=count+1
        i=i+1
    if(count==2):
        print("It is a prime number")
    else:
        print("It is not a prime number")
