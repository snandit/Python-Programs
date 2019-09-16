x=int(input("Enter number"))
pal=0
c=x
while(x>0):
    d=x%10
    x=x//10
    pal=pal*10+d
if(pal==c):
    print("It is a pallindrome")
else:
    print("It is not a pallindrome")
