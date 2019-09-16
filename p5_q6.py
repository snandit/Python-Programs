x=int(input("Enter number"))
sum=0
while(x>0):
    d=x%10
    x=x//10
    sum=sum+d
print("Sum is ",sum)
