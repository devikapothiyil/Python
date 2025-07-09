def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print("GCD:", gcd(48, 18))
