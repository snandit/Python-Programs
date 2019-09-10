a=int(input("Enter square coefficient"))
b=int(input("Enter x coefficient"))
c=int(input("Enter constant"))
d=(b**2-(4*a*c))
if(d>0):
    print("Roots are real")
else:
    print("Roots are imaginary")
root1= (-b +(d**0.5))/2*a
root2= (-b -(d**0.5))/2*a
#print(f'Roots are {root1} \n {root2}')
print("Roots are",root1,"\n",root2)
