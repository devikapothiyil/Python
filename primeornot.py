def check(num):
    for i in range(2,num):
        if(num%i)==0:
            return 1
        return 0
num=int(input("Enter the number:"))
x=check(num)
if x==1:
    print("Number is not prime")
else:
    print("Number is prime")
    
        
        
    
