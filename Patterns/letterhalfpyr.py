n=int(input("Enter a number:"))
for i in range(n+1):
    for j in range(65,i+65):
        a=chr(j)
        print(a,end=" ")
    print()

#Output
# Enter a number:5
# A 
# A B 
# A B C 
# A B C D 
# A B C D E 
