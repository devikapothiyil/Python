n=int(input("Enter a number:"))
for i in range(n,1,-1):
     for j in range(n-i):
         print(" ",end=" ")
     for k in range(i,2*i-1):
         print("*",end=" ")
     for m in range(1,i-1):
         print("*",end=" ")
     print()

#output
#* * * * *
#  * * * 
#    *
 
