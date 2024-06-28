lim=int(input("Enter limit:"))
numbers=[]
odd=[]
even=[]
for i in range (0,lim):
    num=int(input("Enter the number:"))
    numbers.append(num)
for i in range (0,lim):
    if(numbers[i]%2==0):
        even.append(numbers[i])
    else:
        odd.append(numbers[i])
print("LIST:",numbers)
print("ODD NUMBERS:",odd)
print("EVEN NUMBERS:",even)
     
