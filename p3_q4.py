sec=int(input("Enter seconds"))

if(sec<60):
    sec=sec/60
    print("it is equal to",sec,"seconds")
    
if(sec<3600):
    mint=int(sec/60)
    sec=sec%60
    print("it is equal to",mint,"minutes",sec,"seconds")

if(sec>=3600):
    hour=sec//3600
    temp=sec%3600
    mint=temp//60
    temp2=temp%60
    
    print("it is equal to",hour,"hours",mint,"minutes",temp2,"seconds")
