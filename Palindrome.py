num=int(input("Enter a number:"))
y=num
reverse=0
while num>0:
    rem=num%10
    reverse=reverse*10+rem
    num=num//10
if reverse==y:
    print("Number" ,y, " is palindrome!!!")
else:
    print("Number" ,y, " is not palindrome!!!")
    
