x=int(input("Enter number"))
a=0
b=1
i=0
print(a,"\n",b)
while(x>i):
    c=a+b
    a=b
    b=c
    i=i+1
    if(c<x):
        print("\n",c)
    
