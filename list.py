lim=int(input("Enter the limit:"))
greatest=[]
for i in range(0,lim):
    num=int(input("Enter the number:"))
    greatest.append(num)
max=greatest[0]
for i in range (0,lim):
    if (max<greatest[i]):
        max=greatest[i]
print("The greatest number is ",max)

            
