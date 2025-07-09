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


# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True

# print(is_prime(7))  # True

    
        
        
    
