x=int(input("Enter number"))
sum=0
c=x

while(x>0):
    d=x%10
    x=x//10
    sum=sum+(d**3)
if(sum==c):
    print("It is an armstrong")
else:
    print("It is not an armstrong")
