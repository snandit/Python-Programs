day=int(input("Enter day"))
m=int(input("Enter month"))
year=int(input("Enter year"))
if(day<0 or m<0 or year<0):             #to check for negative values
    print("Enter valid input")
if(day>31 or m>12):
    print("Enter valid input")
if(m==4 or m==6 or m==9 or m==11):      #to check day=31 and valid month
    if(day==31):
        print("Enter valid input")
    elif(day<30):
        day=day+1
if(m==2):
    if(day>29):
        print("Enter valid input")
    
        



        
if(year%4==0):                              #to check for leap year
    
    if(year%100==0 and year%400==0):
        x=1
    if(year%4==0 and year%100!=0):
        x=1
    if(year%100==0 and year%400!=0):
        x=0
else:
    x=0

if (m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
    if(day<31):
        day=day+1

if(x==0 and m==2):                          #to check if not a leap year and day=29
    if(day==29):
        print("Enter valid input")
    if(day==28):
        day=1
        m=m+1
    else:
        day=day+1
if(x==1 and m==2):                          #to check if it is a leap year and day=29
    if(day==29):
        day=1
        m=m+1
    else:
        day=day+1
    

        
    

if(m==12 and day==31):
    year=year+1
    day=1
    m=1
if(m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
    if(day==31):
        day=1
        m=m+1
if( m==4 or m==6 or m==9 or m==11):
    if(day==30):
        day=1
        m=m+1
print(f'Day is {day} \n Month is {m} \n Year is {year}')    
