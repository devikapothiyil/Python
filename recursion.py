def recursion(num):
    if num == 0: 
        return 1
    else:
        return num * recursion(num - 1)

num = int(input("Enter the number: "))
factorial = recursion(num)
print("Factorial of", num, "is", factorial)
