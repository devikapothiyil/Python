listorg=["m","a","k","a","m"]
print(listorg)
listcp=listorg.copy()
listcp.reverse()
print(listcp)
if(listorg==listcp):
    print("Palindrome!!")
else:
    print("Not Palindrome!!")