def rec_factorial(n):
    if(n==1 or n==0):
        return 1
    return n*rec_factorial(n-1)


def factorial(n):
    fac=1
    for i in range(1,n+1):
        fac=fac*i
    return fac
num=int(input("Enter the number: "))


print(factorial(num))
print(rec_factorial(num))