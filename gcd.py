def computeGCD(x, y):

    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small+1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i

    return gcd


a = int(input("Enter the First Number: "))
b = int(input("Enter the Second Number: "))

print("The Gcd of %d and %d is : " % (a, b), end='')
print(computeGCD(a, b))
